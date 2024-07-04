"""
--------------------------------------------------------------------------
File Name: comFunctions.py

Purpose:
This script provide all the functions necessary for compartmentalization OpenFoam results

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
import pickle

#-----------------------------------------------------------------------------------------------------------------------
# Function for save and load files
#-----------------------------------------------------------------------------------------------------------------------
def savePythonObject(fileName, parameter):
    """
    Save a Python object to a file using pickle.

    Parameters:
    fileName (str): The name of the file where the object will be saved (without extension).
    parameter (object): The Python object to be saved.
    """
    # Open a file with the given filename (adding .pky extension) in binary write mode
    with open(fileName + ".pky", 'wb') as file:
        # Serialize the Python object and save it to the opened file
        pickle.dump(parameter, file)


def loadPythonObject(fileName):
    """
    Load a Python object from a file using pickle.

    Parameters:
    fileName (str): The name of the file from which the object will be loaded (without or with .pky extension).

    Returns:
    object: The Python object that was loaded from the file.
    """
    try:
        # Attempt to open the file with the provided filename (without .pky extension) in binary read mode
        with open(fileName, 'rb') as file:
            # Deserialize the Python object from the file
            load_file = pickle.load(file)
    except:
        # If the first attempt fails, try to open the file with the .pky extension in binary read mode
        with open(fileName + '.pky', 'rb') as file:
            # Deserialize the Python object from the file
            load_file = pickle.load(file)

    # Return the loaded Python object
    return load_file


def importData(path_to_file, dataType=float, write_numpy=True):
    """
    Import mesh information from the polyMesh/XXX file to the Python environment.

    Parameters:
    path_to_file (str): The path to the file containing the mesh information.
    dataType (type): The type of data to be read (default is float).
    write_numpy (bool): Whether to convert the list of data to a numpy array (default is True).

    Returns:
    data (list or numpy array): The imported mesh data, either as a list or a numpy array.
    """
    # Declare variables
    data = []  # A list to store read data
    startRecord = 0  # A flag variable to tell the program to start reading the line

    # Open the file
    with open(path_to_file, 'r') as f:

        # Loop over each line in the file
        for line in f:

            # According to how OpenFOAM stores its data, if it finds a line with a single '(',
            # we set startRecord = 1 to start recording the data, then continue to the next line
            if line == '(\n':
                startRecord = 1
                continue

            # If it finds a line with a single ')', we set startRecord = 0 to stop recording the data, then break the loop
            if line == ')\n':
                break

            # If startRecord = 1, record the data
            if startRecord == 1:

                # There are two types of data: vector and scalar.
                # According to how OpenFOAM stores its data, a vector is stored as, for example, (10 2 3).
                # While a scalar is stored as a single number, for example, 5
                # If the line stores a vector (i.e., contains both '(' and ')')
                if line.find('(') >= 0 and line.find(')') >= 0:

                    # Record the datum as a vector
                    datum = line[line.find('(') + 1:line.find(')')]
                    vector = np.fromstring(datum, dtype=dataType,
                                           sep=' ')  # Create a new 1-D array from text data in a string
                    data.append(vector)

                # If the line stores a scalar, record the datum as the specific type of a scalar
                else:
                    if dataType == int:
                        data.append(int(line))
                    elif dataType == float:
                        data.append(float(line))

    # If write_numpy is True, convert the list to a numpy array
    if write_numpy:
        data = np.array(data)

    return data

#-----------------------------------------------------------------------------------------------------------------------
# Function to construct data maps (e.g. Element --> Face, Face --> Elements)
#-----------------------------------------------------------------------------------------------------------------------

def constructFaceToElements(owner, neighbour):
    """
    Combine two face-to-element data (owner and neighbour) to create a list of faces to elements.
    The list stores elements that are shared by each face.

    Parameters:
    owner (ndarray): Array containing the owner elements for each face.
    neighbour (ndarray): Array containing the neighbour elements for each face.

    Returns:
    face_to_elements_interFace (ndarray): 2D array where each row contains the owner and neighbour elements for internal faces.
    face_to_elements_boundaryFace (ndarray): 2D array where each row contains the owner element for boundary faces.
    """
    # Declare ndarrays to store data
    face_to_elements_interFace = np.zeros([len(neighbour), 2], dtype=int)  # Array for internal faces
    face_to_elements_boundaryFace = np.zeros([len(owner) - len(neighbour), 1], dtype=int)  # Array for boundary faces

    # Copy the data from the original objects
    face_to_elements_interFace[:, 0] = owner[:len(neighbour)]  # Owner elements for internal faces
    face_to_elements_interFace[:, 1] = neighbour  # Neighbour elements for internal faces
    face_to_elements_boundaryFace[:, 0] = owner[len(neighbour):]  # Owner elements for boundary faces

    return face_to_elements_interFace, face_to_elements_boundaryFace

def constructElementToFaces(owner, neighbour):
    '''
    Construct the connectivity map between elements and their associated faces
    using the provided face-to-element data (-ref and -neighbour).

    Parameters:
    owner (ndarray): Array where each entry represents the element ID on one side of the faces.
    neighbour (ndarray): Array where each entry represents the element ID on the other side of the faces.

    Returns:
    list_of_sets (list of sets): A list where each set contains the indices of faces associated with each element.
    '''
    element_to_faces = np.zeros([max(owner) + 1, 6], dtype=int)
    count = np.zeros(max(owner) + 1, dtype=int)
    for i in range(len(owner)):
        value = owner[i]
        element_to_faces[value, count[value]] = i
        count[value] = count[value] + 1
    for i in range(len(neighbour)):
        value = neighbour[i]
        element_to_faces[value, count[value]] = i
        count[value] = count[value] + 1

    # Get the number of rows in the NumPy array
    num_rows = element_to_faces.shape[0]

    # Convert each row of the NumPy array to a list of sets
    list_of_sets = []
    for i in range(num_rows):
        row = element_to_faces[i, :]  # Extract the i-th row
        row_set = set(row)  # Convert the row to a set
        list_of_sets.append(row_set)
    return list_of_sets

def constructElementToNeighbours(face_to_interElements):
    '''
    Construct a list of elements to their neighbour elements.

    Parameters:
    face_to_interElements (ndarray): 2D array where each row contains a pair of elements that share a face.

    Returns:
    neighbour (list of sets): A list where each index corresponds to an element, and the set at each index contains the neighbours of that element.
    '''
    # Extract the size (number of elements)
    n = np.max(face_to_interElements) + 1

    # Initialize a list of sets to store neighbours for each element
    neighbour = [set() for _ in range(n)]

    # Loop over each pair of elements in face_to_interElements
    for i in range(len(face_to_interElements)):
        # Add the neighbour elements to each other's sets
        neighbour[face_to_interElements[i][0]] |= {face_to_interElements[i][1]}
        neighbour[face_to_interElements[i][1]] |= {face_to_interElements[i][0]}

    return neighbour

def constructElementToZone(zone_to_elements):
    '''
    Construct a ndarray that maps each element to its zone.

    Parameters:
    zone_to_elements (list of lists): A list where each sublist contains the elements belonging to a zone.

    Returns:
    element_to_zone (ndarray): An array where each index corresponds to an element, and the value at each index is the zone to which the element belongs.
    '''
    # Calculate the total number of elements by summing the lengths of all sublists in zone_to_elements
    count = sum(len(elements) for elements in zone_to_elements)

    # Initialize an array to store the zone of each element
    element_to_zone = np.zeros([count], dtype=int)

    # Loop over each zone (i) and its corresponding elements
    for i in range(len(zone_to_elements)):
        # Assign the zone index to each element in the sublist
        for j in zone_to_elements[i]:
            element_to_zone[j] = i

    return element_to_zone


def calculateSurfaceVec(face_to_points, point_to_coordinates):
    '''
    Calculate the surface vector (the vector normal to the face with a magnitude equal to the area of the face) of the surface.

    Parameters:
    face_to_points (ndarray): A 2D array where each row contains the indices of the points that form a face.
    point_to_coordinates (ndarray): A 2D array where each row contains the coordinates of a point.

    Returns:
    surfaceVec (ndarray): A 2D array where each row contains the surface vector for a face.
    '''
    # Check if the faces are quadrilateral (having 4 points)
    if face_to_points.shape[1] == 4:
        # Extract the point coordinates of the vertices of the face
        point0 = point_to_coordinates[face_to_points[:, 0]]
        point1 = point_to_coordinates[face_to_points[:, 1]]
        point2 = point_to_coordinates[face_to_points[:, 2]]
        point3 = point_to_coordinates[face_to_points[:, 3]]

        # Calculate the surface vector by summing the cross products of two triangles formed by the face points
        surfaceVec = (np.cross(point1 - point0, point2 - point0) * 0.5) + \
                     (np.cross(point2 - point0, point3 - point0) * 0.5)
    else:
        # If the face is not quadrilateral, print an error message and return None
        print("The method does not support the geometry of the face")
        return None

    return surfaceVec


def constructZoneToShells(zone_to_elements, element_to_faces):
    '''
    Construct a shell map for each zone.

    Parameters:
    zone_to_elements (list of lists): A list where each sublist contains the elements belonging to a zone.
    element_to_faces (list of sets): A list where each index corresponds to an element, and the set at each index contains the faces of that element.

    Returns:
    zone_to_shells (list of sets): A list where each index corresponds to a zone, and the set at each index contains the shell faces of that zone.
    '''
    # Initialize a list to store shell faces for each zone
    zone_to_shells = []
    for i in range(len(zone_to_elements)):
        zone_to_shells.append(set())

    # Loop over each zone (i)
    for i in range(len(zone_to_elements)):
        # Loop over each element in the zone (j)
        for j in zone_to_elements[i]:
            # Use the symmetric difference operator (^) to update the set of shell faces for the zone
            zone_to_shells[i] ^= element_to_faces[j]

    return zone_to_shells


def constructZoneToVolume(zone_to_elements, element_to_volume):
    '''
    Calculate the volume of each zone.

    Parameters:
    zone_to_elements (list of lists): A list where each sublist contains the elements belonging to a zone.
    element_to_volume (ndarray): An array where each index corresponds to an element, and the value at each index is the volume of that element.

    Returns:
    zone_to_volume (ndarray): An array where each index corresponds to a zone, and the value at each index is the total volume of that zone.
    '''
    # Initialize a list to store the volume of each zone
    zone_to_volume = []

    # Loop over each zone (i)
    for i in range(len(zone_to_elements)):
        # Initialize the volume of the zone
        zone_volume = 0

        # Loop over each element in the zone (j) and sum their volumes
        for j in zone_to_elements[i]:
            zone_volume += element_to_volume[j]

        # Append the calculated volume to the list
        zone_to_volume.append(zone_volume)

    # Convert the list to a numpy array and return it
    return np.array(zone_to_volume)


def coordinateToZone(coordinate, element_to_coordinates, element_to_zone):
    '''
    Determine the zone of a given coordinate based on element centers and zone assignments.

    Parameters:
    coordinate (list or ndarray): The coordinates of the point to determine the zone for.
    element_to_coordinates (ndarray): An array where each row contains the coordinates of an element center.
    element_to_zone (ndarray): An array where each index corresponds to an element, and the value at each index is the zone ID of that element.

    Returns:
    zone_ID (int): The zone ID of the closest element to the given coordinate.
    '''
    # Calculate the Euclidean distance between the coordinate and each element center
    d = np.sqrt(np.square(element_to_coordinates[:, 0] - coordinate[0])
                + np.square(element_to_coordinates[:, 1] - coordinate[1])
                + np.square(element_to_coordinates[:, 2] - coordinate[2]))

    # Determine the index of the element with the minimum distance (closest element)
    element_ID = np.argmin(d)

    # Determine the zone ID of the closest element
    zone_ID = element_to_zone[element_ID]

    return zone_ID

#-----------------------------------------------------------------------------------------------------------------------
# Function for compartmentalization
#-----------------------------------------------------------------------------------------------------------------------

def assignZones(data, delta_p=0):
    '''
    Assign zone indices using the basic sort and section method.

    Parameters:
    data (ndarray or list): The data to be assigned zone indices.
    delta_p (float): Optional parameter defining the size of bins or intervals for data segmentation (default is 0).

    Returns:
    inds (ndarray): An array of zone indices assigned to each element in data.
    '''
    # Determine number of bins or intervals based on delta_p or using 'doane' method if delta_p is 0
    if delta_p != 0:
        bins = int(np.ceil((abs((data.max() - data.min()) / delta_p))))
    else:
        bins = 'doane'

    # Compute the edges of the bins using histogram bin edge calculation
    bin_edge = np.histogram_bin_edges(data, bins=bins, range=(data.min(), data.max()))

    # Assign each element in data to a zone based on which bin its value falls into
    inds = np.digitize(data, bin_edge)

    # Adjust indices to ensure they start from 0
    inds[np.where(inds == max(inds))] = max(inds) - 1

    return inds - 1  # Adjust indices to start from 0 and return


def constructZoneToElements(element_to_zone):
    '''
    Construct the connectivity map between zones and their elements.

    Parameters:
    element_to_zone (ndarray): An array where each index corresponds to an element, and the value at each index is the zone ID of that element.

    Returns:
    zone_to_elements (list of sets): A list where each index corresponds to a zone, and the set at each index contains the indices of elements belonging to that zone.
    '''
    zone_to_elements = []

    # Get unique zone IDs from element_to_zone
    uniqueZone = np.unique(element_to_zone)

    # Initialize sets for each zone
    for i in range(len(uniqueZone)):
        zone_to_elements.append(set())

    # Map original zone IDs to a sequential order
    sorted_lst = sorted(uniqueZone)
    order_mapping = {value: index for index, value in enumerate(sorted_lst)}
    element_to_zone = [order_mapping[value] for value in element_to_zone]

    # Populate zone_to_elements with element indices for each zone
    i = 0
    for j in element_to_zone:
        zone_to_elements[j].add(i)
        i += 1

    return zone_to_elements


def constructZoneToNeighbourZone(zone_to_shells, face_to_elements, element_to_zone):
    '''
    Construct the connectivity map between zones and their neighbor zones based on shell faces.

    Parameters:
    zone_to_shells (list of sets): A list where each index corresponds to a zone, and the set at each index contains shell faces of that zone.
    face_to_elements (list of ndarrays): A list where each element is an array representing faces and elements connected to the faces.
    element_to_zone (ndarray): An array where each index corresponds to an element, and the value at each index is the zone ID of that element.

    Returns:
    neighbourZone (list of sets): A list where each index corresponds to a zone, and the set at each index contains the IDs of neighboring zones.
    '''
    neighbourZone = [set() for _ in range(len(zone_to_shells))]  # Initialize a list of sets for neighboring zones

    n_cut = len(face_to_elements[1])  # Number of cut faces (assuming it's the length of face_to_elements[1])

    # Create a set of all shell faces
    set_shell = set()
    for shell in zone_to_shells:
        set_shell.update(shell)
    set_shell = list(set_shell)
    set_shell = set([x for x in set_shell if x < n_cut])  # Filter out shell faces that exceed the number of cut faces

    # Iterate until all shell faces are processed
    while len(set_shell) > 0:
        shell = set_shell.pop()  # Pop a shell face from the set
        elements = [face_to_elements[0][shell], face_to_elements[1][shell]]  # Elements connected to the shell face
        zones = [element_to_zone[elements[0]], element_to_zone[elements[1]]]  # Zones of the connected elements
        neighbourZone[zones[0]] |= {zones[1]}  # Add the neighbor zone to the set of neighbors for zone 0
        neighbourZone[zones[1]] |= {zones[0]}  # Add the neighbor zone to the set of neighbors for zone 1
        intersect = zone_to_shells[zones[0]] & zone_to_shells[zones[1]]  # Intersection of shell faces between zones
        set_shell -= intersect  # Remove intersecting shell faces from set_shell

    return neighbourZone

def splitZone(zone_to_elements, element_to_neighbours):
    '''
    Split non-contiguous zones that fall into the same bin from assignZone into contiguous zones.

    Parameters:
    zone_to_elements (list of sets): A list where each index corresponds to a zone, and the set at each index contains elements belonging to that zone.
    element_to_neighbours (list of sets): A list where each index corresponds to an element, and the set at each index contains neighbouring elements.

    Returns:
    finalZone_to_elements (list of sets): A list where each set contains elements belonging to a contiguous zone.
    '''
    finalZone_to_elements = []  # Initialize a list to store final zone-to-elements mappings

    # Iterate over each non-contiguous zone
    for i in range(len(zone_to_elements)):
        zone_to_elements_i = zone_to_elements[i]  # Get elements in current non-contiguous zone

        newZone_to_elements = []  # Initialize list to store elements of new contiguous zones

        # Iterate until all elements in current non-contiguous zone are assigned to new contiguous zones
        while len(zone_to_elements_i) > 0:
            currentZone = [zone_to_elements_i.pop()]  # Start with a single element

            n = 0
            # Iterate over currentZone to find all connected neighbours
            while n < len(currentZone):
                extendNeighbour = zone_to_elements_i & element_to_neighbours[currentZone[n]]
                currentZone.extend(extendNeighbour)
                zone_to_elements_i -= extendNeighbour
                n += 1

            newZone_to_elements.append(currentZone)  # Append currentZone as a new contiguous zone

        finalZone_to_elements.extend(newZone_to_elements)  # Extend final list with new contiguous zones

    return [set(x) for x in finalZone_to_elements]  # Convert each list of elements to set and return


def overlayZones(zone_to_elements_list):
    '''
    Overlay multiple zone-to-elements mappings into a single map.

    Parameters:
    zone_to_elements_list (list of lists of sets): A list where each element is a list representing zone-to-elements mappings (sets of elements).

    Returns:
    zone_to_elements (list of sets): A list where each set contains elements belonging to a zone in the overlayed map.
    '''
    element_to_zone_list = []

    # Convert each zone-to-elements mapping to element-to-zone mapping
    for i in range(len(zone_to_elements_list)):
        element_to_zone_list.append(list(map(str, constructElementToZone(zone_to_elements_list[i]))))

    # Initialize the first element-to-zone list to overlay others
    element_to_zone_combined = element_to_zone_list[0]

    # Overlay element-to-zone lists
    for i in range(1, len(element_to_zone_list)):
        element_to_zone_combined = [m + n for m, n in zip(element_to_zone_combined, element_to_zone_list[i])]

    # Convert the combined element-to-zone list to integers
    element_to_zone = list(map(int, element_to_zone_combined))

    # Construct zone-to-elements mapping from combined element-to-zone mapping
    zone_to_elements = constructZoneToElements(element_to_zone)

    # Remove empty sets from zone-to-elements mapping
    zone_to_elements = [ele for ele in zone_to_elements if ele]

    return zone_to_elements


def manualDefineZone(fixedZone, zone_to_elements):
    '''
    Define a zone manually by subtracting a fixed set of elements from each zone in zone_to_elements.

    Parameters:
    fixedZone (set): A set of elements that define the fixed zone.
    zone_to_elements (list of sets): A list where each set contains elements belonging to a zone.

    Returns:
    zone_to_elements_new (list of sets): A modified list where the fixed zone is placed at the beginning and each zone's elements are adjusted accordingly.
    '''
    zone_to_elements_new = []

    # Iterate over each zone in zone_to_elements
    for i in range(len(zone_to_elements)):
        # Subtract fixedZone from each zone's elements
        diffSet = zone_to_elements[i] - fixedZone

        # If there are elements left after subtraction, add them to zone_to_elements_new
        if len(diffSet) != 0:
            zone_to_elements_new.append(diffSet)

    # Insert the fixedZone at the beginning of zone_to_elements_new
    zone_to_elements_new.insert(0, fixedZone)

    return zone_to_elements_new


def mergeNeighbourZonesToZone(zoneDict, targetZone, mergedZone):
    '''
    Merge information from mergedZone into targetZone in zoneDict and update neighbor relationships.

    Parameters:
    zoneDict (dict): A dictionary where keys are zone identifiers and values are dictionaries containing zone attributes ('elements', 'shells', 'volume', 'neighbour').
    targetZone (hashable): The zone identifier to merge into.
    mergedZone (hashable): The zone identifier to merge from and then delete.

    Returns:
    zoneDict (dict): Updated zone dictionary after merging and updating neighbor relationships.
    '''
    # Merge elements, shells, and volume from mergedZone into targetZone
    zoneDict[targetZone]['elements'] |= zoneDict[mergedZone]['elements']
    zoneDict[targetZone]['shells'] ^= zoneDict[mergedZone]['shells']
    zoneDict[targetZone]['volume'] += zoneDict[mergedZone]['volume']

    # Update neighbor relationships
    for i in zoneDict[mergedZone]['neighbour'].keys():
        if i in zoneDict[targetZone]['neighbour'].keys():
            zoneDict[targetZone]['neighbour'][i] |= zoneDict[mergedZone]['neighbour'][i]
        elif i != targetZone:
            zoneDict[targetZone]['neighbour'].update({i: zoneDict[mergedZone]['neighbour'][i]})

    # Remove mergedZone from targetZone's neighbor list
    del zoneDict[targetZone]['neighbour'][mergedZone]

    # Update neighbor relationships of neighbors of mergedZone
    for i in zoneDict[mergedZone]['neighbour'].keys():
        if i != targetZone:
            # Update targetZone in the neighbor's neighbor list
            if targetZone in zoneDict[i]['neighbour'].keys():
                zoneDict[i]['neighbour'][targetZone] |= zoneDict[mergedZone]['neighbour'][i]
            else:
                zoneDict[i]['neighbour'].update({targetZone: zoneDict[mergedZone]['neighbour'][i]})
            # Remove mergedZone from neighbor's neighbor list
            zoneDict[i]['neighbour'].pop(mergedZone)

    # Remove mergedZone from zoneDict
    zoneDict.pop(mergedZone)

    return zoneDict


def mergeZone(V_threshold, face_to_area, data_list, zoneDict, reserved_zone=set()):
    '''
    Merge a small volume zone with a zone that shares the longest internal faces and averaged mass.

    Parameters:
    V_threshold (float): Threshold volume for considering zones for merging.
    face_to_area (numpy array): Array where each element represents the area of a face.
    data_list (list of numpy arrays): List of arrays containing data for averaging.
    zoneDict (dict): Dictionary containing zone information with keys as zone identifiers.
    reserved_zone (set, optional): Set of zone identifiers that should not be considered for merging.

    Returns:
    zoneDict (dict): Updated zone dictionary after merging operations.
    '''
    # Append average data to dictionary
    for N in zoneDict:
        data_avg = []
        for data in data_list:
            data_avg.append(np.average(data[list(zoneDict[N]['elements'])]))
        zoneDict[N].update({"data_avg": data_avg})

    # Loop over all the zones
    i = 0
    keys = list(zoneDict.keys())
    while i < len(zoneDict):

        # Sort zones based on volume to prioritize smaller zones first
        if i < len(zoneDict) - 1 and zoneDict[keys[i]]['volume'] > zoneDict[keys[i + 1]]['volume']:
            keys[i], keys[i + 1] = keys[i + 1], keys[i]

        # Check if the volume of the current zone is below the threshold and not in reserved_zone
        if zoneDict[keys[i]]['volume'] < V_threshold and keys[i] not in reserved_zone:
            mergedZone_partition = zoneDict[keys[i]]["partition"]

            # Extract the neighboring zones
            neighbour = list(zoneDict[keys[i]]['neighbour'].keys() - reserved_zone)
            neighbour = [p for p in neighbour if zoneDict[p]["partition"] == mergedZone_partition]
            neighbour_faceArea = []

            # Calculate the total area of shared faces with each neighboring zone
            for j in neighbour:
                intersect = zoneDict[keys[i]]['neighbour'][j]
                area = 0
                for k in intersect:
                    area += face_to_area[k]
                neighbour_faceArea.append(area)

            # Identify the neighboring zone with the maximum shared face area
            max_value = np.max(neighbour_faceArea)
            argm = np.where(neighbour_faceArea == max_value)[0]
            neighbour_value = []

            # If multiple zones have the same maximum face area, choose based on data average differences
            if len(argm) > 1:
                max_neighbour = [neighbour[i] for i in argm]
                for m in max_neighbour:
                    delta = 0
                    for k in range(len(data_list)):
                        delta += abs((zoneDict[keys[i]]['data_avg'][k] - zoneDict[m]['data_avg'][k]) /
                                     zoneDict[keys[i]]['data_avg'][k])
                    neighbour_value.append(delta)
                target_zone = max_neighbour[np.argmax(neighbour_value)]
            else:
                target_zone = neighbour[argm[0]]

            # Average the data averages between the current zone and the target zone
            for k in range(len(data_list)):
                zoneDict[target_zone]['data_avg'][k] += zoneDict[keys[i]]['data_avg'][k]
                zoneDict[target_zone]['data_avg'][k] /= 2

            # Merge the current zone into the target zone
            zoneDict = mergeNeighbourZonesToZone(zoneDict, target_zone, keys[i])
            keys = list(zoneDict.keys())  # Update keys after merging
        else:
            i += 1

    return zoneDict

#-----------------------------------------------------------------------------------------------------------------------
# Post-Processing function
#-----------------------------------------------------------------------------------------------------------------------

def sumZoneData(data, zone_to_elements):
    '''
    Sum the values of 'data' corresponding to each zone defined by 'zone_to_elements'.

    Parameters:
    data (numpy.ndarray): Array of data values associated with each element.
    zone_to_elements (list of lists): List where each element is a list of indices representing elements in a zone.

    Returns:
    numpy.ndarray: Array where each element corresponds to the sum of 'data' values for each zone.
    '''
    zone_data = np.zeros(len(zone_to_elements))  # Initialize array to store summed data for each zone
    i = 0
    for j in zone_to_elements:
        for k in j:
            zone_data[i] += data[k]  # Sum data values for each element in the zone
        i += 1
    return zone_data

def volumeAverageZoneData(data, zone_to_elements, element_to_volume):
    '''
    Calculate the volume-weighted average of 'data' for each zone defined by 'zone_to_elements'.

    Parameters:
    data (numpy.ndarray): Array of data values associated with each element.
    zone_to_elements (list of lists): List where each element is a list of indices representing elements in a zone.
    element_to_volume (numpy.ndarray): Array where each element corresponds to the volume of an element.

    Returns:
    numpy.ndarray: Array where each element represents the volume-weighted average of 'data' values for each zone.
    '''
    zone_data = np.zeros(len(zone_to_elements))  # Initialize array to store average data for each zone
    zone_volume = np.zeros(len(zone_to_elements))  # Initialize array to store total volume of each zone

    data *= element_to_volume  # Weight data by element volumes

    i = 0
    for j in zone_to_elements:
        for k in j:
            zone_data[i] += data[k]  # Sum weighted data values for each element in the zone
            zone_volume[i] += element_to_volume[k]  # Sum volumes of elements in the zone
        i += 1

    zone_data /= zone_volume  # Compute volume-weighted average for each zone

    return zone_data


def constructFaceToZone(face_to_elements, zone_to_elements):
    '''
    Construct a connectivity map between faces and their respective zones based on element-to-zone mapping.

    Parameters:
    face_to_elements (numpy.ndarray): 2D array where each row represents a face and contains indices of elements connected to the face.
    zone_to_elements (list of sets): List where each element is a set containing indices of elements belonging to each zone.

    Returns:
    numpy.ndarray: 2D array where each row corresponds to a face and contains indices of the zone to which the face belongs.
    '''
    element_to_zone = constructElementToZone(zone_to_elements)  # Create element-to-zone mapping

    # Reshape face_to_elements to match element_to_zone indexing
    fte = face_to_elements.reshape(face_to_elements.shape)

    # Map element_to_zone to face_to_elements indices
    etz = element_to_zone[fte]

    # Reshape etz back to match the original shape of face_to_elements
    face_to_zone = etz.reshape((face_to_elements.shape[0], face_to_elements.shape[1]))

    return face_to_zone

def constructInternalFlowNetwork(zone_to_elements, zone_to_shells, volFlowRate, face_to_elements, uniDirection=False):
    '''
    Construct the volumetric flow rate matrix assuming incompressible liquid phase.

    Parameters:
    zone_to_elements (list of sets): List where each element is a set containing indices of elements belonging to each zone.
    zone_to_shells (list of sets): List where each element is a set containing indices of shells (faces) belonging to each zone.
    volFlowRate (numpy.ndarray): Array containing the volumetric flow rates associated with each face.
    face_to_elements (numpy.ndarray): 2D array where each row represents a face and contains indices of elements connected to that face.
    uniDirection (bool, optional): Flag indicating whether to enforce uni-directional flow (default is False).

    Returns:
    numpy.ndarray: Volumetric flow rate matrix Q, where Q[i, j] indicates the flow rate from zone j to zone i.

    '''
    Q = np.zeros([len(zone_to_shells), len(zone_to_shells)])  # Initialize flow rate matrix

    face_to_zones = constructFaceToZone(face_to_elements, zone_to_elements)  # Map faces to their respective zones

    # Loop through each zone
    for i in range(len(zone_to_shells)):
        # Loop through each shell (face) in the current zone
        for j in zone_to_shells[i]:
            if j < len(face_to_elements):
                # Determine if the owner of the face is in zone i
                if face_to_elements[j, 0] in zone_to_elements[i]:
                    owner_flag = True
                else:
                    owner_flag = False

                # Assign flow rate based on owner_flag and volFlowRate direction
                if owner_flag and volFlowRate[j] < 0:  # Flow into zone i
                    Q[face_to_zones[j, 1], i] += -1 * volFlowRate[j]
                elif not owner_flag and volFlowRate[j] >= 0:  # Flow into zone i
                    Q[face_to_zones[j, 0], i] += volFlowRate[j]

    if not uniDirection:
        return Q  # Return the flow rate matrix Q

    else:
        Q = Q - Q.transpose()  # Ensure uni-directional flow
        Q[Q < 0] = 0  # Set negative flows to zero
        return Q  # Return the uni-directional flow rate matrix Q


def balanceMass(Q):
    """
    Balance the mass in the volumetric flow rate matrix (assuming incompressible liquid phase).

    Parameters:
    Q (numpy.ndarray): The volumetric flow rate matrix where Q[i, j] represents the flow rate from zone j to zone i.

    Returns:
    numpy.ndarray: The balanced volumetric flow rate matrix.

    """
    np.fill_diagonal(Q, 0)  # Set diagonal elements of Q to zero

    QIndex = np.where(Q > 0, 1, 0)  # Matrix where Q > 0 is replaced by 1, else 0

    sumRow = np.sum(Q, axis=1)  # Sum of elements in each row of Q
    sumColumn = np.sum(Q, axis=0)  # Sum of elements in each column of Q

    delta = sumRow - sumColumn  # Difference between sum of rows and sum of columns

    etol = 1e-10  # Tolerance for convergence

    while max(abs(delta)) > etol:
        # Find the index of the row/column with the maximum absolute difference
        i = np.argmax(abs(delta))

        # Sum of row i and column i
        sum_rc = (np.sum(Q[i, :]) + np.sum(Q[:, i])) ** 1

        # Calculate the adjustment factor deltai
        deltai = delta[i] / sum_rc

        # Adjust the matrix Q by subtracting and adding delta
        Q[i, :] -= Q[i, :] ** 1 * deltai * QIndex[i, :]
        Q[:, i] += Q[:, i] ** 1 * deltai * QIndex[:, i]

        # Recalculate sum of rows and sum of columns
        sumRow = np.sum(Q, axis=1)
        sumColumn = np.sum(Q, axis=0)

        # Recalculate delta
        delta = sumRow - sumColumn

    # Set diagonal elements to ensure row sums are zero
    for i in range(len(Q)):
        Q[i, i] = -np.sum(Q[i, :])

    return Q