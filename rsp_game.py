
def play_rsp():

    return 2

count_win = 0
count_lose = 0
count_draw = 0


for x in range(10):
    result = play_rsp()

    if result == 2:
        count_win += 1
    elif result == 1:
        count_lose += 1
