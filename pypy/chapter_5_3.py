# -*- coding : utf-8 -*-
"""모든 함수에서 함수의 이름만 있는 것은 값도있고 type도 있다."""

import time

"""map()는 리스트 내포에서 조건문(if문)을 없앤 것과 같다."""

"""filter()는 리스트 내포에서 맨앞에 (만들고자 하는 리스트의 원소의 함수)를 없애고 그냥 조건문만 있는 것과 같다."""

def ftn() :
    return 1, #괄호가 있거나 괄호가 없는 데이터 뒤에 쉼표 하나만 붙이면 tuple이다.
# 한편, 대입연산자에서 좌항을 제외한 , 다른 것들에서 쉼표로 이어진 데이터들은 모두 괄호가 없는 튜플이다!!!!

def power(item) :
    return item**2
"""map()는 리스트 내포에서 조건문(if문)을 없앤 것과 같다."""

def under_3(item) :
    return item<3 # True or False를 반환하는 함수 -> filter()의 매개변수로 쓰임
""" filter()의 첫번째 매개변수는 함수인데, 그 함수의 리턴값은 항상 0아니면 1이어야하고, 조건에 따라 1이면 해당 리스트의 원소를 통과시키고 조건이 맞지 않으면 통과 시키지 않는다."""
"""filter()는 리스트 내포에서 맨앞에 (만들고자 하는 리스트의 원소의 함수)를 없애고 그냥 조건문만 있는 것과 같다."""

#print(type(ftn()))

list_a = list(range(1,6))
print("\n내장,외장,멤버함수 그리고 사용자 지정 함수에 대하여 각각의 타입을 조사해보겠다!\n")

print("사용자 지정 함수(즉, def를 이용하여 내가 만든 함수)의 타입은?(즉, 함수 이름의 타입은?) : {}".format(type(ftn)))
print("사용자 지정 함수(즉, def를 이용하여 내가 만든 함수)의 타입은?(즉, 함수 이름의 타입은?) : {}".format(type(power)))
print("사용자 지정 함수(즉, def를 이용하여 내가 만든 함수)의 타입은?(즉, 함수 이름의 타입은?) : {}\n".format(type(under_3)))

print("내장 함수의 타입? : {}".format(type(next)))
print("외장 함수의 타입? : {}".format(type(time.time)))
print("클래스의 멤버함수의 타입? : {}\n".format(type(list_a.append)))

#내장 ,외장, 멤버함수의 타입은 builtin_function_or_method이고, 사용자 지정 함수(def or lambda)의 타입은 function이다.

print("\n내장,외장,멤버함수 그리고 사용자 지정 함수에 대하여 각각의 을 조사해보겠다!\n")

print("사용자 지정 함수(즉, def를 이용하여 내가 만든 함수)의 값은?(즉, 함수 이름의 값은?) : {}".format(ftn))
print("사용자 지정 함수(즉, def를 이용하여 내가 만든 함수)의 값은?(즉, 함수 이름의 값은?) : {}".format(power))
print("사용자 지정 함수(즉, def를 이용하여 내가 만든 함수)의 값은?(즉, 함수 이름의 값은?) : {}\n".format(under_3))

print("내장 함수의 값? : {}".format(next))
print("외장 함수의 값? : {}".format(time.time))
print("클래스의 멤버함수의 값? : {}\n".format(list_a.append))

output_a = map(power,list_a) # output_a = [i**2 for i in range(1,6)]이랑 똑같
print("map함수의 실행 결과는 아래와 같다.")
print("map(power,list_a) : {}".format(output_a)) #map()의 결과 -> 제너레이터
print("map(power,list_a) : {}\n".format(list(output_a))) #제너레이터를 리스트로 캐스트

output_b = filter(under_3,list_a)
print("filter함수의 실행 결과는 아래와 같다.")
print("filter(power,list_a) : {}".format(output_b)) #map()의 결과 -> 제너레이터
print("filter(power,list_a) : {}\n".format(list(output_b))) #제너레이터를 리스트로 캐스트
