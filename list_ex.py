from random import randint

#data = list(range(0, 10))
#data = list(range(0, 100, 2))

#data = [10] * 10

data = [ ("사용자"+ str(x),randint(1,100)) for x in range(10)]

print(data)
print("---------------------")

for user, grade in data:
    print(user ,  grade)


