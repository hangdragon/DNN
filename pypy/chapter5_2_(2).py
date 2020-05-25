# -*- coding : utf-8 -*-

list_first = list(range(1, 200001))
for a in list_first:
    list1 = []
    for i in list(range(1, a)):
        if a % i == 0:
            list1 = list1 + [i]
    b = sum(list1)
    list2 = []
    for k in list(range(1, b)):
        if b % k == 0:
            list2 = list2 + [k]
    c = sum(list2)