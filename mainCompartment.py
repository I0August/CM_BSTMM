"""
--------------------------------------------------------------------------
File Name: mainCompartment.py

Purpose:
This script shows an example of how to use compartmentalization functions to obtain
a compartmental model.

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
                                         Part 1: Data Preparation
------------------------------------------------------------------------------------------------------------------------   
The following codes has been used for data preparation for further analysis
1) constructFaceToElements:
   Combine two face-to-element data (-ref and -neighbour) to create a list of faces to elements i.e. the list store 
   elements that are shared by each face
   input >> [face_to_element_ref, face_to_element_neighbour]
   output >> faces_to_elements: a list store elements that are shared by each face
   Example:
             face ID              element IDs
                 0                  0     5         internal face
                 1                  10    15
                ...                   ...
                1500                   12            boundary face
2) constructElementToFaces:
   Construct the connectivity map between elements and their faces by reconstructing the owners and neighbours data
   input >> [owners, neighbours]
   output >> EFM: a list of element-faces map
   Example:
             element ID              face IDs
                 0           0   1   10   15  132  150
                 1           2   5    8   22  156  183
                ...                     ...
3)  element_to_neighbours:
    Construct the connectivity map between elements and their neigbours
    input >> [intarface_to_elements]
    output >> 
    
3) calculateSurfaceVec:
   Calculate the surface area vector (SV) by using faces and points data
   input >> [faces, points] 
   output >> surface area vector: a list of surface area vector
------------------------------------------------------------------------------------------------------------------------
"""

# Load data
U_water = np.load('resources/CFD/UMean.water.npy')
alpha_water = np.load('resources/CFD/alphaMean.water.npy')
element_to_volume = np.load('resources/CFD/V.npy')
element_to_coordinates = np.load('resources/CFD/C.npy')
point_to_coordinates = np.load('resources/CFD/points.npy')
face_to_points = np.load('resources/CFD/faces.npy')
face_to_element_owner = np.load('resources/CFD/owner.npy')
face_to_element_neighbour = np.load('resources/CFD/neighbour.npy')
face_to_elements = [face_to_element_owner, face_to_element_neighbour]

U_x = U_water[:, 0]
U_y = U_water[:, 1]
U_z = U_water[:, 2]

# Combine two face-to-element data (-ref and -neighbour) to create a list of faces to elements
intarface_to_elements, boundaryface_to_element = constructFaceToElements(face_to_element_owner,
                                                                         face_to_element_neighbour)
# Construct the connectivity map between elements and their faces
element_to_faces = constructElementToFaces(face_to_element_owner, face_to_element_neighbour)

# Construct element conectivity
element_to_neighbours = constructElementToNeighbours(intarface_to_elements)

# Calculate the surface area vector
surfaceVec = calculateSurfaceVec(face_to_points, point_to_coordinates)
surfaceArea = np.sqrt(surfaceVec[:,0] ** 2 + surfaceVec[:,1] ** 2 + surfaceVec[:,2] ** 2)

# Save the values of internal surface vector to different parameter
internalSurfaceVec = surfaceVec[:len(intarface_to_elements), :]
internal_surface_area = surfaceArea[:len(intarface_to_elements)]

