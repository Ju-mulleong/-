# 세 자리 정수 입력받기
n = int(input('세 자리 정수를 입력하세요 : '))

# 각 자릿수 출력하기
'''
hundred_digit = n // 100
ten_digit = (n - hundred_digit*100) // 10
one_digit = (n - hundred_digit*100 - ten_digit*10) // 1
'''

# 좀 더 간단하게? % 사용?
hundred_digit = n // 100
ten_digit = (n // 10 ) % 10
one_digit = n % 10

print('백의 자리 : {}'.format(hundred_digit))
print('십의 자리 : {}'.format(ten_digit))
print('일의 자리 : {}'.format(one_digit))