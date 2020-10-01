import sys, os
import random

# 玩一次 monty-hall 遊戲
def monty_hall_game(switch):
    doors = [1,2,3]
    prize = random.choice(doors)
    sheep = doors.copy(); sheep.remove(prize)
    choice = random.randint(1,3)
    if prize==choice:
        show = random.choice(sheep) # 一開始就挑到中獎的, show就從剩下的隨機挑
    else:
        # 一開始選到羊, show從移除choice prize挑剩下的
        show = doors.copy()
        show.remove(choice); show.remove(prize)
        show = show[0]

    # 決定 final choice
    if switch=='true':
        # 如果選擇換，則最後的選擇一定是choice, show剩下的
        remain = doors.copy(); remain.remove(choice); remain.remove(show)
        final_choice = remain[0]
    elif switch=='false':
        final_choice = choice

    # 如果final choice 選中prize就是 win; 反之就是 lose
    if final_choice==prize:
        return 'win'
    else:
        return 'lose'

def simulation(switch, n=100):
    win_num = 0
    for i in range(0, n):
        if monty_hall_game(switch) == 'win':
            win_num += 1
    print('win rate:', round(win_num/n*100, 2), '%')


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        print("please key in the number you want to simulate")
        os._exit(0)

    try:
        switch = sys.argv[2]
    except:
        switch = 'false'

    simulation(n=n, switch=switch)



