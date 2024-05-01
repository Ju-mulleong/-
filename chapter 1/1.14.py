#n 팩토리얼은 n*(n-1)*(n-2)*...*2*1 로 정의한다. 이 정의를 바탕으로 다음 값을 구하라

#(1) 3!

n = int(input('n을 입력해 주세요.'))
i = n
sum = n
while i > 1:
    i -= 1
    sum = sum*i

print('{}!의 값은 {}입니다.'.format(n,sum))

