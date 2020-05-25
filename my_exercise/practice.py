# -*- coding : utf-8 -*-

import sys
import numpy as np
from scipy import signal as sig

matlab_dict = {} #내가 선언해준 리스트들을 넣을 딕셔너리


'''mode1 : script가 없는 경우'''
def show_variable() : # 실제 콘솔창에 있는 변수 리스트들처럼 만들어보자.
    for i in matlab_dict :
        print("\n")
        print("{} = ({}: {}) {}\n".format(i,matlab_dict[i].shape,'ndarray',matlab_dict[i]))

def make_matrix(str) :
    if ';' not in str : #1차원 행렬이라면
        key = (sys.argv[-1])[0 : sys.argv[-1].find('=')] # 대입 연산자 왼쪽의 str은 모두 변수의 이름이 된다.
        element = (((sys.argv[-1])[((sys.argv[-1]).find('[')+1):]).split(' '))
        element.pop()
        element.remove('')
        #key와 element는 matlab_dict에 저장할 key와 그애 해당하는 element임.

        for i in range(len(element)) :
            element[i] = float(element[i])
        element = np.array(element)

        matlab_dict[key] = element
        print("{} = {}".format(key,element))

    elif ';' in str : #2차원 행렬이라면

        key = (sys.argv[-1])[0:sys.argv[-1].find('=')]
        element = (((sys.argv[-1])[((sys.argv[-1]).find('[') + 1):]).split(';')) # ';'가 있으면 쪼개고

        for i in range(len(element)) :
            element[i] = element[i].split(' ') #또 쪼개고

            while((''  in element[i]) or (']' in element[i])) : # ''랑 ']' 아예 제거

                if '' in element[i] :
                    element[i].remove('')
                elif ']' in element[i] :
                    element[i].remove(']')

            for j in range(len(element[i])) :
                element[i][j] = float(element[i][j])

        element = np.array(element)

        matlab_dict[key] = element
        print("{} = {}".format(key,element))


def add_matrix(str) : # A+B
    tmp = list(str) # 받은 str을 list로 변환. A + B 같이 공백도 허락하려고 함.

    while ' ' in tmp :  # ' ' 아예 제거

        tmp.remove(' ')

    left = ''.join(tmp[0:tmp.index('+')]) # 긴 이름의 변수도 다루고자 한다.
    right = ''.join(tmp[(tmp.index('+')+1):]) # 긴 이름의 변수도 다루고자 한다.

    if ((left) not in matlab_dict) and ((right) not in matlab_dict) :
        print("{}와 {}라는 변수는 없습니다.".format(left,right))
        return
    elif left not in matlab_dict :
        print("{}라는 변수는 없습니다.".format(left))
        return
    elif right not in matlab_dict :
        print("{}라는 변수는 없습니다.".format(right))
        return

    print(np.add(matlab_dict[left],matlab_dict[right]))

    return np.add(matlab_dict[left],matlab_dict[right])

def mul_matrix(str) : # "A * B"
    tmp = list(str) # 받은 str을 list로 변환. A + B 같이 공백도 허락하려고 함.

    while ' ' in tmp :  # ' ' 아예 제거

        tmp.remove(' ')

    left = ''.join(tmp[0:tmp.index('*')]) # 긴 이름의 변수도 다루고자 한다.
    right = ''.join(tmp[(tmp.index('*')+1):]) # 긴 이름의 변수도 다루고자 한다.

    if ((left) not in matlab_dict) and ((right) not in matlab_dict) :
        print("{}와 {}라는 변수는 없습니다.".format(left,right))
        return
    elif left not in matlab_dict :
        print("{}라는 변수는 없습니다.".format(left))
        return
    elif right not in matlab_dict :
        print("{}라는 변수는 없습니다.".format(right))
        return

    print(np.matmul(matlab_dict[left],matlab_dict[right]))

    return np.matmul(matlab_dict[left],matlab_dict[right])

def element_wise_mul_matrix(str) : #"A .* B"
    tmp = list(str)  # 받은 str을 list로 변환. A + B 같이 공백도 허락하려고 함.

    while ' ' in tmp:  # ' ' 아예 제거

        tmp.remove(' ')

    left = ''.join(tmp[0:tmp.index('.')])  # 긴 이름의 변수도 다루고자 한다.
    right = ''.join(tmp[(tmp.index('*') + 1):])  # 긴 이름의 변수도 다루고자 한다.

    if ((left) not in matlab_dict) and ((right) not in matlab_dict):
        print("{}와 {}라는 변수는 없습니다.".format(left, right))
        return
    elif left not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(left))
        return
    elif right not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(right))
        return

    print((matlab_dict[left]* matlab_dict[right]))

    return (matlab_dict[left]* matlab_dict[right])