"""
------------------------------------------------------------------------------------------------------------------------
                                       Part 2: Compartmentalization
------------------------------------------------------------------------------------------------------------------------
The following functions are used for compartmentalization
1) assignZone: 
   Sort the elements based on N scalar fields --> N arrays of sorted scalar fields. Then,
   section the sorted list based on threshold variables into zones
   Example: Threshold variable (delta_p_i) = 0.1 
    element ID | variables of field i (p_i) | zone
      1823                 0.21                0
      1764                 0.21                0
      1765                 0.22                0
      1453                 0.35                1
      1454                 0.37                1
      1455                 0.38                1
      1201                 0.39                1
      1200                 0.40                1
      ...                  ...                ...       
    --> N arrays of sorted scalar fields with assigned zone ID
2) splitZone: 
   Reform the zone as in step 2 as we may arrive at noncontinuous zones
   Example: If element 1200 and 1201 share a surface but do not share any with element 1453-1455
   element ID | variables of field i (p_i) | zone
      1453                 0.35                1
      1454                 0.37                1
      1455                 0.38                1
      1201                 0.39                1 --Then--> 2
      1200                 0.40                1 --Then--> 2 
   --> N arrays of sorted scalar fields with new assigned zone ID
3)  overlayZone:
    Overlay the maps based on the common zones for N variables
    # It needs to update zone again because the overlay algorithm may yield noncontinuous zone (Using Step 3)
    --> The final map of compartments with new assigned zone ID
4) mergeZone:
   Combine some small zones with the adjacent main zones to reduce the number of zone
   --> N arrays of sorted scalar fields with new assigned zone ID 
------------------------------------------------------------------------------------------------------------------------
"""

# Assign zones
element_to_zone_U_x = assignZones(U_x, 0.5)
element_to_zone_U_y = assignZones(U_y, 0.5)
element_to_zone_U_z = assignZones(U_z, 0.5)

# Manually add zones
element_to_zone_U_x_sign = np.zeros(element_to_coordinates[:, -1].shape)
element_to_zone_U_y_sign = np.zeros(element_to_coordinates[:, -1].shape)
element_to_zone_U_z_sign = np.zeros(element_to_coordinates[:, -1].shape)
element_to_zone_U_x_sign[U_x > 0] = 1
element_to_zone_U_y_sign[U_y > 0] = 1
element_to_zone_U_z_sign[U_z > 0] = 1

element_partition = np.zeros(element_to_coordinates[:, -1].shape)
partition1 = (0.647391 + 2.09776) / 2
partition2 = (2.09776 + 3.5476) / 2
partition3 = (3.5476 + 4.9974) / 2
element_partition[element_to_coordinates[:, -1] > partition1] = 1
element_partition[element_to_coordinates[:, -1] > partition2] = 2
element_partition[element_to_coordinates[:, -1] > partition3] = 3

# Construct zone to elements
zone_to_elements_U_x = constructZoneToElements(element_to_zone_U_x)
zone_to_elements_U_y = constructZoneToElements(element_to_zone_U_y)
zone_to_elements_U_z = constructZoneToElements(element_to_zone_U_z)
zone_to_elements_partition = constructZoneToElements(element_partition)

zone_to_elements_U_x_sign = constructZoneToElements(element_to_zone_U_x_sign)
zone_to_elements_U_y_sign = constructZoneToElements(element_to_zone_U_y_sign)
zone_to_elements_U_z_sign = constructZoneToElements(element_to_zone_U_z_sign)

# Split zones
zone_to_elements_U_x = splitZone(zone_to_elements_U_x, element_to_neighbours)
zone_to_elements_U_y = splitZone(zone_to_elements_U_y, element_to_neighbours)
zone_to_elements_U_z = splitZone(zone_to_elements_U_z, element_to_neighbours)
zone_to_elements_partition = splitZone(zone_to_elements_partition, element_to_neighbours)

zone_to_elements_U_x_sign = splitZone(zone_to_elements_U_x_sign, element_to_neighbours)
zone_to_elements_U_y_sign = splitZone(zone_to_elements_U_y_sign, element_to_neighbours)
zone_to_elements_U_z_sign = splitZone(zone_to_elements_U_z_sign, element_to_neighbours)

# Overlay zones
zone_to_elements = overlayZones([zone_to_elements_U_x, zone_to_elements_U_y, zone_to_elements_U_z])
zone_to_elements_sign = overlayZones([zone_to_elements_U_x_sign, zone_to_elements_U_y_sign, zone_to_elements_U_z_sign])
zone_to_elements = overlayZones([zone_to_elements, zone_to_elements_sign, zone_to_elements_partition])

