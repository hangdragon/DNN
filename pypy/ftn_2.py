# -*- coding:utf-8 -*-

def printing (*values,n = 3): # *쓰면 가변 매개변수, 초기값을 지정해주면(n= 3) 기본 매개변
    for i in range(n):
        for value in values :
            print(value , end = ' ')
        print("\n")

printing("웅이" , "헤헤",[1,2,3,4],n =5) # 함수를 호출할때, 키워드 매개변수

#기본 매개변수와 키워드 매개변수는 짝꿍이다! 기본 매개변수를 지정해준 다음, 함수 호출시에 키워드 매개변수를 작성해주자!