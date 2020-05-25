# -*- coding : utf-8 -*-

f =open("tttt.out","w")
for i in range(4+1) :
	f.write("%d\n" % i)

f.close()

f = open("tttt.out","r")
while(1):
	a = f.read()
