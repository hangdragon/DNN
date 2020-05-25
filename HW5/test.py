# -*- coding : utf- 8 -*-

def myfunc(x,y,z) :
    print(x,y,z)

tuple_vec = 1,0,1
dict_vec ={
    'x' :2,
    'y' : 3,
    'z' : 4
}

myfunc(*tuple_vec) # *tuple_vec로 아규먼트를 준다는 것은 내가 튜플을 언패킹하여 각각 x,y,z로 하나하나씩 넘겨주는 것을 의미한다.
myfunc(dict_vec)