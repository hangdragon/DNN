# -*- coding : utf-8 -*-

"""
3x3 칸을 만들어서 좌표로 해당 값 입력하는 방

"""

def str_list_input(n=5): # 그냥 n이면 일반변수, n= 3이면 기본 변수(디폴트 매개변수)
    str_list = []
    for i in range(n):
        str_list.append(input("{}번째 값을 입력하세요:".format(i+1)))
    print("\n")

    for i,value in enumerate(str_list) :
        print("{}번째 값은 : {}입니다.".format(i+1,value))

    print("\n")
    print(enumerate(str_list)) #그냥 enumerate 자체로는 걍 이터레이터일뿐이다.
    print(list(enumerate(str_list))) # 이터레이터는 메모리를 아끼기 위한것임. 그값을 해당 객체의 주소를 가리키로 참조함. 한편 제너레이터는 동적 바인딩!

    return list(enumerate(str_list))

x = str_list_input()

print(x)
#list에서 indexingd이나 slicing을 잘못하면 indexerror가 떳는데 함수에서 매개변수가 잘못되면 type에러가 뜬다. 아마 컨테이너에선 indexerror고 함수는 컨테이너가 아니므로 그런듯
