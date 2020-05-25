# -*- coding : utf-8 -*-

def calling (ftn) : #그냥 함수이름의 타입은 function 또는 builtin_fucntion_or_method이다.
    return ftn()
def name_buffer() :
    name_list = input("이름들을 여러개 입력하세요. 공백으로 이름들을 구분하겠습니다. :").split()
    return name_list

def printing(name_list) :
    for name in name_list :
        print("이름은 :%10s" % name)

calling(printing(calling(name_buffer)))
