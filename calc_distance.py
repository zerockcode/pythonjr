import math

points =  [
    {"x": 1, "y": 1},
    {"x": 5, "y": 5},
    {"x": 7, "y": 7},
    {"x": 10, "y": 3},]

target = { "x" : 10, "y": 1}

def calc_distance(p1, p2):
    distance = math.sqrt( math.pow( p2['x'] - p1['x'], 2) +   math.pow(p2['y'] - p1['y'], 2) )
    return distance

for point in points:
    result = calc_distance(target, point)
    print(result)
