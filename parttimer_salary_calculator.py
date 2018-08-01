
oper = input("D or H \n")
if oper == 'D':
    print("날짜로 계산합니다.")
    day = int(input("몇 일 근무했습니까?"))
    salary = (day * 8) * 7560
    print(salary)
elif oper == 'H':
    print("시간으로 계산합니다.")
    hour = int(input("몇 시간 근무했습니까?"))
    salary = hour * 7560
    print(salary)
    