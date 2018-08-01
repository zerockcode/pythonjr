

data = [ ('A', 'D', 24),
         ('B', 'D', 24),
         ('C', 'H', 192),
         ('D', 'H', 160),
         ('E', 'H', 94),]

for item in data:
    gubun = item[1]
    amount = item[2]
    salary = 0
    if gubun == 'D':
        salary = amount * 8 * 7560
    else:
        salary = amount * 7560

    print(item[0], salary)