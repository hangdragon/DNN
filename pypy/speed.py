# -*- coding : utf-8 -*-


print("{}문의 {} : {}".format("for", "iterable" , "dictionary"))

dict_a = {"key1" : 12 , "key2" :34}

for i in dict_a:
    print(i,end = ' ')
print("\n")

print("{}문의 {} : {}".format("for", "iterable" , "dictionary.items()"))

dict_a = {"key1" : 12 , "key2" :34}.items()

for i in dict_a:
    print(i,end = ' ')
print("\n")

print("{}문의 {} : {}".format("for", "iterable" , "enumerate()"))

list_a = enumerate([i*i for i in range(5)])

for i in list_a :
    print(i,end = ' ')
print("\n")

print("{}문의 {} : {}".format("for", "iterable" , "list(enumerate())"))

list_a = list(enumerate([i * i for i in range(5)]))

for i in list_a:
    print(i,end=' ')
print("\n")


#for의 iterable로 enumerate()와 list(enumerate())는 완전 똑같고, for 의 반복자로 2개가 올 수 있다. 글고 첫번쨰는 인덱스, 두번쨰는 값!
print("{}문의 {} : {}".format("for", "iterable" , "str"))

str_a = "{}".format("웅애야웅애야 ")

for i in range(len(str_a)) :
    print("{}번째 반복 : {}".format(i+1,str_a[i]), end = "\n")

print("\n")



#for문에서 iterable자리에는 container(list,tuple,dict,set,str) ,range() enumerate, items등이 있다.