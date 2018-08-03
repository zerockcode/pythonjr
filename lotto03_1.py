
#step1
from random import randint

from random import shuffle

balls = list(range(1,46))
shuffle(balls)
print(balls[0:6])


# balls = list(range(1, 46))
#
# print(balls)
#
# result = []
#
# for x in range(6):
#     idx = randint(0,len(balls) -1)
#     result.append(balls.pop(idx))
#     print(balls)
#     print("----------------------")
#
# print(result)


