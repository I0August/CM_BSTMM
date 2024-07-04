"""
--------------------------------------------------------------------------
File Name: mainExtractCM.py

Purpose:
This script computes physical properties (such as mass transfer coefficient kLa) used in the simulation,
and constructs the volumetric flow rate matrix from the information of the compartmental model.

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


from comFunctions import *

# Load data

zone_to_elements = loadPythonObject("resources/CM/zone_to_elements.pky")  # zone-to-elements mapping
zone_to_shells = loadPythonObject("resources/CM/zone_to_shells.pky")      # zone-to-shells mapping
zone_to_volume = np.load("resources/CM/zone_to_volume.npy")               # zone volumes
element_to_volume = np.load('resources/CFD/V.npy')                        # element volumes
element_to_coordinates = np.load('resources/CFD/C.npy')                   # coordinates of element centres
free_surface = loadPythonObject("resources/CM/free_surface.pky")          # free surface data
internalSurfaceArea = np.load('resources/CFD/internalSurfaceArea.npy')    # internal surface area
intarface_to_elements = np.load('resources/CFD/interface_to_elements.npy') # interface-to-elements mapping
volume = np.load('resources/CFD/V.npy')                                    # element volumes
alpha_water = np.load('resources/CFD/alphaMean.water.npy')                 # mean volume fraction of water
epsilon_water = np.load('resources/CFD/epsilonMean.water.npy')             # mean dissipation of turbulent kinetic energy
P = np.load('resources/CFD/pMean.npy')                                     # mean absolute pressure
T = np.load('resources/CFD/TMean.water.npy')                               # mean temperature
volFlowRate = np.load('resources/CFD/phiMean.water.npy')                   # mean volumetric flow rate

# Calculate the physical properties needed for simulation

# Calculate water volume using alpha_water and total volume
water_volume = alpha_water * volume

# Calculate gas volume as the complement to total volume
gas_volume = volume - water_volume

# Calculate inverse density (inv_rho) based on temperature (T) and pressure (P)
inv_rho = 0.001278 - (2.1055e-6)*T + ((3.9689e-9)*(T**2)) - (4.3772e-13)*P + (2.0225e-16)*P*T

# Calculate density (rho) from inverse density
rho = 1/inv_rho

# Calculate liquid viscosity (vl) based on density (rho)
vl = 3.645e-4 / rho

# Calculate bubble diameter (d_b) using pressure (P)
d_b = 3e-3 * (1e5/P) ** (1/3)

# Calculate specific interfacial area (a) based on alpha_water and bubble diameter (d_b)
a = 6 * (1 - alpha_water) / d_b

# Calculate mass transfer coefficient (kL) using epsilon_water, liquid viscosity (vl), and empirical factors
kL = 0.4 * ((2.42e-9) ** 0.5) * ((epsilon_water / vl) ** 0.25)

# Calculate overall mass transfer coefficient (kLa) using kL and specific interfacial area (a)
kLa = kL * a

# Calculate SATO2 using pressure (P)
SATO2 = 0.2095 * P / 8.010755e7 * 1000

# Determine the average properties of each zone
zone_to_water_volume = sumZoneData(water_volume, zone_to_elements)
zone_to_gas_volume = zone_to_volume-zone_to_water_volume
zone_to_kL = volumeAverageZoneData(kL, zone_to_elements, element_to_volume)
zone_to_kLa = volumeAverageZoneData(kLa, zone_to_elements, element_to_volume)
zone_to_SATO2 = volumeAverageZoneData(SATO2, zone_to_elements, element_to_volume)

# Determine the volumetric flow rate matrix

# Construct the volumetric flow rate matrix Q using constructInternalFlowNetwork function
Q = constructInternalFlowNetwork(zone_to_elements, zone_to_shells, volFlowRate, intarface_to_elements, uniDirection=False)

# Zero out the last row and column; these belong to the overhead compartment that is assumed
# that there is no mass transport in and out.
coordinate = [0.5, 0, 7]
element_to_zone = constructElementToZone(zone_to_elements)
overhead_zone = coordinateToZone(coordinate, element_to_coordinates, element_to_zone)
Q[:, -1] = 0
Q[-1, :] = 0

# At this point, Q has no diagonal components, which are crucial as they define the total
# volumetric flow rate out of compartments. These will be determined in the next step.

# Balance the mass in the volumetric flow rate matrix Q0 using the balanceMass function.
# Mass balance is crucial, especially for the results of two-phase simulations,
# as the method does not guarantee mass balance.
Q = balanceMass(Q)

# Save data for further use
np.save("resources/CM/zone_to_water_volume", zone_to_water_volume)
np.save("resources/CM/zone_to_kLa", zone_to_kLa)
np.save("resources/CM/zone_to_SATO2", zone_to_SATO2)
np.save("resources/CM/Q", Q)