# Define a zone of the overhead gas
element_newzone1 = np.zeros(element_to_coordinates[:, -1].shape)
element_newzone2 = np.zeros(element_to_coordinates[:, -1].shape)
element_newzone1[alpha_water <= 0.3] = 1
element_newzone2[element_to_coordinates[:, -1] >= 6.1] = 1
element_newzone = element_newzone2 * element_newzone2
zone_to_elements_liquid = constructZoneToElements(element_newzone)
zone_to_elements = manualDefineZone(zone_to_elements_liquid[1], zone_to_elements)

# !!! Update zone again because the overlay algorithm may yield noncontinuous zone
zone_to_elements = splitZone(zone_to_elements, element_to_neighbours)

# Define the over head zone
coordinate = [0.5, 0, 7]
element_to_zone = constructElementToZone(zone_to_elements)
reservedzone = coordinateToZone(coordinate, element_to_coordinates, element_to_zone)
reservedZones = {reservedzone}

# Construct maps of zones to shells, volume, and neighbours,
# which will be further used to generate zone connectivity map (Dictionary)
zone_to_shells = constructZoneToShells(zone_to_elements, element_to_faces)
zone_to_volume = constructZoneToVolume(zone_to_elements, element_to_volume)
zone_to_neighbour = constructZoneToNeighbourZone(zone_to_shells, face_to_elements, element_to_zone)

# Determine zone to partition
zone_to_partition = np.zeros(len(zone_to_elements))
i = 0
for j in zone_to_elements:
    zone_to_partition[i] = element_partition[list(j)[0]]
    i += 1

# Create Dictionary of zone connectivity
zoneDict = {}

# Iterate over each zone index
for i in range(len(zone_to_elements)):
    # Initialize zone information in zoneDict
    zoneDict.update({
        i: {
            'elements': zone_to_elements[i],  # List of elements in the zone
            'partition': zone_to_partition[i],  # Partition information of the zone
            'shells': zone_to_shells[i],  # Set of shell IDs associated with the zone
            'volume': zone_to_volume[i],  # Volume of the zone
            'neighbour': {}  # Dictionary to store neighbour information
        }
    })

    # Iterate over neighbours of zone i
    for j in zone_to_neighbour[i]:
        # Find common shells between zone i and neighbour zone j
        common_shells = zone_to_shells[i].intersection(zone_to_shells[j])

        # Update neighbour information in zoneDict for zone i
        zoneDict[i]['neighbour'].update({
            j: common_shells  # Store common shells as a set
        })

# Sort zoneDict based on the volume of each zone in ascending order
zoneDict = dict(sorted(zoneDict.items(), key=lambda item: item[1]["volume"]))

# Merge zone
V_min = 1e-1
zoneDict = mergeZone(V_min, internal_surface_area, [U_x, U_y, U_z], zoneDict, reservedZones)
zoneDict = dict(sorted(zoneDict.items(), key=lambda item: item[1]["volume"]))

"""
------------------------------------------------------------------------------------------------------------------------
                                Part 3: Export of the compartmental model
------------------------------------------------------------------------------------------------------------------------
"""

# Define free surface area
free_surface = []
i = 0
for key in zoneDict:
    if reservedzone in zoneDict[key]['neighbour']:
        free_surface.append([i, zoneDict[key]['neighbour'][reservedzone]])
    i += 1

# Reorganize data to export
zone_to_elements = []
zone_to_shells = []
zone_to_volume = []
for i in zoneDict:
    zone_to_elements.append(list(zoneDict[i]['elements']))
    zone_to_shells.append(list(zoneDict[i]['shells']))
    zone_to_volume.append(zoneDict[i]['volume'])

# Save data for further use
savePythonObject("resources/CM/zone_to_elements", zone_to_elements)
savePythonObject("resources/CM/zone_to_shells", zone_to_shells)
savePythonObject("resources/CM/free_surface", free_surface)
np.save("resources/CM/zone_to_volume", zone_to_volume)
np.save("resources/CFD/interface_to_elements", intarface_to_elements)
np.save("resources/CFD/internal_surface_area", internal_surface_area)










