import math

def great_circle_distance(radius, lat1, lon1, lat2, lon2):

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    distance = radius * math.acos(math.sin(lat1_rad) * math.sin(lat2_rad) + 

                                  math.cos(lat1_rad) * math.cos(lat2_rad) * 

                                  math.cos(lon2_rad - lon1_rad))

    return round(distance, 2)

radius = 6371  
start_lat = 52
start_lon = 21
end_lat = 41
end_lon = 12

distance = great_circle_distance(radius, start_lat, start_lon, end_lat, end_lon)
print("Great Circle Distance:", distance, "km") 
