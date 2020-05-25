# -*- coding:utf-8 -*-

import sys
if(len(sys.argv))<2:
    print ("파일 이름을 입력해보자\n")
    exit()

f =open(sys.argv[1],"r")
a = f.readline()
b= f.readline()

list_a = list(a)
list_b = list(b)

print("a는 = {} 이고, len = {}".format(a,len(a)))
print("a는 = {} 이고, len = {}".format(b,len(b)))

print(list_a)
print(list_b)