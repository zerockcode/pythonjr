
def doA(num):

    if num == 10:
        return num

    print("doA" , num)
    
    return num + doA(num + 1)

print(doA(1))
