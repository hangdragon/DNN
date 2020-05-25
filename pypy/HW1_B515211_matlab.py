# -*- coding:utf-8 -*-

"""mxn행렬을 만드는 함수를 만들어보자"""

#str_matrix와 list_matrix 두개를 다루고, 리턴값도 두가지로 하고, A = [ 1 2; 3 4]뭐 이런식으로 하자 / 클래스넷 과제란 참조

def m_by_n_matrix_ftn (m=1,n=1) :

    list_matrix = [] # 뼈대 []를 만들었음
    for i in range(m) :
        list_matrix.append([]) # m개만큼 속뼈대 [] 원소를 넣어줌.

    for i in range(m) :
        print("제 {}행에 대한 원소를 하나씩 넣어주세요.".format(i+1))
        for j in range(n) :
            list_matrix[i].append(float(input())) # list_matrix의 원소들의 값들은 전부 float형태이다.

    #이제 남은건 format을 이용한 str으로 만들, 리턴값은 그것으로 한다.

    str_matrix = ''

    for row in range(m) :
        str_matrix += '[ ' + ' '.join(map(str,list_matrix[row])) + ' ]\n' # str_matrix의 원소들의 값들은 전부 str형태이다.

    select_matrix_type = input('\n{}x{}행렬을 str으로 받고싶다면 : {}\n{}x{}행렬을 list로 받고싶다면 : {}\n'.format(m,n,'str',m,n,'list'))
    # 스트링 형의 행렬로 리턴값을 받을지, 리스트 형의 행렬을 리스트로 받을 지 선택하는 조건문 갈림길 변수

    if select_matrix_type =='str' :
        print()
        print(str_matrix)
        return str_matrix

    elif select_matrix_type == 'list' :
        print()
        print(list_matrix)
        return list_matrix

def m_by_n_matrix_plus(list_matrix1,list_matrix2) : # 위에 선언한 list_matrix와는 다른 local variable이다.
    if

m_by_n_matrix_ftn(3,3)

#m_by_n_matrix_plus()