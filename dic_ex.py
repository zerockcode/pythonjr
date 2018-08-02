

s1 = {"name":"KFC",
        "addr": "종각 4거리" ,
        "price": 5000,
        "next" : None}

s2 = {"name":"Burger King",
        "addr": "종각 4거리 KFC 옆" ,
        "price": 5000,
        "next" : None}

s3 = {"name":"Moms Touch",
        "addr": "종각 지하철 옆" ,
        "price": 6000,
        "next" : None}


s1['next'] = s2
s2['next'] = s3

current = s1

while True:

    if current == None:
        print("다 떨어졌어요..")
        break


    print(current['name'],'에 도착하였습니다.')
    oper = input("계속 드시렵니까? y/n")

    if oper == 'y':
        current = current['next']
    else:
        print("오늘 식사는 여기까지..")
        break