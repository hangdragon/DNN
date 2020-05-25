# -*- coding : utf-8 -*-

def rev(list_x) :
    for i in list_x[::-1] :
        yield i

rev_iterator = rev(list(range(1,20)))

print(rev_iterator)

print(list(rev_iterator))