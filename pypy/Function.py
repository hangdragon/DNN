# -*- coding : utf-8 -*-

a = 10

def ftn(n) :
    global a
    a = n
    print("로컬변수 a는 {}".format(a))

ftn(120)
print("전역변수 a는 {}".format(a))