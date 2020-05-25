# -*- coding : utf-8 -*-

import time

counter = 0

dictionary = {1:1 ,2:2}

def fibo(n) : # n번째 항을 리턴하는 것을 할 예정, n은 n-1 + n-2로 가능!
    global counter  # 함수 스택 안에서 전역변수를 사용하기 위해서는 global (변수이름) 선언 후에 변수를 쓰면 된다!
    counter += 1

    if n<0 :
        print("음수를 입력할 수는 없습니다. 시스템을 종료합니다.")
        return

    elif n==0 :
        return 0
    if n in dictionary :

        return dictionary[n]
    else:
        return fibo(n-1) + fibo(n-2)
tmp = int(input("피보나치 수열의 항의 수는?:"))

start_time = time.time()

print(fibo(tmp))

end_time = time.time()

print("fibo({})을 수행하는 데에 걸린 시간은 :{}".format(tmp,(end_time - start_time)))
print(counter)