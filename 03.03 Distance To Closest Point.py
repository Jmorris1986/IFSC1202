def closest_distance(a, b, c):

    distance_ab = abs(a - b)

    distance_ac = abs(a - c)
    return min(distance_ab, distance_ac)

a = 10
b = 35
c = 30

print("the closest distance from a is:", closest_distance(a, b, c))