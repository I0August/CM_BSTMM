% MP_Ecoli.m
%
% This file is part of the study presented in the paper:
% "A coupled metabolic flux/compartmental hydrodynamic
% model for large-scale aerated bioreactors".
%
% Authors:
% Ittisak Promma, Nasser Mohieddin Abukhdeir, Hector Budman, Marc G. Aucoin
%
% Institution:
% Dept. of Chemical Enginnering, University of Waterloo
%
% Contact:
% itpromma@outlook.com
%
% Description:
% This script performs multiparametric analysis and hyperplane partitioning
% for metabolic reactions in large-scale aerated bioreactors. It sets up
% and solves the multiparametric problem to optimize fluxes, identifies
% unique hyperplanes across partitions, and saves the results for further analysis.
%
% Usage:
% Ensure that all necessary toolboxes and dependencies are installed.
% Run the script in MATLAB to obtain the results.
%

% Clear the command window and workspace variables
clc;
clear;

% Set MPT options for linear programming solver
mptopt('lpsolver', 'CDD', 'rel_tol', 1e-6, 'abs_tol', 1e-10, 'lex_tol', 1e-10);

% Define matrix A, representing metabolic reactions
A = [0     -9.46   -9.84   -19.23;...   % Glucose (glc)
    -35    -12.92  -12.73  0;...        % Oxygen (o2)
    -39.43   0       1.24    12.12;...  % Acetate (ace)
    1        1      1        1];        % Biomass (x)

c = A(4,:);   % Objective coefficients

% Define constants for metabolic parameters
Km = 0.015;        % [mM]
GUR_max = 6.5;     % [mM/g-dw/h]
OUR_max = 12;      % [mM/g-dw/h]
AUR_max = 100;
kla = 4;           % [h^-1]

% Define constraints for the fluxes
Constr = [-A(1,:); -A(2,:); -A(3,:); -A(1:3,:)];

flux = sdpvar(4,1);     % Decision variables for fluxes
theta = sdpvar(6,1);    % Parameter variables

obj = -c*flux;          % Linear programming objective

G = [eye(6)];  % Identity matrix for constraints

% Constraints definition
Con1 = [Constr*flux <= G*theta, flux >= 0];

% Create an optimization problem
plp = Opt(Con1, obj, theta, flux);
solution = plp.solve(); % Solve the optimization problem

S = solution.xopt.Set;  % Extract the solution set

NP = length(S);  % Number of partitions
HK = {};
vertices = {};
F = {};
g = {};
Tol = 1e-20;     % Tolerance for numerical comparisons

% Extract hyperplanes, vertices, and primal functions for each partition
for i = 1:NP
    HK{i} = S(i).H;
    vertices{i} = S(i).V;
    F{i} = solution.xopt.Set(i).Functions('primal').F;
    g{i} = solution.xopt.Set(i).Functions('primal').g;
end

% Find unique hyperplanes across all partitions
hyperplanes = {};
for i = 1:length(S(1).H)
    hyperplanes{i} = S(1).H(i,:);
end

for j1 = 2:NP
    for j2 = 1:length(S(j1).H)
        l = 0;
        for j3 = 1:length(hyperplanes)
            if norm(hyperplanes{j3} - S(j1).H(j2,:)) < Tol || norm(hyperplanes{j3} + S(j1).H(j2,:)) < Tol
                l = l + 1;
            end
        end
        if l == 0
            i = i + 1;
            hyperplanes{i} = S(j1).H(j2,:);
        end
    end
end

% Determine the indices of hyperplanes in each partition
hps_inside_regions = {};
for k1 = 1:NP
    I = [];
    for k2 = 1:length(HK{k1})
        for k3 = 1:length(hyperplanes)
            if norm(HK{k1}(k2,:) - hyperplanes{k3}) < Tol
                I(k2) = k3;
            elseif norm(HK{k1}(k2,:) + hyperplanes{k3}) < Tol
                I(k2) = -k3;
            end
        end
    end
    hps_inside_regions{k1} = I;
end

% Save results to a .mat file
save('resources/BSTMM/MP_ecoli', 'vertices', 'hyperplanes', 'hps_inside_regions', 'F', 'g');