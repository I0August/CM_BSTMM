CM_BSTMM

This directory provides functions and examples used in the simulation of a large-scale bioreactor as presented in
the paper "A coupled metabolic flux/compartmental hydrodynamic model for large-scale aerated bioreactors."

Authors: Ittisak Promma, Nasser Mohieddin Abukhdeir, Hector Budman, Marc G. Aucoin
Institution: Dept. of Chemical Engineering, University of Waterloo
Contact: itpromma@outlook.com
-------------------------------------------------------------------------------------------------------------------
Directory Structure:

OF_simulation
    Contains an OpenFoam case of the large-scale bioreactor

resources (Create via mainInitial.sh)
    Serves as a storage while simulating the provided Python/ Matlab scripts in this directory.

    - CFD: Properties or mesh data extracted from the OpenFOAM simulation.
    - CM: Data of the compartmental model used in the simulation.
    - BSTMM: Data of the binary search tree metabolic model used in the simulation.

Python/ Matlab scripts
    Contains various scripts to simulate a large-scale bioreactor.
-------------------------------------------------------------------------------------------------------------------
Simulation procedure:

Prerequisite:
1) An executed OpenFoam case with simulating fields stored at time 100 (default). We provide an 
   unexecuted OF case for the large-scale bioreactor; however, additional runs are necessary to 
   obtain the simulation results.

To run a simulation, the following scripts should be run in sequence:
1) mainInitial.sh: Create resorces files for data storing
2) MP_Ecoli.m (Requires Matlab and MPT3 module): Generate objects required to construct BST.
3) mainBST.py: Construct BST.
4) mainExtractCFD.py: Extract data from OF_simulation for further use.
5) mainCompartment.py: Generate a compartmental model.
6) mainExtractCM.py: Extract data from the compartmental model necessary for bioreactor simulation.
7) mainIVP_~.py: Run the simulation of the bioreactor.
-------------------------------------------------------------------------------------------------------------------

