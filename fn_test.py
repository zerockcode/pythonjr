
def make_benefit(peple, ticket_price):
    income = peple * ticket_price
    outcome = 180 + (peple * 0.04)

    result = income - outcome

    return result


ticket = 5.0
people_count = 120
before_benefit = 0
before_ticket = 0

for i in range(0, 50):
    money = make_benefit(people_count, ticket)
    print( ticket, ":" ,  money)
    ticket = round(ticket - 0.1,2)
    people_count =  people_count + 15

    if before_benefit < money:
        before_benefit = money
        before_ticket = ticket +0.1
    else:
        break

print("-------------------------------")

print(before_benefit)
print(before_ticket)




