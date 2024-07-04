"""
--------------------------------------------------------------------------
File Name: bstFunctions.py

Purpose:
This script provide all the functions necessary for constructing the BST

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

import numpy as np
import random
from numpy import ndarray
from typing import *
import scipy.io as sio
from numba import njit


def import_tree_ingredient(file_name: str, tree_construction: bool = False) -> dict:
    """
    Function to import and prompt the necessary data for constructing the tree or locating points.
    The data is imported from a .mat file (Matlab object) which stores the data under the same name.

    For a critical region i, it is stored as a 1-D NumPy array of the signed indices, (+/-) j+1, of hyperplane
    objects bounding the critical region, where the equations of these hyperplanes, H[j] x = K[j], are stored in
    parameters H and K. The coordinates of a critical region are also stored for further use.

    :param file_name: String of the file name containing the .mat file
    :param tree_construction: Boolean that denotes if the data is for tree construction (True) or point location (False)
    :return: Dictionary of data required for either tree construction or point location

    If tree_construction = True, the function returns data needed for tree construction:
        - vertices: Numpy array where each index i is another array containing the coordinates of critical region i
        - hps_inside_regions: Numpy array where each index i is another array containing the signed indices j+1 of
                              hyperplanes forming critical region i
        - H: Numpy array where each index j is another array containing the coefficients H of the hyperplane equation,
             H[j] x = K[j]
        - K: Numpy array where each index j is the coefficient K of the hyperplane equation, H[j] x = K[j]

    If tree_construction = False, the function returns data needed for point location:
        - F: Numpy array where each index i is another array containing the coefficients F in the rate law equation,
             rate = F[i] x + g[i]
        - g: Numpy array where each index i is another array containing the coefficients g in the rate law equation,
             rate = F[i] x + g[i]
        - H: Numpy array where each index j is another array containing the coefficients H of the hyperplane equation,
             H[j] x = K[j]
        - K: Numpy array where each index j is the coefficient K of the hyperplane equation, H[j] x = K[j]

    Note:
    - hps_inside_regions is a 2-D Numpy array where each row stores an array of signed indices of hyperplanes bounding
      a critical region. The signs indicate which side of the hyperplane the critical region is located.
      - If it is a positive index (+(j+1)), the critical region is on the side that vector H[j] points into.
      - If it is a negative index (-(j+1)), the critical region is on the side that vector -H[j] points into.

    Example:
    1D Domain:   [ |-> CR_1 |-> CR_2 |-> CR_3 <-| ]
                    ^H[1]     ^H_2    ^H_3     ^H_4
    where: 
        - CR_i is critical region i
        - H_j is a vector of the coefficients of the hyperplane equation H_j x = K_j, which is perpendicular to the hyperplane.

    hps_inside_regions = [[+H_1,-H_2],[+H_2,-H_3],[+H_3,+H_4]]
                              ^CR_1        ^CR_2       ^CR_3

    In words, CR_1 is bounded by hyperplane no.1 and no.2, with the equations of both hyperplanes being H[0] x = K[0]
    and H[1] x = K[1], respectively.
    """

    data = sio.loadmat(file_name)

    # The values of H and K define a hyperplane as Hx = K. hyperplanes[i] contains H[i] and K[i] for the ith hyperplane.
    hyperplanes = data['hyperplanes'][0]
    # Preallocate H and K which are coefficients of the hyperplane equation, Hx = K.
    H = np.zeros((hyperplanes.shape[0], hyperplanes[0].shape[1] - 1), dtype=np.float64)
    K = np.zeros((hyperplanes.shape[0], 1), dtype=np.float64)

    # Fill H and K arrays
    for i in range(hyperplanes.shape[0]):
        row = hyperplanes[i]
        H[i] = row[0][0:-1]
        K[i] = row[0][-1]

    if tree_construction:
        vertices = data['vertices'][0]
        # The indices of the hyperplanes binding each critical region, where the ith entry is for the ith critical region.
        hps_inside_regions = data['hps_inside_regions'][0]
        return {'vertices': vertices, 'hps_inside_regions': hps_inside_regions, 'H': H, 'K': K}
    else:
        FF = data['F'][0]
        gg = data['g'][0]
        F = np.empty((len(FF), len(FF[0]), len(FF[0][0])))
        g = np.empty((len(gg), len(gg[0])))
        for n in range(len(gg)):
            F[n, :, :] = FF[n]
            g[n, :] = gg[n].transpose()
        return {'F': F, 'g': g, 'H': H, 'K': K}

class BSTnode:
    def __init__(self, regions: List[int] = None, hyperplane: int = None, l: int = 0) -> None:
        """
        Initialize a node in the Binary Search Tree (BST).

        The BSTnode class stores the structure of a binary search tree, where each node has:
        - regions: List of indices of critical regions representing a collection of regions within the state space.
        - hyperplane: Index of the hyperplane used for partitioning.
        - left: Reference to the left child node, storing critical regions on one side of the hyperplane.
        - right: Reference to the right child node, storing critical regions on the other side of the hyperplane.

        Example:
        1D Domain:   [ CR_1 | CR_2 | CR_3 ]
                            ^HP_1   ^HP_2
        where: CR_i is critical region i, HP_j is hyperplane j.
        Binary Tree:    {NULL/BSTnode0}
                         /    HP_1    \
                {CR_2/BSTnode1}   {NULL/BSTnode2}
                                  /      HP_2     \
                            {CR_1,BSTnode3}    {CR_3/BSTnode4}

        The first node (BSTnode0), also known as the root node, stores the data as follows:
        self.regions = [CR1, CR2, CR3]
        self.hyperplane = HP_1
        self.left = BSTNode1
        self.right = BSTNode2

        The second node (BSTnode1), also known as a leaf node, stores the data as follows:
        self.regions = [CR2]
        self.hyperplane = None
        self.left = None
        self.right = None

        The second node (BSTnode2), also known as an internal node, stores the data as follows:
        self.regions = [CR1, CR3]
        self.hyperplane = HP_2
        self.left = BSTNode3
        self.right = BSTNode4
        """
        self.hyperplane = hyperplane
        self.regions = regions
        self.node_id = 0
        self.layer = 0
        self.left = None
        self.right = None

    def to_dict(self) -> dict:
        """
        Convert the BST node to a nested dictionary representation.

        :return: Nested dictionary representation of the BST node with keys 'left', 'right', 'regions', 'Hyperplane'.

        Example:
            The dictionary result of the 1D Domain (see class BSTnode) is:
            {'regions':[CR1, CR2, CR3], 'Hyperplane': P_1, 'left': {'regions':[CR2]}, ...
             'right': {'regions':[CR1, CR3], 'Hyperplane': P_2, 'left': {'regions':[CR1]}, ...
             'right': {'regions':[CR3]}}}
        """
        regions = self.regions
        hyperplane = self.hyperplane
        left = self.left
        if left is not None:
            left = left.to_dict()
        right = self.right
        if right is not None:
            right = right.to_dict()
        if left is None and right is None:
            return {'regions': regions}
        return {'left': left, 'right': right, 'regions': regions, 'Hyperplane': hyperplane}

    def to_ndarray(self, list_nd=None) -> ndarray:
        """
        Convert the BST node to a NumPy ndarray structure.

        :return: NumPy ndarray representation of the BST node.

        Example:
            The ndarray result of the 1D Domain (see class BSTnode) is:
            [[HP_1, BSTnode1, BSTnode2], [CR2, -1, -1],
             [HP_2, BSTnode3, BSTnode4], [CR1, -1, -1],
             [CR3, -1, -1]]
        """
        if list_nd is None:
            list_nd = []

        hyperplane = self.hyperplane
        regions = self.regions
        left = self.left
        right = self.right
        if left is not None:
            list_nd.append([hyperplane, left.node_id, right.node_id])
            left.to_ndarray(list_nd)
            right.to_ndarray(list_nd)
        if left is None:
            list_nd.append([int(regions[0]), 0, 0])

        return np.array(list_nd)

    def to_list(self) -> list:
        """
        Convert the BST node to a nested list representation.

        :return: Nested list representation of the BST node with the order [left, right, regions, hyperplane].

        Example:
            The list result of the 1D Domain (see class BSTnode) is:
            [[CR2], [[CR1], [CR3], [CR1, CR3], P_2], [CR1, CR2, CR3], P_1]
        """
        hyperplane = self.hyperplane
        regions = self.regions
        left = self.left
        if left is not None:
            left = left.to_list()
        right = self.right
        if right is not None:
            right = right.to_list()
        if left is None and right is None:
            return regions
        return [left, right, regions, hyperplane]

    def list_to_BSTclass(self, nlt: list) -> None:
        """
        Convert a nested list representation back to a BST node class.

        :param nlt: Nested list tree.
        :return: None

        Example:
            bst = BSTnode()
            bst.list_to_BSTclass(nlt)
        """
        if not self.regions:
            self.regions = nlt[-2]
        if len(self.regions) > 1:
            self.hyperplane = nlt[-1]
            self.left = BSTnode(nlt[0])
            self.left.list_to_BSTclass(nlt[0])
            self.right = BSTnode(nlt[1])
            self.right.list_to_BSTclass(nlt[1])

    def depth(self) -> int:
        """
        Determine the depth (or height) of the BST.

        :return: The depth (or height) of the tree.
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def size(self) -> int:
        """
        Determine the size of the BST (i.e., the number of nodes in the tree).

        :return: The size of the tree.
        """
        count = 1
        if self.left:
            count += self.left.size()
        if self.right:
            count += self.right.size()
        return count

