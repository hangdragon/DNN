# -*- coding : utf-8 -*-

'''메모이제이션이란, 한번 호출한 함수의 값을 메모리 상에 계속 저장하는 것이다.'''

import time

memo_dict = { #1,2번째 항. 즉 , 리프(호출의 제일 마지막 단계의 노드)의 값들만 저장하는 딕셔너
    1 : 1, #피보나치 수열의 1번째 항 = 1
    2 : 1, #피보나치 수열의 2번째 항 = 1
    3 : 2,
    4 : 3,
    5 : 5,
    6 : 8 #메모리에 저장된 메모의 갯수가 많아질 수록, 재귀 함수가 걸리는 시간은 줄어든다..!! 따라서 메모리에 내가 알 수 있는 한 최대한 많이 우겨넣자!
}

def fibo(n) :
    if n in memo_dict : # dictionary에서는 in 연산자의 첫번째 원소는 key이다!
        return memo_dict[n]
    else :
        return fibo(n-1) + fibo(n-2)


start_time = time.time()

print("피보나치 {}번째 항의 값은 : {}".format(30,fibo(30)))
print("피보나치 걸린 시간 : {}".format(time.time() - start_time))