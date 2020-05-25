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

def make_matrix(key,token) : # 미리 정제된 key값과 토큰을 넘겨받는 함수. 토큰에서 행렬 안에 넣을 숫자들을 탐색하고 그것들로 초기화.
    if ';' not in token : #1차원 행렬이라면
        #key = (str)[0 : str.find('=')] # 대입 연산자 왼쪽의 str은 모두 변수의 이름이 된다.
        element = (((token)[(token.find('[')+1):]).split(' '))

        element.pop()
        element.remove('')
        #key와 element는 matlab_dict에 저장할 key와 그애 해당하는 element임.

        for i in range(len(element)) :
            element[i] = float(element[i])
        element = np.array(element)

        matlab_dict[key] = element
        print("{} = {}".format(key,element))

    elif ';' in token : #2차원 행렬이라면

        #key = (str)[0:str.find('=')]
        element = (((token)[(token.find('[') + 1):]).split(';')) # ';'가 있으면 쪼개고

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

    key = str[0:str.find('=')]
    """mode는 하나씩 선택되게 조건문을 짰다.(switch문이 있으면 좋을텐데...)"""

    if '+' in str : # 아마 이 자리에 if '+' in str 넣어야할듯.. 이런 조건들이 *, 등등 나머지 연산들에 다 적용될거임.
        element = add_matrix(str[(str.find('='))+1:])
    elif ('*' in str) and ('.*' not in str) :
        element = mul_matrix((str[(str.find('=')) + 1:]))
    elif ('.*' in str)  :
        element = element_wise_mul_matrix(str[(str.find('=')) + 1:])
    elif ('cos(' in str)  :
        element = cosine(str[(str.find('=')) + 1:])
    elif ('sin(' in str)  :
        element = sine(str[(str.find('=')) + 1:])
    elif ('exp(' in str)  :
        element = exponential(str[(str.find('=')) + 1:])
    elif ('conv(' in str)  :
        element = conv(str[(str.find('=')) + 1:])
    elif ('conv2D(' in str)  :
        element = conv2D(str[(str.find('=')) + 1:])

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

        token = (sys.argv[-1])  # sys.argv 스택의 맨 마지막 원소인 sys.argv[-1] 원소는 str 타압인데, 그것을 list로 캐스트 해줬음. 그 이유는 아래 코드에서 볼 수 있듯이 공백을 제거해주시 위해서!

        if '[' in token :
            init_buffer = list(token)[0:list(token).index('[')+1] # [의 앞에까지 ' ' 공백을 지우기 위함임. ex) A =  [ 1 2 3 4 ] 그리고 이 값은 key임.
            while ' ' in init_buffer:  # ' ' 아예 제거

                init_buffer.remove(' ')
            key = init_buffer.copy() # deep copy
            key.pop() ; key.pop() # =[ 두개 제거
            key = "".join(key) # 변수 딕셔너리의 키로 사용
            init_buffer = "".join(init_buffer)  # 다시 str으로 캐스팅, 글고 init_buffer는 행렬 초기화를 위한 조건문을 위해 사용

            if "=[" in init_buffer : # 1)
                make_matrix(key,token)

        elif "+" in token : #2)

            if '=' in token: #9)
                substitution(token)
            else :
                add_matrix(token)

        elif ".*" in token:  # 3)

            if '=' in token:  # 9)
                substitution(token)

            else :
                element_wise_mul_matrix(token)

        elif ("*" in token) and (".*" not in token):  # 4)

            if '=' in token:  # 9)
                substitution(token)

            else :
                mul_matrix(token)

        elif 'cos(' in token :  # 5)cos(A)

            if '=' in token:  # 9)
                substitution(token)

            else :
                cosine(token)

        elif 'sin(' in token :  # 5)sin(A)

            if '=' in token:  # 9)
                substitution(token)

            else :
                sine(token)

        elif 'exp(' in token :  # 5)exp(A)

            if '=' in token:  # 9)
                substitution(token)

            else :
                exponential(token)

        elif 'conv(' in token :  # 6)conv(A,B)

            if '=' in token:  # 9)
                substitution(token)

            else :
                conv(token)

        elif 'conv2D(' in token :  # 7)conv2D(A,B)

            if '=' in token:  # 9)
                substitution(token)

            else :
                conv2D(token)

        elif token == 'show_all()' : #8)
            show_variable()

    exit() # program 종료를 의미한다. 참고) loop을 중단 => break, PG를 중단 exit()

#아래는 아규먼트로 스크립트 파일이 올때이다.

else : # argument를 script로 전달 받을 때,
    f = open(sys.argv[1],'r') # read는 한번 읽으면 다음으로 넘어간다(이터레이터랑 비슷)

    for i in (f.readlines()) : # 파일 전체의 str을 한라인씩 리스트에 차곡차곡 저장. 그리고 리턴값은 리스트.
        #prompt = input()
        exec(i) # str을 실행시켜주는 험수.