def tree_construction(bst: BSTnode, regions: List[int], vertices: ndarray, H: ndarray, K: ndarray,
                      hps_inside_regions: ndarray, l : list = [0], layer : int = 0, balanced = False):
    """
    Function to construct a binary search tree from the verticies and hyperplanes binding the critical regions.
    There is two modes available:
    1) Random method: (balanced = False) At each process of partitioning, a splitting hyperplane is randomly picking from
                      a set of potential hyperplane. (See random_tree)
    2) Balanced method: (balanced = True) ~, the splitting hyperplane that results in a balanced number of child regions
                      is chosen. (See balanced_tree)

    :param regions: List of indices of critical regions assembling a collection of regions within the state space
    :param vertices: Numpy array where each index i is another array containing all coordinates of a critical region i
    :param H: Numpy array where each index j is another array containing the coefficient H of the hyperplane equation,
              H[j] x = K[j]
    :param K: Numpy array where each index j is the coefficient K of the hyperplane equation, H[j] x = K[j]
    :param hps_inside_regions: Numpy array where each index i is another array containing the indices j of hyperplanes
           bounding the critical region i (See import_tree_ingredient)
    :return: None
    """
    # Update regions into the tree node
    bst.regions = regions

    # Update the layer
    bst.layer = layer
    layer += 1

    # Update the node id
    bst.node_id = l[0]
    l[0] += 1

    #  Index of hyperplane
    j = None

    if len(bst.regions) > 1:
        if balanced == True:
            # j, childnode = balanced_tree(bst.regions, hps_inside_regions, vertices, H, K)
            pass
        else:
            j, child_node = random_tree(bst.regions, hps_inside_regions, vertices, H, K)

    if j is not None:
        # Update the index of splitting hyperplane to the node
        bst.hyperplane = j

        # Update the list of regions on the left-child node
        bst.left = BSTnode()

        # Run the recursive function to create child nodes on the left-child node
        tree_construction(bst.left, child_node[0], vertices, H, K, hps_inside_regions, l, layer)

        # Update the list of regions on the right-child node
        bst.right = BSTnode()

        # Run the recursive function to create child nodes on the right-child node
        tree_construction(bst.right, child_node[1], vertices, H, K, hps_inside_regions, l, layer)

