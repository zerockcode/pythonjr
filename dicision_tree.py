

s0 = {"desc": "운명적인 사랑을 믿는다","yes": None, "no": None  }
s1 = {"desc": "탁 트인 곳이 좋다","yes": None, "no": None  }
s5 = {"desc": "무드와 분위기가 중요하다","yes": None, "no": None  }

s0['yes'] = s1
s0['no'] = s5

current = s0

while True:
    if current == None:
        break
    print(current['desc'])
    user_input = input("yes or no")
    current = current[user_input]

