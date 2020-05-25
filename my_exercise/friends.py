# -*- coding : utf-8 -*-

'''친화수가 절대 될 수 없는 수들 => 소수!! 거듭제곱들!!'''

def filter_prime(num) :
    for i in range(len(num)) :

        if (num[i]%2 != 0) and(num[i] !=1) : # 넘겨준 리스트에서 홀수 원소만 해당된다.
            count = 1

            for j in range(3,num[i],2) :
                if num[i] % j == 0 :
                    count += 1
            if count==1 :
                num[i] = 1

    return (num)

def sum_divisor(num) :
    sum = 1
    for i in range(2, num) :
        if num%i == 0 :
            sum += i
    return sum

tmp = list(enumerate(list(map(sum_divisor,filter_prime(list(range(0,2000)))))))

for i in tmp:
    if (i[1] != 1) and (i[0] != i[1]):
        if i[::-1] in tmp:
            print(f'{i[0]}는 {i[1]}의 친화수')