def random_tree(regions: List[int], hps_inside_regions: ndarray, vertices: ndarray, H: ndarray, K: ndarray)-> (int, List[int]):
    '''
    Function to randomly pick the splitting hyperplane to use to partition the critical regions. This function is called
    infrequently during construction of the tree in random mode (See tree_construction function)

    python
    Copy code
    :param regions: List of indices of critical regions assembling a collection of regions within the state space
    :param used_hp: List of used hyperplanes that fails to split the regions
    :param hps_inside_regions: Numpy array where each index i is another array containing the indices j of hyperplanes
                               forming the critical region i (See import_tree_ingredient)
    :param vertices: Numpy array where each index i is another array containing the vertices' coordinates of region i
    :param H: Numpy array where each index j is another array containing the coefficient H of the hyperplane equation,
              H[j] x = K[j]
    :param K: Numpy array where each index j is the coefficient K of the hyperplane equation, H[j] x = K[j]
    :return: Index of hyperplane that will be use as the splitting hyperplane
    '''

    used_j = []

    # (See j) it happens that some random hyperplane j fails to partition regions, the while-loop will keep
    # running until the result partitions differ from their parent regions.
    while True:

        # Calculate the index of the hyperplane to use for partitioning
        hp_id = list_HP_indices(regions, hps_inside_regions)

        # Get rid of duplicates
        ndp_j = np.unique(np.abs(hp_id))

        # The hyperplanes that did not share between any two regions
        ntoching_j = nontouching_HP(hp_id)

        # Remove the Hyperplane that is not touching with the others
        toching_j = np.setdiff1d(ndp_j, np.abs(ntoching_j), assume_unique=False)

        if len(toching_j) == 0:
            # Arrive at the case where two regions do not touch to each other
            jj = np.setdiff1d(ndp_j, used_j, assume_unique=False)
            j = random.choice(jj)
        else:
            # Arrive at the case that there exists at least two regions touching to each other
            toching_j = np.setdiff1d(toching_j, used_j, assume_unique=False)
            j = random.choice(toching_j)
        j = j-1

        # Create two child nodes and split the critical regions among them using hyperplane j
        child_node = split(regions, j, vertices, H, K)

        # Store used hyperplaneds
        used_j.append(j + 1)

        # Check if the result partitions differ from their parent regions, if so break the while loop
        if regions != child_node[0] and regions != child_node[1]:
            break
    return j, child_node

