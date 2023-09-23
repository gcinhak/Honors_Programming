import pyautogui as pag

# 1. 원하는 위치로 이동 후 클릭
# pag.sleep(3) # 3초 대기
# print(pag.position())
#
# pag.sleep(2) # 2초 대기
# pag.click(66, 18, duration=1) # 1초 동안 (64, 17) 좌표로 이동 후 마우스 클릭

# 2. click() == mouseDown() -> mouseUp()
# pag.mouseDown()
# pag.mouseUp()

# 3. 원하는 위치로 이동 후 더블 클릭
# pag.sleep(2) # 2초 대기
# print(pag.position())

# pag.doubleClick(163, 521, duration=0.5)

# 4. doubleClick() == click(clicks=2)
# pag.click(465, 515, clicks=2, interval=0.25, duration=0.5)

# 5. 절대 좌표로 드래그
# pag.sleep(2) # 2초 대기
# print(pag.position())

# pag.moveTo(376, 421)
# pag.dragTo(576, 421, duration=0.25) # 절대 좌표 기준

# 6. dragTo() == mouseDown() -> moveTo() -> mouseUp()
# pag.mouseDown() # 마우스 버튼 누른 상태
# pag.moveTo(367, 28, duration=0.2)
# pag.mouseUp() # 마우스 버튼 뗀 상태

# 7. 상대 좌표로 드래그
# pag.sleep(2) # 2초 대기
# print(pag.position())

# pag.moveTo(376, 421)
# pag.drag(1000, 300, duration=0.5) # 현재 위치 기준으로 x 100 만큼, y 0 만큼 드래그

# 8. drag() -> mouseDown() -> move() -> mouseUp()
# pag.mouseDown() # 마우스 버튼 누른 상태
# pag.move(100, 0, duration=0.2)
# pag.mouseUp() # 마우스 버튼 뗀 상태

# 9. 오른쪽 클릭
# pag.moveTo(470, 500)
# pag.rightClick()

# 10. 휠 클릭
# pag.moveTo(1374, 89)
# pag.middleClick()

# 11. 스크롤
# pag.scroll(800) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤.
# pag.sleep(1)
# pag.scroll(-700)