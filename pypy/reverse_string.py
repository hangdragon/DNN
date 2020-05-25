# -*- coding:utf-8 -*-

def ftn ( x, y ,z ):
    return x**2,y**2,z**2

result = ftn(1,2,3) # 함수의 리턴값이 n개 일때, 대입연산자의 왼쪽항이 1개뿐이라면 튜플만 반환한다.

print(result)

another = (ftn(1,2,3))[0]

print(another)