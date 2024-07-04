"""
--------------------------------------------------------------------------
File Name: mainIVP_7L.py

Purpose:
A sample simulation of a 7-L bioreactor for which the well-mixed approximation is justifiable,
a CSTR model is coupled with the binary search tree metabolic model to simulate the reactor.

This code is part of the study presented in the paper:
"A coupled metabolic flux/compartmental hydrodynamic model for large-scale
aerated bioreactors"

Authors:
Ittisak Promma, Nasser Mohieddin Abukhdeir, Hector Budman, Marc G. Aucoin

Institution:
Dept. of Chemical Engineering, University of Waterloo

Contact:
itpromma@outlook.com

Date:
19 Sept. 2023
--------------------------------------------------------------------------
"""


import bstFunctions as bstf
from scipy.integrate import BDF
import numpy as np
from numba import njit

@njit
def Source(t, y, yc, dt, teval, n_reactor, n_component, Q_vol, qI, yI,
           zone_feed, zone_outlet, zone_Probe, zone_Probe_O2, vol, A, H, K, F, g, bst_ndarray,
           K_Gmax, k_G, Y_EX, k_dE, K_Omax, n_r, k_dX, kLa, SatO2, K_c, tau_I, C_O2_set, r_star,
           etol=1e-8, eps=1e-10):
    """
    Calculate the source term for the simulation, including convection, inlet/outlet fluxes,
    gas transfer, dead reaction rates, and reaction fluxes.
    """

    # Calculate Q with oscillation
    alpha = 0
    omega = 1 / 1200
    Q_vol = Q_vol * (1 + (alpha * np.sin(omega * t)))

    # Calculate the convection flux between compartments
    CF = y @ Q_vol

    # Calculate the inlet flux
    QI = np.zeros((n_reactor, n_reactor), dtype=float)  # Convection into the system
    q_in = np.interp(t, teval, qI)
    QI[zone_feed, zone_feed] = q_in
    IF = yI @ QI  # mM/s
    IF[:, zone_feed] = IF[:, zone_feed] / vol[zone_feed]

    # Calculate the outlet flux
    QO = np.zeros((n_reactor, n_reactor), dtype=float)  # Convection out of the system
    QO[zone_outlet, zone_outlet] = -1 * q_in
    OF = y @ QO  # Define the outlet flux for the substrates (glucose, oxygen, acetate)
    OF[:, zone_outlet] = OF[:, zone_outlet] / vol[zone_outlet]
    OF[3, :] = 0 # No cell leave the system
    OF[4, :] = 0 # No enzyme leave the system

    # Calculate total convection flux
    TCF = CF + IF + OF

    # Calculate the gas tr cansfer flux and dead rate
    AF = np.zeros((n_component, n_reactor), dtype=float)  # Mass transport and others
    deltaSignal = -1 * K_c * (yc[1] + (1 / tau_I) * yc[0])
    kLa_C = kLa + (deltaSignal * kLa / kLa[zone_Probe[zone_Probe_O2]])
    AF[1, :] = (kLa_C) / 3600 * (SatO2 - y[1, :])
    AF[3, :] = -1 * k_dX * y[3, :] / 3600
    TCF += AF

    # Calculate reaction flux
    RF = np.zeros((n_component, n_reactor), dtype=float)  # Reaction

    # If dt is 0, we use another set of tree search to evaluate the case where dt equals zero
    if dt == 0:
        dt = 1e-15

    # Calculate the input for the tree search
    z = np.zeros((n_reactor, 5))
    z[:, 0] = K_Gmax * y[0, :] / (k_G + y[0, :])
    for i in range(n_reactor):
        if (y[4, i] / y[3, i]) < r_star:
                  z[i, 0] *= np.power(((y[4, i] / y[3, i])), n_r) / np.power(r_star, n_r)
        else:
            z[i, 0] *= 1
    z[:, 1] = K_Omax
    z[:, 2] = (y[0, :]) / ((dt / 3600) * (y[3, :]) + etol) + ((TCF[0, :] * 3600) / (y[3, :] + etol))
    z[:, 3] = y[1, :] / ((dt / 3600) * (y[3, :]) + etol) + ((TCF[1, :] * 3600) / (y[3, :] + etol))
    z[:, 4] = (y[2, :]) / ((dt / 3600) * (y[3, :]) + etol) + ((TCF[2, :] * 3600) / (y[3, :] + etol))

    # Define the reaction region for each compartment via point location method
    region = np.zeros(n_reactor, dtype=np.int64)
    rate = np.zeros((n_reactor, 4))
    flux = np.zeros((n_reactor, 4))
    for i in range(n_reactor):
        j = 0
        while bst_ndarray[j, 1] != 0:
            hyperpland_id = bst_ndarray[j, 0]
            d = H[hyperpland_id] @ z[i, :] - K[hyperpland_id]
            if d < eps:
                j = bst_ndarray[j, 2]
            else:
                j = bst_ndarray[j, 1]
        region[i] = bst_ndarray[j, 0]

    # Loop over the reactors to determine reaction rates for each of the reactors
    for i in range(n_reactor):
        # if there is no microorganisms, there is no rate.
        if y[3, i] != 0:
            flux[i, :] = F[region[i]] @ z[i, :] + g[region[i]]
            rate[i, :] = A @ flux[i, :]
            RF[:-1, i] = rate[i, :] * y[3, i] / 3600

        # Update reaction rate for the enzyme
        RF[-1, i] = (Y_EX * RF[-2, i]) - (y[4, i] * (k_dE + k_dX) / 3600)

    return CF + IF + OF + AF + RF

