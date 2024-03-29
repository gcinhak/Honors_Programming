import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 위치 + 크기
# pyautogui.click(fw.left + 70, fw.top + 20)

for w in pyautogui.getAllWindows():
    print(w) # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("계산기")[0]
print(w)

if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)
pyautogui.sleep(2)

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화
pyautogui.sleep(2)

if w.isMinimized == False : # 현재 최소화가 되지 않았다면
    w.minimize() # 최소화
pyautogui.sleep(2)

w.restore() # 화면 원복
w.close() # 윈도우 닫기