def split(regions: List[int], j: int, vertices: ndarray, H: ndarray, K: ndarray, eps = 1e-8) -> (List[int], List[int]):
    """
    Function to divide regions of a parent node into two regions of the two child nodes using the input hyperplane j.
    This function is called infrequently during construction of the tree (See tree_construction function).

    :param regions: List of indices of critical regions within the state space.
    :param j: Index of the hyperplane used for partitioning.
    :param vertices: Numpy array where each index i contains the vertices' coordinates of region i.
    :param H: Numpy array where each index j contains the coefficients H of the hyperplane equation, H[j] x = K[j].
    :param K: Numpy array where each index j contains the coefficient K of the hyperplane equation, H[j] x = K[j].
    :return: Tuple containing two lists, where each list contains indices of critical regions for each child node.

    The function partitions each critical region based on its positions relative to the hyperplane defined by H[j] x = K[j].
    

            |------|
            |  1   |
            |------|                                                     H[j]
                        |------|                                          ^
                        |  2   |        |------|                          |
        ----------------|------|--------|  3   |--------|------|----------|------ H[j] x = K[j]
                                        |------|        |  4   |
                                                        |------|
                                                                    |------|
                                                                    |  5   |
                                                                    |------|

    Scenarios:
    1. All vertices of a region are on the side that vector H[j] points into.
    2. Some vertices are on the hyperplane, and others are on the side that H[j] points into.
    3. Some vertices are on the side that H[j] points into, and some are on the side that -H[j] points into.
    4. Some vertices are on the hyperplane, and others are on the side that -H[j] points into.
    5. All vertices of a region are on the side that -H[j] points into.

    Each scenario determines whether a region belongs to the left child node, the right child node, or both.

    Note:
    - The calculation uses a small epsilon (eps) to compare against zero to handle numerical precision issues.
    - The '@' operator in 'vertices[cr_i] @ H[j]' performs matrix multiplication.
    """

    # Initialize the list holding the critical region numbers for the two child nodes
    left_child_node = []
    right_child_node = []

    # Iterate over all critical regions to be split among the child nodes
    for cr_i in regions:
        # Calculate what side of the hyperplane all vertices of the current critical region are on
        d = vertices[cr_i] @ H[j] - K[j]

        # Critical region completely on one side (Scenario 1 and 2)
        if all(d > -eps):
            left_child_node.append(cr_i)

        # Critical region completely on the one other side (Scenario 4 and 5)
        if all(d < eps):
            right_child_node.append(cr_i)

        # Critical region is split into two by hyperplane, it to both child nodes (Scenario 3)
        if any(d > eps) and any(d < -eps):
            left_child_node.append(cr_i)
            right_child_node.append(cr_i)

    return (left_child_node, right_child_node)

