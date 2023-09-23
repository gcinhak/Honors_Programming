import pyautogui as pag

# size = pag.size()
# pag.sleep(3) # 3초 대기
# print(size) # [0] width , [1] height


# 절대 좌표로 마우스 이동
# pag.moveTo(1, 1) # 지정한 위치(가로 x, 세로 y)로 마우스를 이동
# pag.moveTo(300, 300, duration = 2) # 5초로 동안 100, 200 위치로 이동
#
# pag.moveTo(100, 100, duration=0.25)
# pag.sleep(0.5)
# pag.moveTo(200, 200, duration=0.25)
# pag.sleep(0.5)
# pag.moveTo(300, 300, duration=0.25)
#
# # 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로부터)
# pag.moveTo(100, 100, duration=0.25)
# print(pag.position()) # Point(x, y)
# pag.move(100, 100, duration=0.25) # 100, 100 기준으로 +100, +100 -> 200, 200
# print(pag.position()) # Point(x, y)
# pag.move(100, 100, duration=0.25) # 200, 200 기준으로 -> 300, 300
# print(pag.position()) # Point(x, y)
#
p = pag.position()
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y