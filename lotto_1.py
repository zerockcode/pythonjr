
#Step1 - 1000개의 리스트
# 내용물은 1부터 45까지의 숫자 - arr
from random import randint

arr = [ randint(1,45) for x in range(1000)]

#print(arr)

#Step2 -  어떤 숫자가 많이 나왔는지 기록

record = [0] * 45

#print(record)

for num in arr:
    #print(num)
    before = record[num -1]
    #print("BEFORE: " , before)
    record[num -1] = before + 1

for idx, count in enumerate(record):
    print(idx +1, "  COUNT: ", count)

#Step3 - 숫자들 중에서 가장 많이 나온 숫자 알아내기
max = 0
max_idx = 0

for idx, count in  enumerate(record):

    if count > max:
        max = count
        max_idx = idx

print("MAX NUM: " + (max_idx)+1)
print("MAX: " + max)