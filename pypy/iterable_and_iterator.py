# -*- coding : utf-8 -*-

tmp = enumerate(list(range(1,6)))

for i, value in tmp :

    print("인덱스의 값 : {} , 원소의 값 : {}".format(i,value))

list_a = list(tmp)

print()
print(list_a)

