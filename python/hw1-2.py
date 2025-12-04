################################################
# 以下為導入 brython_robot 進行動態模擬的起始內容
################################################
# 導入 brython_robot.py 並設為 robot
import brython_robot as robot
# 導入 Brython browser 模組中的 timer
# 以便讓 AnimatedRobot 可以正常運作
from browser import timer

# 初始化世界與機器人
# 利用 robot 物件中的 World 方法
# 建立一個 10x10 的模擬世界

x=int(input('輸入X'))
y=int(input('輸入Y'))
w = robot.World(x, y)
# 利用 robot 物件的 AnimatedRobot 方法
# 針對 w 進行動態模擬, 且讓機器人位於 (1, 1)
r = robot.AnimatedRobot(w, 1, 1)
################################################
# 範例 1
# 基本變數與數值操作
################################################
# r 為透過上列程式所建立的動態模擬機器人物件
steps = x-1
xz = x-1
yz = int(y/2)
ys=y/2

def t_ro():
  r.move(steps)
  r.turn_left()
  r.move(1)
  r.turn_left()
def t_rt():
  r.move(steps)
  r.turn_left()
  r.turn_left()
  r.turn_left()
  r.move(1)
  r.turn_left()
  r.turn_left()
  r.turn_left()


r.turn_left()
# 讓機器人往前移動 steps 步數
for i in range(yz):
  t_rt()
  t_ro()


print(ys,yz)
if int(ys) != ys:
  r.move(steps)
else:
  pass
