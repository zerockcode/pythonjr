
def convert (value):
    odd = value  % 2

    if int(value / 2) == 0:
        return "1"

    return str(convert( int(value / 2))) + str(odd)

for x in range(1,30):
    print(convert(x))