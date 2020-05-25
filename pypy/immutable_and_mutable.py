# -*- coding utf-8 -*-

def switching_immu(a,b) : #비파괴적 and call-by-value
    tmp = a #tmp = 2
    a = b # a = b
    b = tmp # b = 2

def switching_mu(a,b) : #비파괴적 and call-by-value

    tmp = []
    tmp_a = []
    tmp.append(a) #tmp = [2]

    tmp_a.append(b) # a = b
    b = tmp
    a = tmp_a

a = 2
b = 3

list_a = [2]
list_b = [3]

switching_immu(list_a,list_b)
print(a,b,end = '\n')

switching_mu(list_a,list_b)
print(a,b)
