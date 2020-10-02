# Monty-Hall-Simulation
python實作模擬：[經典統計問題 - Monty Hall Problem](https://www.youtube.com/watch?v=XXcv3RHuROU)


## 使用方式: 主程式 [monty_hall_simulation.py](https://github.com/pcchencode/Monty-Hall-Simulation/blob/master/monty_hall_simulation.py)
1. git clone this repo

2. cd into this workdir

3. 輸入指令:
```
python3 monty_hall_simulation.py {number you want to simulate: n} {switch or not: true or false}
```

### 範例
* 模擬玩 1000 次; 選擇不換
```
python3 monty_hall_simulation.py 1000 false
```
輸出結果
`win rate: 32.97 %`

* 模擬玩 1000 次; 選擇換
```
python3 monty_hall_sumulation.py 1000 true
```
輸出結果
`win rate: 67.32 %`

***
# 擴展至 `n` 門問題: 
## 使用方式:主程式 [monty_hall_extend_sim.py](https://github.com/pcchencode/Monty-Hall-Simulation/blob/master/monty_hall_extend_sim.py)
1. git clone this repo

2. cd into this workdir

3. 輸入指令:
```
python3 monty_hall_extend_sim.py
```
4. 輸出結果
```
10門問題; 玩100次; 「不換」 的勝率
win rate: 11.0 %
==========================
10門問題; 玩100次; 「換」 的勝率
win rate: 92.0 %
==========================
100門問題; 玩100次; 「不換」 的勝率
win rate: 1.0 %
==========================
100門問題; 玩100次; 「換」 的勝率
win rate: 98.0 %
==========================
3門問題; 玩100次; 「不換」 的勝率
win rate: 33.0 %
==========================
3門問題; 玩100次; 「換」 的勝率
win rate: 68.0 %
```
