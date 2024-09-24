# %%Selection sort
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if(lst[j] < lst[min_index]): 
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

list = [3, 4, 5, 1, 7]
selection_sort(list)
print(list)

# %%Bubble sort
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst)-1):
            if(lst[j] > lst[j+1]):
                hold = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = hold
    return lst

lst = [49, 61, 12, 19]
print(bubble_sort(lst))

# %%Sorting Exercise
import math

def cities_distances(clat, clon):
    stores_dict = {}
    dist_dict = {}
    clat = math.radians(clat)
    clon = math.radians(clon)
    file1 = open('stores_location.dat', 'r') # open file
    Lines = file1.readlines()
    # read all lines
    file1.close()
    # close file
    for line in Lines:
    # loop over each line
        storeID, location, latitude, tmp, longitude, tmp = line.split()
        stores_dict.setdefault(storeID, []).append(location)
        stores_dict.setdefault(storeID, []).append(math.radians(float(latitude)))
        stores_dict.setdefault(storeID, []).append(math.radians(-float(longitude)))
    # compute using haversin formula
        
    for key in stores_dict:    
        dlat = clat - stores_dict[key][1]
        dlon = clon - stores_dict[key][2]
        haversin = math.sin(float(dlat)/2)**2 + math.cos(float(latitude))*math.cos(float(clat))*math.sin(float(dlon/2))**2
        distance = 2 * math.atan2(math.sqrt(haversin), math.sqrt(1-haversin))
        r = 6371.0
        total_dist = r * distance

        dist_dict[stores_dict[key][0]] = total_dist
    
    distances = list(dist_dict.values())
    cities = list(dist_dict.keys())

    #selection sort list of distances
    for i in range(len(distances)):
        min_index = i
        for j in range(i+1, len(distances)):
            if(distances[j] < distances[min_index]): 
                min_index = j
        cities[i], cities[min_index] = cities[min_index], cities[i]
        distances[i], distances[min_index] = distances[min_index], distances[i]

    return cities, distances
    
lat = 30.189281
lon = -89.565155
cities_distances(lat,lon)
