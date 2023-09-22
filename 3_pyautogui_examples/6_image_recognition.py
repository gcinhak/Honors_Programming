import pyautogui
# file_icon = pyautogui.locateOnScreen("file_icon.png")
# print(file_icon)
# pyautogui.click(file_icon)

# option_icon = pyautogui.locateOnScreen("option_icon.png")
# pyautogui.moveTo(option_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for pos in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(pos)
#     pyautogui.click(pos, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# option_icon = pyautogui.locateOnScreen("option_icon.png")
# pyautogui.moveTo(option_icon)

# 속도 개선
# 1. GrayScale
# option_icon = pyautogui.locateOnScreen("option_icon.png", grayscale=True)
# pyautogui.moveTo(option_icon)

# 2. 범위 지정
# option_icon = pyautogui.locateOnScreen("option_icon.png", region=(1794, 891, 1904-1794, 929-891))
# pyautogui.moveTo(option_icon)

# 3. 정확도 조정
# pip install openve-python
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# notepad_add_icon = pyautogui.locateOnScreen("notepad_add_icon.png")
# if notepad_add_icon:
#     pyautogui.click(notepad_add_icon)
# else:
#     print("발견 실패")

# while notepad_add_icon is None:
#     notepad_add_icon = pyautogui.locateOnScreen("notepad_add_icon.png")
#     print("발견 실패")
# pyautogui.click(notepad_add_icon)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 5 # 5초 대기
# start = time.time() # 시작 시간 설정
# notepad_add_icon = None
# while notepad_add_icon is None:
#     notepad_add_icon = pyautogui.locateOnScreen("notepad_add_icon.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout=5):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def click_target(img_file, timeout=5):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("[Timeout {}s] Target not found ({})."\
              .format(timeout, img_file))
        sys.exit()
#
# pyautogui.click(notepad_add_icon)
#
click_target("notepad_add_icon.png", 3)


