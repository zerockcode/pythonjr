from random import randint

data = [ randint(1,10) for x in range(10)]

print(data)

min_value = 100
min_idx = 0

for idx, num in enumerate(data):

    if num < min_value:
        min_value = num
        min_idx = idx

print(min_idx, min_value)