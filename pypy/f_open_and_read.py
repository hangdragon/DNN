# -*- coding:utf-8 -*-

class Hello:
    num = 10
    def __init__(self,number):
        self.num = number
    def inc(self):
        self.num =self.num +1
    def number(self):
        return(self.num)
    def pri(self):
        print(self.num)

a = Hello(100)

a.pri()
a.inc()
a.pri()
a.inc()
a.pri()

with a.pri() as p:

p()