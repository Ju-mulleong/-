# 피타고라스의 정리 : c**2 = a**2 + b**2

# 밑변 입력받기
width = int(input('밑변을 입력하세요 : '))

# 높이 입력받기
height = int(input('높이를 입력하세요 : '))

# 빗변 계산, 출력
hypo = (width**2 + height**2)**0.5

print('빗변 : ', hypo)