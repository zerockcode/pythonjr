

# 5000 over 5%
# 5000 under 4.5%
# 1000 over 4%

def calc_interest(money):

    rate = 0.0
    if money > 5000:
        rate = 0.05
    elif money > 1000:
        rate = 0.045
    else:
        rate = 0.04

    return round(money * rate, 3)


# interest_money = calc_interest(4000)
# print(interest_money)

year = int(input("How long ?\n"))
money = int(input("How much?\n"))

for x in range(year):
    print(x)
    interest_money = calc_interest(money)
    money += interest_money

print("------------------")
print(year , " 뒤에 금액은? " , money)