def wrapper_Source(t, y, **kwargs):
    """
    Wrapper function for the Source function to reshape input and output and calculate the
    rate of change of concentration as well as control laws.
    """

    # Declare variables
    n_c = kwargs["n_component"]
    n_r = kwargs["n_reactor"]
    zone_Probe = kwargs["zone_Probe"]
    zone_Probe_O2 = kwargs["zone_Probe_O2"]
    C_O2_set = kwargs["C_O2_set"]

    # Extract concentration and control parameter y from vector to matrix form
    yM = y[:n_c * n_r].reshape((n_c, n_r))
    yc = y[-2:]

    # Determine total flux/ rate for all compartments
    TF = Source(t, yM, yc, **kwargs)

    # Determine the rate of change of control laws
    E = np.array([yM[1, zone_Probe[zone_Probe_O2]] - C_O2_set, TF[1, zone_Probe[zone_Probe_O2]]])

    # Reshape the total flux matrix
    TF = TF.reshape((n_r * n_c))

    #Concanate the total flux and control laws to a single array
    f = np.concatenate((TF, E), axis=0)

    return f

def ivpSolver(fun, t0, y0, t_eval, t_feed, max_step = 10, **kwargs):
    """
    Solves an initial value problem (IVP) for a system of ODEs using the BDF method.
    """

    # Declare variables
    y_solution = np.zeros((kwargs["n_component"], kwargs["n_reactor"], len(t_eval)))
    control_solution = np.zeros((2, len(t_eval)))

    # Loop over the feeding times
    i = 0
    for j in range(len(t_feed)):
        # Initialize the solver
        sol = BDF(fun=lambda t, y: fun(t, y, **kwargs), t0=t0, y0=y0, t_bound=t_feed[j], max_step=max_step, atol=1e-8,
                  rtol=1e-5)

        # Solve until the current feeding time
        while sol.t < t_feed[j]:
            # Calculate the current time step
            kwargs['dt'] = t_eval[i] - sol.t

            # Take a solver step
            sol.step()

            # Save the value at each evaluation time
            while sol.t_old <= t_eval[i] <= sol.t:
                # Get the value at the evaluation time using interpolation
                yy = sol.dense_output()(t_eval[i])

                # Separate the solution of concentration profiles and control variables
                for jj in range(y_solution.shape[0]):
                    y_solution[jj, :, i] = yy[:-2][jj * y_solution.shape[1]:(jj + 1) * y_solution.shape[1]]

                control_solution[:, i] = yy[-2:]

                # Update the index
                i += 1
                if i == len(t_eval):
                    break

            # Update initial conditions for the next segment
            t0 = sol.t
            y0 = sol.y

    return [t_eval, y_solution, control_solution]

# Import BST resources for point location
ingredient = bstf.import_tree_ingredient('resources/BSTMM/MP_ecoli.mat')
F = ingredient['F']
g = ingredient['g']
H = ingredient['H']
K = ingredient['K']
bst_ndarray = np.load("resources/BSTMM/BST_ecoli.npy")

