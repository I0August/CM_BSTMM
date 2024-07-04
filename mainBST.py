"""
--------------------------------------------------------------------------
File Name: mainBST.py
 
Purpose:
This script imports data for tree construction, constructs a binary search tree (BST) 
using the imported data, and converts the BST to a NumPy array for further processing.

This code is part of the study presented in the paper:
"A coupled metabolic flux/compartmental hydrodynamic model for large-scale 
aerated bioreactors"

Authors: 
Ittisak Promma, Nasser Mohieddin Abukhdeir, Hector Budman, Marc G. Aucoin

Institution: 
Dept. of Chemical Enginnering, University of Waterloo

Contact:
itpromma@outlook.com

Date: 
19 Sept. 2023 
--------------------------------------------------------------------------
"""
# Import modules required
from bstFunctions import *

# Import data for tree construction
# This function imports the ingredient data and constructs an initial tree structure
bst = BSTnode()
ingredient_tree = import_tree_ingredient('resources/BSTMM/MP_ecoli.mat', tree_construction=True)

# Extract relevant data from the imported tree
vertices = ingredient_tree['vertices']
H = ingredient_tree['H']
K = ingredient_tree['K']
hps_inside_regions = ingredient_tree['hps_inside_regions']

# Index all critical regions and store them as a list
root: list = list(range(len(ingredient_tree['vertices'])))

# Construct a binary search tree (BST)
# This function constructs the BST from the indexed root and other data
tree_construction(bst, root, vertices, H, K, hps_inside_regions, balanced=False)

# Convert the BST to a NumPy ndarray structure
# bst_ndarray will store the BST in a ndarray format for further processing
bst_ndarray = bst.to_ndarray()

# Save the ndarray structure of the BST to a file
np.save("resources/BSTMM/BST_ecoli", bst_ndarray)




