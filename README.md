# Monty-Hall-Simulation
python實作模擬：[經典統計問題 - Monty Hall Problem](https://www.youtube.com/watch?v=XXcv3RHuROU)


## 使用方式
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
