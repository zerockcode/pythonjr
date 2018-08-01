from random import randint

data = [ randint(1,10) for x in range(10)]

print(data)

def calc_min(min, list):
    if len(list) == 0:
        return min

    num = list.pop()

    if num < min:
        min = num

    return calc_min(min,list)

print("--------------------")
print(calc_min(100, data))


# min_value = 100
# min_idx = 0
#
# for idx, num in enumerate(data):
#
#     if num < min_value:
#         min_value = num
#         min_idx = idx
#
# print(min_idx, min_value)