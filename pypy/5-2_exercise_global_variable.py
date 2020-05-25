# -*- coding : utf-8 -*-

"""
global var => immutable : global 키워드 반드시 필요!!!!
global var => mutable : global 키워드 필요 없음!!!!
"""
global_int = 0

global_list = [1]

global_dict = {
    1:1,
    2:2
}

def just_reference_for_globals ():
    print("global_int : {}\nglobal_list : {}\nglobal_dict : {}\n".format(global_int, global_list, global_dict))

def modify_for_globals ():
    global global_int
    global_int += 1
    global_list.append(1)
    global_dict[3] = 3

    print("global_int : %d\nglobal_list : {}\nglobal_dict : {}".format(global_list, global_dict) %global_int)

just_reference_for_globals()

modify_for_globals()

tmp = just_reference_for_globals() # 매개변수의 값이 없는데도!! 값을 저장 가능하다.(이때 값은 None) 한편, 이렇게 대입을 하는 곳에 쓰이더라도 함수는 호출 된거다.

print("리턴값이 없는 함수에서 (type(ftn) == None) = {}".format((just_reference_for_globals()==None))) #여기도 마찬가지로 함수가 호춮 된 것이다.