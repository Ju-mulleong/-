# n값 입력받기
n = int(input('n값을 입력해주세요 : '))
m = int(input('m값을 입력해주세요 : '))

bin_n = bin(n)
bin_m = bin(m)

# n, m 비트 연산 후 출력
result_and = n & m
result_or = n | m 
result_xor = n ^ m

## 비트 연산은 정수형의 피연산자끼리만 가능

print('{} & {} = {}'.format(str(bin_n), str(bin_m), bin(result_and)))
print('{} | {} = {}'.format(str(bin_n), str(bin_m), bin(result_or)))
print('{} ^ {} = {}'.format(str(bin_n), str(bin_m), bin(result_xor)))


