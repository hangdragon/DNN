# -*- coding : utf -8 -*-

flag = 24

if flag == 2:
    spell = 's w e e t'.split()
    print(f'spell의 결과 : {spell}')
    spell[3] = 'a'
    print(f'spell의 결과 : {spell}')
    spell[4] = 'r'
    print(f'spell의 결과 : {spell}')
    print(f'spell * 2 의 결과 : {spell*2}')

if flag == 4:
    a = [2,3,4,5,6]
    print(f'a = {a}')
    rev_a = []
    for i in range(5) :
        rev_a.append(a.pop())
    print(f'rev_a = {rev_a}')

if flag == 6 :
    list1 = [2,3,4,1,32]
    print(f'max(list1)의 결과 : {max(list1)}')
    print(f'sum(list1)의 결과 : {sum(list1)}')
    list1.remove(32)
    print(f'list1의 결과 : {list1}')
    list1.reverse()
    print(f'list1의 결과 : {list1}')
    list1.sort()
    print(f'list1의 결과 : {list1}')

if flag == 8 :
    n_list = [10,20,30,50,60]
    result = 1
    for i in n_list :
        result *= i
    print(f'리스트의 원소들 : {n_list}\n리스트의 원소들의 곱 : {result}')

if flag == 10 :
    def minimum(list_n) :
        mini = list_n[0]
        for i in list_n :
            if mini >= i :
                mini = i
        return mini
    n_list = [10, 20, 30, 50, 60]
    print(f'리스트의 원소들 : {n_list}\n리스트의 원소들중 최솟값 : {minimum(n_list)}')

if flag == 12 :
    n = int(input('n을 입력하세요 : '))
    list_n = list(map(int,input(f'{n}개의 수를 입력하세요: ').split()))
    print(f'합: {sum(list_n)}\n평균: {sum(list_n)/n}\n최댓값: {max(list_n)}\n최솟값: {min(list_n)}')

if flag == 14 :
    spell = ['h','a','p','p','y',' ','b','i','r','t','h','d','a','y']
    print(f'spell[1:5] : {spell[1:5]}\nspell[:] : {spell[:]}\nspell[:5] : {spell[:5]}\nspell[6:] : spell[6:] : {spell[:6]}\nspell[:2] + spell[9:] : {spell[:2]+spell[9:]}')

if flag == 16 :
    s = 'Birthday'
    print(f's[:5] : {s[:5]}\ns[5:] : {s[5:]}\ns[1:-1] : {s[1:-1]}\ns[::-1] : {s[::-1]}')
    print(f'\'day\' in s : {"day" in s}\n\'birth\' in s : {"birth" in s}\n\'Birth\' in s : {"Birth" in s}\n\'Birth\' not in s : {"Birth" not in s}')

if flag == 18 :
    def minimum(list_n) :
        mini = list_n[0]
        for i in list_n :
            if mini >= i :
                mini = i
        return mini

    def find_short (s_list) :
        len_list = list(map(len,s_list)) #각 원소인 str의 길이 반환
        minimum_len = minimum(len_list) #str길이의 최솟값 찾음
        minimum_str = list(filter(lambda x : len(x) == minimum_len,s_list)) #최소길이인 스트링들을 모은 리스트
        return minimum(minimum_str) # 사전순 가장 앞에 오는게 값이 작으므로 최소값 함수를 다시 써주면 됨.

    def maximum(list_n):
        maxi = list_n[0]
        for i in list_n:
            if maxi <= i:
                maxi = i
        return maxi

    def find_long (s_list) :
        len_list = list(map(len,s_list)) #각 원소인 str의 길이 반환
        maximum_len = maximum(len_list) #str길이의 최솟값 찾음
        maximum_str = list(filter(lambda x : len(x) == maximum_len,s_list)) #최소길이인 스트링들을 모은 리스트
        return maximum(maximum_str) # 사전순 가장 앞에 오는게 값이 작으므로 최소값 함수를 다시 써주면 됨.

    def modified_find_short (s_list) :
        len_list = list(map(len,s_list)) #각 원소인 str의 길이 반환
        minimum_len = minimum(len_list) #str길이의 최솟값 찾음
        minimum_str = list(filter(lambda x : len(x) == minimum_len,s_list))#최소길이인 스트링들을 모은 리스트
        return sorted(minimum_str,key=len) # 사전순 가장 앞에 오는게 값이 작으므로 최소값 함수를 다시 써주면 됨.

    s_list = ['abc','bcd','bcdefg','abba','cddc','opq']

    print(f'가장 길이가 짧은 문자열 : {find_short(s_list)}') #18-1 해결!

    print(f'가장 길이가 긴 문자욜 : {find_long(s_list)}') #18-2 해결!

    print(f'가장 길이가 짧은 문자열 : {modified_find_short(s_list)}') #18-3 해결!

if flag == 20 :
    def switching(tmp) : # tmp = ['a','a','a','a']
        x = tmp[0] + str(len(tmp)) # x = 'a4'
        return x

    def eliminate_multiplicity(str) :
        if (len(str) == 0)  :
            return str # 공백문자이면 그냥 출력
        elif (len(str) == 1) :
            return str+'1'
        else :
            output = [] #중복되는 애들을 정리하고 여기에 하나하나 push할 예정임. 결과값으로는 스트링으로 캐스트해서 반환할 거임.
            tmp = []
            tmp.append(str[0])
            i = 1
            while(i != len(str)) :
                if (str[i] == str[i-1]) : #str= a , b..
                    tmp.append(str[i])
                    i += 1
                else:

                    output.append(switching(tmp))
                    tmp.clear()
                    tmp.append(str[i])
                    i += 1

            output.append(switching(tmp))
            return ''.join(output)

    src = 'aaaabbb'
    print(f'src = \'{src}\'')
    print(f'output = \'{eliminate_multiplicity(src)}\'')
    src = 'aaaabccccaaaaacccfg'
    print(f'src = \'{src}\'')
    print(f'output = \'{eliminate_multiplicity(src)}\'')
    src = ''
    print(f'src = \'{src}\'')
    print(f'output = \'{eliminate_multiplicity(src)}\'')
    src = 'a'
    print(f'src = \'{src}\'')
    print(f'output = \'{eliminate_multiplicity(src)}\'')

if flag == 22 :
    def printing(list_x):
        tmp = ''
        for i in list_x :
            tmp +=(f'{i:2} ')
        print(tmp)

    import numpy as np

    n = int(input("n을 입력하시오 : "))
    list_buffer =[]
    list_original = np.arange(1,n**2+1).reshape((-1,n))
    for i in range(n) :
        list_buffer.append(list_original[i].tolist())
    for i in range(n) :
        if (i+1) %2 ==0 :
            list_buffer[i] = (list_buffer[i])[::-1]

    for i in list_buffer :
        printing(i)

if flag == 24 :
    list_buffer = []
    for i in range(3,10000) :
        tmp = []
        for j in range(1,i) :
            if i%j ==0 :
                tmp.append(j) # 진약수 리스트
        if sum(tmp) == i:
            list_buffer.append(f'{i}은 완전수입니다 {i}의 약수 : {tmp}, 약수의 합 = {sum(tmp)}')
    list(map(print,list_buffer))




