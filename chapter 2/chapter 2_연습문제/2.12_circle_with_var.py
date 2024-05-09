# 반지름 값 11 radius 변수에 대입
radius = 11

#원의 둘레, 면적 구하기
PI = 3.141592
circumference = 2 * PI * radius
area = PI * radius * radius 
area2 = PI * radius ** 2 

print(area != area2)
# area와 area2 다르다

# 원의 둘레, 면적 출력 
print('원의 반지름 = {}, 원의 둘레 = {}, 원의 면적 = {:.14f}'.format(radius, circumference, area))