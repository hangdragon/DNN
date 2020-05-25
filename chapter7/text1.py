# -*- coding : utf -8 -*-

from math import pi
from random import random,uniform,randrange,choice,shuffle,sample
import numpy as np

def gen_ndarray(nd) :
    print(f'전달받은 초기 ndarray값은 {nd}')
    yield
    for i in range(len(nd)) :
        yield nd[i]

tmp = np.array([uniform(1,50) for i in range(50)])

clone = gen_ndarray(tmp)
next(clone)
print(f'리스트뿐만 아니라 제너레이터도 ndarray캐스트가 가능한가?\n list 캐스트 후 해준다.')

buffer = [[] for i in range(10)]
try:
    for i in range(10) :
        for j in range(5) :
            buffer[i].append(next(clone))
    print(np.array(buffer))
    #print(next(clone))
    raise NotImplementedError(
        '그냥 정상작동임에도 불구하고 에러 한번 내봤습니다! 반동노무섀기들아!\n'
    )
except Exception as e :
    print(f'에러의 종류 : {type(e)}\n에러의 값 : {e}')


