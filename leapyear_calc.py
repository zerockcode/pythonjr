

year = int(input("YEAR"))

if year % 400 == 0:
    print("Leap year")
elif year  % 100 == 0:
    print("Plain Year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Plain Year")




