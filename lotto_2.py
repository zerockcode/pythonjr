
from random import randint

arr = [ randint(1,45) for x in range(1000)]


result = [ {"name": x , "count": 0 }
            for x in range(1,46)]

