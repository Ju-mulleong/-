'''
# 좌표 입력받기
a = int(input('좌표의 실수부를 입력해 주세요 : '))
b = int(input('좌표의 허수부를 입력해 주세요 : '))

# 몇 도 만큼 회전시킬지 입력받기
r = int(input('회전시킬 각도를 입력해주세요(도 단위) : '))

# 각도 r만큼 회전 = a + bi * (cos r + (sin r)i)
# 회전 후 좌표 = c + di
# 파이썬에서 삼각함수 표시?
c = a * cos(r) + (-1)*b*sin(r)
d = b*cos(r) + a*sin(r)

# 좌표 결과값 출력
print('회전 후 좌표는 {}+{}i입니다.'.format(c,d))
'''
# 일단 각도 입력받아서 하는거말고 정해진 값으로 해보자 위에꺼는 math 모듈 써야함.

input_val = complex(input("좌표를 'a+bj' 의 형식으로 입력해주세요 : "))

# 반시계로 90도 회전
# cos90 + (sin90)i = 0+1i(도 단위)
rotate_val90 = 0+1j

# 반시계로 30도 회전
# cos30 + (sin30)i = (3**0.5)/2 + 0.5i (도 단위)
rotate_val30 = (3**0.5)/2 + 0.5j

# 회전 후 좌표 
output_val90 = input_val * rotate_val90
output_val30 = input_val * rotate_val30

# 결과 출력
print('회전하기 전 : {}'.format(input_val)) 
print('90도 회전 한 후 : {}'.format(output_val90))
print('30도 회전 한 후 : {}'.format(output_val30))

## 복소수형 자료형을 출력하면 ()를 포함해서 출력한다.
## rotate_val30 에서 0.5j가 아니라 1/2j, (1/2)j로 하면 결과값이 다르다.