def cosine(str):
    tmp = list(str)  # 받은 str을 list로 변환. A + B 같이 공백도 허락하려고 함.

    while ' ' in tmp:  # ' ' 아예 제거

        tmp.remove(' ')
    tmp = "".join(tmp) # 공백 전부 제거된 str // cos(A)

    key = tmp[tmp.find('(')+1 : tmp.find(')')] # 긴 이름의 변수 키도 다루고자 한다.

    if key not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(key))
        return

    print(np.cos(matlab_dict[key]))

    return (np.cos(matlab_dict[key]))

def sine(str):
    tmp = list(str)  # 받은 str을 list로 변환. A + B 같이 공백도 허락하려고 함.

    while ' ' in tmp:  # ' ' 아예 제거

        tmp.remove(' ')
    tmp = "".join(tmp)  # 공백 전부 제거된 str // sin(A)

    key = tmp[tmp.find('(') + 1: tmp.find(')')]  # 긴 이름의 변수 키도 다루고자 한다.

    if key not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(key))
        return

    print(np.sin(matlab_dict[key]))

    return (np.sin(matlab_dict[key]))

def exponential(str) :
    tmp = list(str)  # 받은 str을 list로 변환. A + B 같이 공백도 허락하려고 함.

    while ' ' in tmp:  # ' ' 아예 제거

        tmp.remove(' ')
    tmp = "".join(tmp)  # 공백 전부 제거된 str // exp(A)

    key = tmp[tmp.find('(') + 1: tmp.find(')')]  # 긴 이름의 변수 키도 다루고자 한다.

    if key not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(key))
        return

    print(np.exp(matlab_dict[key]))

    return (np.exp(matlab_dict[key]))

def conv(str) :
    tmp = list(str)  # 받은 str을 list로 변환.

    while ' ' in tmp:  # ' ' 아예 제거

        tmp.remove(' ')
    tmp = ''.join(tmp) # 공백을 걸러낸 tmp를 str으로 캐스트

    left = tmp[(tmp.find('(')+1) : tmp.find(',')]  # 긴 이름의 변수도 다루고자 한다.
    right = tmp[(tmp.find(',')+1) : tmp.find(')')] # 긴 이름의 변수도 다루고자 한다.

    if ((left) not in matlab_dict) and ((right) not in matlab_dict):
        print("{}와 {}라는 변수는 없습니다.".format(left, right))
        return
    elif left not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(left))
        return
    elif right not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(right))
        return


    print(np.convolve(matlab_dict[left], matlab_dict[right])) # 컨볼루션 모드는 'full'로! (디폴트 모드임)

    return np.convolve(matlab_dict[left], matlab_dict[right])

def conv2D(str) :
    tmp = list(str)  # 받은 str을 list로 변환.

    while ' ' in tmp:  # ' ' 아예 제거

        tmp.remove(' ')
    tmp = ''.join(tmp)  # 공백을 걸러낸 tmp를 str으로 캐스트

    left = tmp[(tmp.find('(') + 1): tmp.find(',')]  # 긴 이름의 변수도 다루고자 한다.
    right = tmp[(tmp.find(',') + 1): tmp.find(')')]  # 긴 이름의 변수도 다루고자 한다.

    if ((left) not in matlab_dict) and ((right) not in matlab_dict):
        print("{}와 {}라는 변수는 없습니다.".format(left, right))
        return
    elif left not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(left))
        return
    elif right not in matlab_dict:
        print("{}라는 변수는 없습니다.".format(right))
        return

    print(sig.convolve2d(matlab_dict[left], matlab_dict[right]))  # 컨볼루션 모드는 'full'로! (디폴트 모드임)

    return sig.convolve2d(matlab_dict[left], matlab_dict[right])

