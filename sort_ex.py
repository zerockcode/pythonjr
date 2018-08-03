import math

data = [1,5,3,2,15,75,323,63,2,90]

def check(num):
    print("NUM ", num)
    return math.fabs(num - 15)

data.sort(key= check)

print(data)