def list_HP_indices(regions: List[int], HK_indices: ndarray) -> ndarray:
    '''
    Miscellaneous function to help define all unique indices of hyperplanes of a input regions.

    :param regions: List of indices of critical regions assembling a collection of regions within the state space
    :param HK_indices: Numpy array where each index i is another array containing the indices j of hyperplanes forming
                       critical region i
    :return: Numpy array of all (signed) indices (See import_tree_ingredient) of hyperplanes
    '''

    # Initialize the list of possible hyperplanes
    y = HK_indices[regions[0]][0]

    # Add all possible indices of hyperplanes to the array
    for k in regions[1:]:
        x = HK_indices[k][0]
        y = np.append(x, y)

    return np.unique(y)


def nontouching_HP(y: ndarray) -> ndarray:
    """
    Function to calculate the hyperplane indices for the nontouching hyperplanes.
    This based on the idea that internal hyperplane indices show up twice (one positive and one negative) but
    region boundary ones only show up once (either positive or negative).

    :param y: Numpy array of all indices of hyperplanes from list_HP_indices function
    :return: Numpy array of indices of non-touching hyperplane

    Note:
    nontouching*: the term "nontouching", "nonbinding", or "nonsharing" are used instead of the term "boundary" because
                  seeing that most of the hyperplanes share only a part partially between two regions, the rest of
                  them remain able to be called "boundary", for example HP_1 on below picture:

                  |-------|
                  |       |------|
                  |       |      |
                  |       |______|
                  |-------|
                          ^HP_1
    """
    # Remove duplicates created by concatenating the binding hyperplanes of remaining critical regions
    y = np.unique(y)

    # Split the signed hyperplane numbers into positive and a negative sets
    y_neg = y[y < 0]
    y_pos = y[y > 0]

    # Find which negative hyperplane number do not have a matching positive one
    Jb1 = np.setdiff1d(np.abs(y_neg), y_pos, assume_unique=True)
    # Find which positive hyperplane number do not have a matching negative one
    Jb2 = np.setdiff1d(y_pos, np.abs(y_neg), assume_unique=True)

    return np.append(Jb1, Jb2)

def bst_point_location(x: ndarray, bst: BSTnode, H: ndarray, K: ndarray, eps: int = 1e-8) -> List[int]:
    '''
    Determine the region of a given query point, the class tree is required.

    :param x: Numpy array of a query point coordination
    :param bst: BSTnode tree
    :param H: Numpy array where each index j is another array containing the coefficient H of the hyperplane equation,
              H[j] x = K[j]
    :param K: Numpy array where each index j is the coefficient K of the hyperplane equation, H[j] x = K[j]
    :param eps: error tolerance (Default: eps= 1e-8)
    :return: the index of the critical region located the point
    '''

    if len(bst.regions) == 1:
        return bst.regions
    else:
        d = H[bst.hyperplane] @ x - K[bst.hyperplane]
        if d < eps:
            return bst_point_location(x, bst.right, H, K)
        else:
            return bst_point_location(x, bst.left, H, K)

@njit
def bst_ndarray_point_location(x: ndarray, bst_ndarray: ndarray, H: ndarray, K: ndarray, eps: int = 1e-8) -> int:
    '''
    Determine the region of a given query point, the binary search tree as the ndarray structure is required.

    :param x: Numpy array of a query point coordination
    :param bst_ndarray: ndarray 
    :param H: Numpy array where each index j is another array containing the coefficient H of the hyperplane equation,
              H[j] x = K[j]
    :param K: Numpy array where each index j is the coefficient K of the hyperplane equation, H[j] x = K[j]
    :param eps: error tolerance (Default: eps= 1e-8)
    :return: the index of the critical region located the point
    '''
    len_x = x.shape[1]
    region = np.zeros(len_x, dtype=np.int64)
    for i in range(len_x):
        j = 0
        while bst_ndarray[j, 1] != 0:
            hyperpland_id = bst_ndarray[j, 0]
            d = H[hyperpland_id] @ x[:,i] - K[hyperpland_id]
            if d < eps:
                j = bst_ndarray[j, 2]
            else:
                j = bst_ndarray[j, 1]
        region[i] = bst_ndarray[j,0]
    return region


