# -*- coding:utf-8 -*-

def normal_funda(n,a=1,b=2,c=3,d=4) :
    for i in range(n) :
        print("{}번 반복합니다".format(n))
        print("a : {} , b : {} , c : {}, d : {}".format(a,b,c,d))
    print()

def funda_vari(a= 1, b=2 , c=3 , *values) :
    print("기본 매개변수는 => a : {} , b : {} , c : {}".format(a,b,c,))
    for value in values :
        print("가변 매개변수는 => {}".format(value))
    print("Tuple이 되어버린 {}의 값은 : {}".format("values",values))
    print()

def vari_funda(*values,a= 1, b=2 , c=3) :
    print("기본 매개변수는 => a : {} , b : {} , c : {}".format(a,b,c,))
    for value in values :
        print("가변 매개변수는 => {}".format(value))
    print()

def normal_vari_funda(n,*values, a= 1, b=2, c=3) :
    print("a : {} , b : {} , c : {}".format(a, b, c))
    print("{}번 반복합니다".format(n))
    for i in range(n) :
        for value in values:
            print("가변 매개변수는 => {}".format(value))
    print()

normal_funda(2,100,200,d = -1424, c =21029) # 이미 a= 100, b = 200, c= 300들어갔음. 여기서 새로 아규먼트로 a= , b= , c= 절대 못쓴다! => 파이썬 인터프리터가 혼란스러워! => 키워드와 기본 매개변수들 끼리의 규칙!

# 일반+기본 => 키워드와 기본 끼리의 규칙! 아규먼트 전달 시, 파이썬에 혼란을 주게 하지 말자.

funda_vari(10,20,30,"이제부터", "가변변수이다") # 얘도 마찬가지로 (10,a=100) , (10,10,b=100) 등등 전부 오류임. => 키워드와 기본 매개변수들끼리의 규칙을 지키자!

#기본 + 가변 => 기본 매개변수들 n개가 다 입력될때만 비로소 가변을 입력할 수 있다.


vari_funda(10,20,30) # 가변과 기본들 사이에서는 '키워드 매개변수'가 꼭 필요하다! 키워드 매개변수를 지정해 주지 않는다면 기본은 영원히 디폴트 값이고 건네준 아규먼트들은 전부 다 가변들의 차지!

#가변 + 기본 => '키워드 매개변수'를 꼭 해주자!

normal_vari_funda(2,200,300,400,b=300)