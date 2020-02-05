"""
Title: Geo Distance: Lat and Lon Approach
Author: Rodrigo Rangel
Description: * The haversine distance determines the distance from two points on a sphere using:
                 - Latitude (North-South position)
                 - Longitude (Easr-West position)
		     
"""

#-----------------------------------------------------------------------------#
#                               Dependencies                                  #
#-----------------------------------------------------------------------------#

from math import radians, cos, sin, asin, sqrt


#-----------------------------------------------------------------------------#
#                               Haversine                                     #
#-----------------------------------------------------------------------------#

# Haversine Formula (Geo Locations -> Distance)
def haversine_distance(lat1, lon1, lat2, lon2, miles = True):
    """
    description: This function uses the haversine formula to compute the distance
                 between two points in miles/kilometers
                 For mi use r = 3959.87433
                 For km use r = 6372.80000
    lon1,lat1: Inputs should be the latitude and longitude of the initial location
               in decimal
    lon2,lat2: Inputs should be the latitude and longitude of the final location
               in decimal
    """
    # Convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula 
    distance_lon = lon2 - lon1 
    distance_lat = lat2 - lat1 
    a = sin(distance_lat/2)**2 + cos(lat1) * cos(lat2) * sin(distance_lon/2)**2
    c = 2 * asin(sqrt(a)) 
    
    if miles == True:
        r = 3959.87433
    if miles == False:
        r = 6372.80000
    return(c * r)
	
# Dallas - Chicago Distance
D_lat, D_lon = [32.776664,-96.796987]
C_lat, C_lon = [41.881832,-87.623177]

# Haversine Distance (Miles)
print(haversine_distance(D_lat,D_lon,C_lat,C_lon))
# 805.30

# Haversine Distance (Kilometers)
print(haversine_distance(D_lat,D_lon,C_lat,C_lon, miles = False))
# 1296.00