# Define reactor parameters
Q = np.array([[0]]).astype(float)  # Flow rate between compartments (m^3/s) (zero for batch system)
vol = np.array([7])  # Volume of the reactor

# Define stoichiometric matrix
A = np.array([[0, -9.46, -9.84, -19.23],
              [-35, -12.92, -12.73, 0],
              [-39.43, 0, 1.24, 12.12],
              [1, 1, 1, 1]])

# Extract information
n_reactor = len(Q)  # Number of reactors
n_component = 5  # Number of components

# Calculate Q/vol
Q_vol = Q.copy()
for k in range(n_reactor):
    Q_vol[:, k] = Q[:, k] / vol[k]

# Manually input the initial and feed concentration
y0 = np.zeros([n_component, n_reactor])
yI = np.zeros([n_component, n_reactor])

# Determine feed concentration (mmol/L)
zone_feed = 0
yI[0, zone_feed] = 532 * (1 / 180.156) * 1000
vol_feed = vol[zone_feed]

# Define evaluating time
t_begin = 0
delta_t = 1
t_end_in_hour = 40
t_end = t_end_in_hour * 3600
t_eval = list(np.arange(t_begin, t_end, delta_t))
t_eval.append(t_end)
t_feed = np.array([0.92, 8.23, 10.73, t_end_in_hour]) * 3600
t_eval = np.concatenate((t_eval, t_feed))
t_eval = np.unique(np.sort(t_eval))

# Inlet flow rate for semi batch system (L/sec)
qI = np.zeros(len(t_eval))
for i in range(len(t_eval)):
    if (t_eval[i] > 0.92 * 3600) and (t_eval[i] < 9.877 * 3600):
        qI[i] = (0.0057 / 3600) * np.exp((0.27 / 3600) * (t_eval[i] - (0.92 * 3600)))
    elif (t_eval[i] > 9.876 * 3600) and (t_eval[i] < 12.377 * 3600):
        qI[i] = 0.064 / 3600
    elif (t_eval[i] > 12.377 * 3600):
        qI[i] = 0.057 / 3600

# Define parameters (See Table 1: Model parameters)
K_Omax = 6
K_Gmax = 10
k_G = 0.2
k_dX = 0.04
Y_EX = 0.51
k_dE = 0.9
r_star = 0.2
n_r = 1.5
kLa = np.array([12.5])
C_O2_star = np.array([0.21])
K_c = 40
tau_I = 100
C_O2_set = 0.1

# Initial concentrations [g/L * mol/g * mmol/mol]
y0[0, :] = 0.563 * (1 / 180.156) * 1000         # mmol/L
y0[1, :] = 0.21                                 # mmol/L
y0[2, :] = 18.63 / 1000 * (1 / 60.052) * 1000   # mmol/L
y0[3, :] = 0.1                                  # g/L
y0[4, :] = 0.065                                # g/L

y0 = y0.reshape((n_component * n_reactor))

# Find initial condition for the controller
initial_error = 0.48
yc = np.array([0, initial_error])
y0 = np.concatenate((y0, yc))

# Store all parameters that will be used in the function
kwargs = {"dt": 0, "teval": t_eval, "n_reactor": n_reactor, "n_component": n_component,
          "Q_vol": Q_vol, "qI": qI, "vol": vol, "yI": yI,
          "zone_feed": zone_feed, "zone_outlet": zone_feed, "zone_Probe": np.array([0]), "zone_Probe_O2": 0,
          "A": A, "H": H, "K": K, "F": F, "g": g, "bst_ndarray": bst_ndarray,
          "K_Gmax": K_Gmax, "k_G": k_G, "Y_EX": Y_EX, "k_dE": k_dE,
          "K_Omax": K_Omax, "n_r": n_r, "k_dX": k_dX,
          "kLa": kLa, "SatO2": C_O2_star, "K_c": K_c, "tau_I": tau_I, "C_O2_set": C_O2_set, "r_star": r_star}

# Solve the system
sol = ivpSolver(wrapper_Source, t_begin, y0, t_eval, t_feed, **kwargs)
time = sol[0]
solution = sol[1]
control = sol[2]

# Convert units back
solution[0] = solution[0] * (180.156 / 1000)  # Convert to g/L
solution[2] = solution[2] * 60.052  # Convert to mg/L

# Save the results
np.save('time_7L', time)
np.save('solution_7L', solution)