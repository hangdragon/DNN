# -*- coding:utf-8 -*-

"""프로그래밍을 잘한다는 것은 자료구조와 알고리즘을 통해 함수들을 쭊쭊 만든다는 것..!"""

import time

"""함수의 실행 시간을 한번 재어보자!"""

compare_time = []
counter1 = 0
counter2 = 0
dictionary = {
    1: 1,
    2: 1
}

def fibo(n):
    start_time = time.time()  # 실행 시작 시각 체
    element = []
    #global compare_time <- mutable 객체는 global 키워드를 선언해줄 필요가 없다.

    for i in range(n + 1):

        if i == 0:
            element.append(0)

        elif i == 1 or i == 2:
            element.append(1)

        else:
            element.append(element[i - 2] + element[i - 1])
    compare_time.append((time.time() - start_time))

    return element[n], (time.time() - start_time)  # n번째 피보나치 항 출력크 및 총 실행 시간 측정. 리턴값이 n개일때는 튜플로 반환한다.


def recur_fibo(n):
    global counter1
    counter1 += 1

    if n == 1 or n == 2:  # 반복이 아닌 재귀를 끝내는 코드
        return 1
    return (recur_fibo(n - 2) + recur_fibo(n - 1))  # 재귀를 불러오는 코드 , 그리고 조기리

"""재귀함수의 긴 수행 속도를 해결하기 위한 메모이제이션"""

def memo_recur_fibo(n):
    global counter2
    counter2 += 1

    if n in dictionary:  # dictionary에 n 이라는 key가 존재하면,
        return dictionary[n]  # 재귀를 멈추는 부분을 재귀함수 리턴값이 아닌, 이미 지정된 dictionary로 하면 연산 횟수 줄일 수 있다.

    output =  memo_recur_fibo(n - 1) + memo_recur_fibo(n - 2) #조기리턴! 함수 종료는 리턴이므로 조기리턴을 써주도록 하자
    dictionary[n] = output
    return output


print(
    "제 {}반째 항은 : %d이고, 피보나치 함수의 수행 시간은 %f입니다.\n".format(20) % fibo(20))  # format함수와 print 직접 서식 지정을 둘 다 동시에 사용 가능!!!!!

start_time = time.time()
print("제 {}번째 항은 : %d이고, 피보나치 함수의 수행 시간은 %f입니다.\n".format(20) % (recur_fibo(20), (time.time() - start_time)))
print("한편, 덧셈 연산은 {}번 이루어졌습니다.\n".format(counter1))

start_time = time.time()
print("제 {}번째 항은 : %d이고, 피보나치 함수의 수행 시간은 %f입니다.\n".format(20) % (memo_recur_fibo(20), (time.time() - start_time)))
print("한편, 덧셈 연산은 {}번 이루어졌습니다.".format(counter2))
