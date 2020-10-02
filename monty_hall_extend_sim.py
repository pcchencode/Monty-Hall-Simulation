import sys, os
import random

# 定義玩一次 monty-hall game, 擴展至 n_d 個門
def monty_hall_game(n_d, switch):
    # doors = [1,2,3]
    doors = []
    for i in range(1, n_d+1):
        doors.append(i)

    prize = random.choice(doors)
    sheep = doors.copy(); sheep.remove(prize)
    choice = random.randint(1,n_d)

    # 主持人決定要開出的門: show
    if prize==choice:
        show = random.sample(sheep, n_d-2) # 一開始就挑到中獎的, show就從剩下的sheep隨機挑 (n_d-2) 個
    else:
        # 一開始選到羊, show就從移除 choice & prize 之中挑剩下的
        show = doors.copy()
        show.remove(choice); show.remove(prize)
        # show = show[0]

    # 決定玩家最後的選擇: final choice
    if switch=='true':
        # 如果選擇換，則最後的選擇一定是 choice & show 之中挑剩下的
        remain = doors.copy(); remain.remove(choice)
        for item in show:
            remain.remove(item)
        final_choice = remain[0]
    elif switch=='false':
        # 如果選擇不換，最後選擇跟原本的不變
        final_choice = choice

    # 如果 final choice 選中 prize就是 win; 反之就是 lose
    if final_choice==prize:
        return 'win'
    else:
        return 'lose'

def simulation(n_d, n, switch):
    win_num = 0
    for i in range(0, n):
        if monty_hall_game(n_d, switch) == 'win':
            win_num += 1
    print('win rate:', round(win_num/n*100, 2), '%')

print("10門問題; 玩100次; 「不換」 的勝率")
simulation(n_d=10, n=100, switch='false')
print("==========================")
print("10門問題; 玩100次; 「換」 的勝率")
simulation(n_d=10, n=100, switch='true')
print("==========================")
print("100門問題; 玩100次; 「不換」 的勝率")
simulation(n_d=100, n=100, switch='false')
print("==========================")
print("100門問題; 玩100次; 「換」 的勝率")
simulation(n_d=100, n=100, switch='true')
print("==========================")
print("3門問題; 玩100次; 「不換」 的勝率")
simulation(n_d=3, n=100, switch='false')
print("==========================")
print("3門問題; 玩100次; 「換」 的勝率")
simulation(n_d=3, n=100, switch='true')



