# -*- coding : utf-8 -*-

"""이터레이터를 알아보자.

이터레이터 -> 1 회 용 리스트들..!!

"""

tmp = enumerate(list(range(5)))

for i,v in tmp : # 이터레이터는 for문에서 반드시 loop variable로 두개의 변수를 줘야하고, for문은 next()의 역할을 해서 루프를 돌떄마다 이터레이터의 포인터값은 하나씩 전진한다.(1번씩 쓰인다)
    print("인덱스 : {} 에 해당하는 원소는 {}".format(i,v))

print()

print("loop문에 의해 다 쓰여진 enumerate 이터레이터를 리스트로 만들어보면 : {}".format(list(tmp))) # for문을 다 돌고나면(next()함수를 길이만큼 다 돌고나면) 이터레이터의 포인터 값은 끝을 넘어간다.

#이터레이터는 이터러블중에서, next()함수에 의해서 원소를 하나하나 꺼낼 수 있는 것들이다. 얘내는 mutable들이 언제나 그렇듯이 동적으로 할당이 되며, 일회용이다.

#참고로, dictionary의 items()함수의 리턴값은 이터레이터가 아니고 dict_items이다.