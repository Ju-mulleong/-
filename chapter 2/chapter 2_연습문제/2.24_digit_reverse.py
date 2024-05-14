# 세 자리 정수 입력받기
n = int(input('세 자리 정수를 입력하세요 : '))

# 입력 받은 정수 역순으로 한 글자에 한 줄씩 출력 (//연산자와 %연산자 사용)
hundred_digit = n // 100
ten_digit = (n // 10 ) % 10
one_digit = n % 10

print(one_digit)
print(ten_digit)
print(hundred_digit)