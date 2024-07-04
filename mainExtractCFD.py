"""
--------------------------------------------------------------------------
File Name: mainExtractCFD.py

Purpose:
This script shows an example of how to extract OpenFoam data for further use.

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

"""
------------------------------------------------------------------------------------------------------------------------
                                PART 0: OpenFoam Data Extraction
------------------------------------------------------------------------------------------------------------------------                                                 
Import mesh and physical fields information by using my developed code
+ Physical Fiels and Some Mesh
   input >> path to access the physical fields
   output >> scalar fields at cell center and at the surface (interpolation) Example: velocity of phase i (U_i), 
             volumetric fractions
+ Mesh
   input >> path to access the mesh and physical fields information
   output >> point_to_Coordinates: a list of coordinates denoting the cell vertices
             face_to_points: a list of faces, with each face described by a list of indices to vertices in the points 
                             list
             face_to_element_ref: a list in which the element at one side of faces are stored 
                                  (for internal and boundary faces)
             face_to_element_neighbour: a list in which the element at the other side of faces are stored 
                                        (for only internal faces)

             |------------------|------------------| 
             |        ref       |                  |                  ref       neighbour
             |      (owner)     |    neighbour     |      face0    element10    element11
             |                  |                  |      face...     ...          ...
             |                  |-----> face 0     |
             |                  |                  |
             |     element10    |    element11     |
             |------------------|------------------|
             
------------------------------------------------------------------------------------------------------------------------
"""

def extractData (name, dir_data, dir_save, dataType = float):
    """
    A function used to facilitate data extraction

    Parameters:
    name (str): Name of the file containing the data.
    dir_data (str): Directory path where the data file is located.
    dir_save (str): Directory path where the extracted data will be saved.
    dataType (type, optional): Data type to be used during import (default is float).
    """
    data = importData(dir_data + name, dataType)
    np.save(dir_save + name, data)

# Provide the path where the data is stored
dir_data = 'OF_simulation/100/'
dir_mesh = "OF_simulation/constant/polyMesh/"
dir_save = 'resources/CFD/'

# Extract data 
extractData('UMean.water', dir_data, dir_save)
extractData('phiMean.water', dir_data, dir_save)
extractData('alphaMean.water', dir_data, dir_save)
extractData('epsilonMean.water', dir_data, dir_save)
extractData('pMean', dir_data, dir_save)
extractData('TMean.water', dir_data, dir_save)
extractData('V', dir_data, dir_save)
extractData('C', dir_data, dir_save)
extractData('points', dir_mesh, dir_save)
extractData('faces', dir_mesh, dir_save, int)
extractData('owner', dir_mesh, dir_save, int)
extractData('neighbour', dir_mesh, dir_save, int)










