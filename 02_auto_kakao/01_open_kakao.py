import pyautogui

# 마우스 자동화
# 1. 화면크기 출력
width, height = pyautogui.size()
print('width={0}, height={1}'.format(width, height))
# print(size)

# 2. 마우스 현재 위치 출력(카카오톡 아이콘 위치)
# x, y = pyautogui.position()
# print(f'x:{x}, y:{y}')
# x:934, y:1060

# 3.마우스 위치 이동
# 절대위치
pyautogui.moveTo(934, 1060, duration=1)#이동하는데 걸리는 시간 주기 1초

# 4. 카카오톡 아이콘 클릭
pyautogui.click()#왼쪽마우스 클릭

# 4. 카카오톡 로그인

# 로그인 창 이동
# 이메일 주소 마우스 위치 출력
# a, b = pyautogui.position()
# print(f'a:{a}, b:{b}')
# a:1134, b:346

# pw 마우스 위치 출력
# c, d = pyautogui.position()
# print(f'c:{c}, d:{d}')
# c:1049, d:426

# 이메일 이동
pyautogui.moveTo(1134, 346, duration=2)

# 이메일 입력
pyautogui.click()#왼쪽마우스 클릭
pyautogui.typewrite('??', interval=0.1)

# pw 이동
pyautogui.moveTo(1049, 426, duration=1)

# pw 입력
pyautogui.click()#왼쪽마우스 클릭
pyautogui.typewrite('??', interval=0.1)

# 로그인 창 클릭
# 로그인창 위치 입력
# e, f = pyautogui.position()
# print(f'e:{e}, f:{f}')
# e:1076, f:453

# # 로그인창 이동
pyautogui.moveTo(1076, 453, duration=1)
pyautogui.click()#왼쪽마우스 클릭