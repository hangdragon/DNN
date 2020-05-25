# -*- coding: utf-8 -*-

ftn = lambda  : 1 # 람다를 쓸 떄 , 매개변수가 없다면 그냥 공백으로 채우면 된다.
#한편, 람다를 쓸때, 대입연산자의 왼쪽으로는 함수가 오는데, 함수의 이름만 써주면 된다. (함수의 매개변수로 함수가 올 때, 함수의 이름만 써주는것과 동일)

zero = lambda : 1

power = lambda x : x**2 -(3*x)
"""map()는 리스트 내포에서 조건문(if문)을 없앤 것과 같다."""

under_3 = lambda x : x<3
""" filter()의 첫번째 매개변수는 함수인데, 그 함수의 리턴값은 항상 0아니면 1이어야하고, 조건에 따라 1이면 해당 리스트의 원소를 통과시키고 조건이 맞지 않으면 통과 시키지 않는다."""
"""filter()는 리스트 내포에서 맨앞에 (만들고자 하는 리스트의 원소의 함수)를 없애고 그냥 조건문만 있는 것과 같다."""
multi = lambda x,y :x*y

print("Zero 함수의 출력값 : {}\n".format(zero())) #매개변수가 있던 없던 항상 함수는 ()를 써줘야한다. 함수를 호출할 때 ()를 안써주게 되면 아마 제너레이터를.. 호출하는 것일 거임

print("lambda 키워드의 리턴값의 타입은 무엇일까? : {}\n".format(type(zero))) # 그냥 함수의 이름의 타입 => function 타입. 그리고 람다 키워드의 리턴값도 function임.

print(ftn())
print(type(ftn()))

print("매개변수가 2개인 람다로 만들어진 함수의 리턴값 : {}\n".format(multi(5,10)))
list_a = list(range(1,6))

output_a = map(power,list_a) # output_a = [i**2 for i in range(1,6)]이랑 똑같
print("map함수의 실행 결과는 아래와 같다.")
print("map(power,list_a) : {}".format(output_a)) #map()의 결과 -> 제너레이터
print("map(power,list_a) : {}\n".format(list(output_a))) #제너레이터를 리스트로 캐스트

print("power의 type : {}".format(type(lambda x : x**2)))

output_b = filter(under_3,list_a)
print("filter함수의 실행 결과는 아래와 같다.")
print("filter(power,list_a) : {}".format(output_b)) #map()의 결과 -> 제너레이터
print("filter(power,list_a) : {}\n".format(list(output_b))) #제너레이터를 리스트로 캐스트