def substitution(str):
    str = list(str) # 공백 ' ' 을 제거하기위해 mutable 객체인 list로 캐스

    while ' ' in str :  # ' ' 아예 제거

        str.remove(' ')
    str = "".join(str) # 다시 str으로 캐스팅 (모드 선택을 쉽게 하기 위해)

    key = str[0:str.find('<')]
    """mode는 하나씩 선택되게 조건문을 짰다.(switch문이 있으면 좋을텐데...)"""

    if '+' in str : # 아마 이 자리에 if '+' in str 넣어야할듯.. 이런 조건들이 *, 등등 나머지 연산들에 다 적용될거임.
        element = add_matrix(str[(str.find('-'))+1:])
    elif ('*' in str) and ('.*' not in str) :
        element = mul_matrix((str[(str.find('-')) + 1:]))
    elif ('.*' in str)  :
        element = element_wise_mul_matrix(str[(str.find('-')) + 1:])
    elif ('cos(' in str)  :
        element = cosine(str[(str.find('-')) + 1:])
    elif ('sin(' in str)  :
        element = sine(str[(str.find('-')) + 1:])
    elif ('exp(' in str)  :
        element = exponential(str[(str.find('-')) + 1:])
    elif ('conv(' in str)  :
        element = conv(str[(str.find('-')) + 1:])
    elif ('conv2D(' in str)  :
        element = conv2D(str[(str.find('-')) + 1:])

    matlab_dict[key] = element
    print("\n{} = {}".format(key,element))

if(len(sys.argv))<2: #script가 없을때임. 참고로 이떄는 디폴트로 sys.agv[0] = 현재 파일 이름 들어가있음.
                     # 그리고 sys.argv[1]부터 script를 넣을 수 있음. 한편, argument로 script를 안건네주면 len(sys.argv) = 1
    print("\nmatlab calulator를 실행합니다. 이 프로그램에서 다룰 수 있는 기능은 다음과 같습니다.\n")
    print((
        "1) 1차원 혹은 2차원 행렬을 만들고 저장하기\n"
        "2) 행렬들의 element wise 합인 '+'\n"
        "3) 행렬들의 element wise 곱인 '.*'\n"
        "4) 행렬들의 행렬곱셈인 '*'\n"
        "5) 행렬들의 cos(), sin(), exp()\n"
        "6) 1차원 행렬들의 컨벌루션인 'conv(A,B)'\n"
        "7) 2차원 행렬들의 컨벌루션인 'conv2D(A,B)'\n"
        "8) 저장된 변수들의 현황을 모두 볼수 있게 해주는 show_all()\n"
    ))

    while('quit' not in sys.argv) : #sys모듈이 제공하는 argv 버퍼 리스트 안에 quit라는 것이 입력되지 않을때까지 프로그램은 계속 실행된다.
        sys.argv.append(input('>>>'))

        if "=[" in sys.argv[-1] : # 1)
            make_matrix(sys.argv[-1])

        elif "+" in sys.argv[-1] : #2)

            if '<-' in sys.argv[-1]: #9)
                substitution(sys.argv[-1])
            else :
                add_matrix(sys.argv[-1])

        elif ".*" in (sys.argv[-1]):  # 3)

            if '<-' in sys.argv[-1]:  # 9)
                substitution(sys.argv[-1])

            else :
                element_wise_mul_matrix(sys.argv[-1])

        elif ("*" in sys.argv[-1]) and (".*" not in sys.argv[-1]):  # 4)

            if '<-' in sys.argv[-1]:  # 9)
                substitution(sys.argv[-1])

            else :
                mul_matrix(sys.argv[-1])

        elif 'cos(' in sys.argv[-1] :  # 5)cos(A)

            if '<-' in sys.argv[-1]:  # 9)
                substitution(sys.argv[-1])

            else :
                cosine(sys.argv[-1])

        elif 'sin(' in sys.argv[-1] :  # 5)sin(A)

            if '<-' in sys.argv[-1]:  # 9)
                substitution(sys.argv[-1])

            else :
                sine(sys.argv[-1])

        elif 'exp(' in sys.argv[-1] :  # 5)exp(A)

            if '<-' in sys.argv[-1]:  # 9)
                substitution(sys.argv[-1])

            else :
                exponential(sys.argv[-1])

        elif 'conv(' in sys.argv[-1] :  # 6)conv(A,B)

            if '<-' in sys.argv[-1]:  # 9)
                substitution(sys.argv[-1])

            else :
                conv(sys.argv[-1])

        elif 'conv2D(' in sys.argv[-1] :  # 7)conv2D(A,B)

            if '<-' in sys.argv[-1]:  # 9)
                substitution(sys.argv[-1])

            else :
                conv2D(sys.argv[-1])

        elif sys.argv[-1] == 'show_all()' : #8)
            show_variable()

    exit() # program 종료를 의미한다. 참고) loop을 중단 => break, PG를 중단 exit()

for i in sys.argv :
    print("sys.argv의 원소는 : {}".format(i))