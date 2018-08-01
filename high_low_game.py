import math

def make_mid(v1, v2):
    return math.floor((v1 + v2)/2)


min = 1
max = 100

while True:
    mid = make_mid(min, max)
    print(mid )
    oper = input("H  L  C ")
    if oper == 'H':
        min = mid
    elif oper == 'L':
        max = mid
    else:
        break






