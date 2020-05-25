# -*- coding : utf-8 -*-

flag = 27

if flag == 1 :
    def my_greet():
        print("환영합니다.")
    my_greet()
    my_greet()

if flag == 3:
    def max2(m,n):
        if m>=n :
            return m
        return n # 조기리턴

    def min2(m,n):
        if m>=n :
            return n
        return m
    print(f'100과 200중 큰 수는 : {max2(100,200)}\n'+f'100과 200중 큰 수는 : {min2(100,200)}')

if flag == 5:
    def inch2cm(inch) :
        return 2.54*inch
    for i in range(5) :
        print(f'{i+1}인치 = {inch2cm(i+1)} 센티미터')

if flag == 7:
    def mean3(a,b,c) :
        return (a+b+c) / 3
    def max3(a,b,c) :
        return max(a,b,c)
    def min3(a,b,c) :
        return min(a,b,c)

    a,b,c = list(map(int,input("세 수를 입력하시오 : ").split())) #컨테이너로 n개의 대입 가능

    for i,v in [("평균값",mean3(a,b,c)),("최댓값",max3(a,b,c)),('최솟값',min3(a,b,c))] :
        print(f'{a}, {b}, {c}의 {i}은 {v}')

if flag == 9:
    def means_of_n(nums): # num은 리스트로 내가 만들어줄 것임.
        return (sum(nums) / len(nums))
    def max_of_n(nums) :
        return max(nums)
    def min_of_n(nums) :
        return min(nums)

    buffer = list(map(int,input("정수를 여러 개 입력하시오 : ").split(' ')))
    for i,v in [("평균값",means_of_n(buffer)),("최댓값",max_of_n(buffer)),('최솟값',min_of_n(buffer))] :
        if i=="평균값" :
            print(f'{i}은 {v:0.1f}')
            continue
        print(f'{i}은 {v}')

if flag == 11:
    def area(x1,x2,y1,y2) :
        return ((max(x1,x2) - min(x1,x2)) * (max(y1,y2) - min(y1,y2)))/2

    x1,y1,x2,y2 = list(map(input,[i+" 좌표를 입력하시오 : " for i in ["x1",'y1','x2','y2']]))
    x1,y1,x2,y2 = list(map(int,[x1,y1,x2,y2]))

    print('직각삼각형의 면적은 {}'.format(area(x1,x2,y1,y2)))

if flag == 13:
    def volume(s=0,w=0,h=0,l=0,r=0,select_mode = '') :
        if s>0:
            return s**3
        elif w>0 and h>0 and l>0 :
            return w*h*l
        elif r>0 and h>0 :
            if select_mode == '원뿔' :
                return (1/3)*3.14*(r**2)*h
            else :
                return 3.14*(r**2)*h
        else :
            return (4/3)*3.14*(r**3)

    print(f'모서리의 길이가 12인 정육면체의 부피 : {volume(s=12)}\n')
    print(f'모서리의 길이가 20인 정육면체의 부피 : {volume(s=20)}\n')
    print(f'가로, 세로, 길이가 각각 3, 5 ,6인 육면체의 부피 : {volume(w=3,h=5,l=6)}\n')
    print(f'반지름과 높이가 각각 20, 10인 원뿔의 부피 : {volume(r=20,h=10,select_mode="원뿔"):g}\n')
    print(f'반지름이 15인 구의 부피 : {volume(r=15):g}\n')
    print(f'반지름과 높이가 각각 20, 10인 원기둥의 부피 : {volume(r=20,h=10):g}\n')

if flag == 15:
    def my_sort(*nums) :
        tmp = list(nums)
        tmp.sort()
        print(f'결과 : {tmp}')
    my_sort(45,3,4,56,5)
    my_sort(9,8,7,6,5,4,3)

if flag == 17:
    def sum_range(n1,n2) :
        return sum(list(range(n1,n2+1)))

    print(f'10에서 {20:3}까지의 정수의 합 : {sum_range(10,20)}\n40에서 {100:3}까지의 정수의 합 : {sum_range(40,100)}')

if flag == 19:
    dict_init = {0:1 , 1:1} #메모이제이션을 위한 딕셔너리

    def fibo(n) :
        if n in dict_init: #메모된 값이 있으면 그것을 리턴
            return dict_init[n]
        else:
            output = fibo(n-1) +fibo(n-2)
            dict_init[n] = output #메모를 하는 코드
            return output

    n = int(input('fibo(n)의 n을 입력하세요: '))
    print(f'fibo({n}) = {fibo(n)}')

if flag == 21:
    def idenfification() :
        str = input('주민등록번호 첫 6숫자 형식 입력: ')

        while(1): #잘못된 입력 처리
            if(len(str) == 6) and (int(str[2:4])<13) and (int(str[4:])<32) :
                break
            else :
                str = input('주민등록번호는 형식에 맞게 6자리로 되어야합니다. 다시 입력해주세요 : ')

        if int(str[:2]) >= 51 : #1900년대생들
            print('19'+str[:2]+f'년 {str[2:4]}월 {str[4:]}일')
        else : #2000년생들
            print('20' + str[:2] + f'년 {str[2:4]}월 {str[4:]}일')

    idenfification()

if flag == 23:
    def area_and_circumference(r) :
        if r>=0:
            print('반지름을 입력하세요: {}'.format(r))
            print(f'넓이 : {(3.14*(r**2)):7.3f}, 둘레 : {(2*3.14*r):7.3f}')
        else :
            print('프로그램을 종료합니다.\n')
            quit()#함수 종료

        while(1):
            r = float(input('반지름을 입력하시오: '))
            if r>=0 :
                print(f'넓이 : {(3.14 * (r ** 2)):7.3f}, 둘레 : {(2 * 3.14 * r):7.3f}')
            else:
                print('프로그램을 종료합니다.')
                break
    area_and_circumference(6)

if flag == 25:
    def modify(str):
        str = str.strip() #함수이름과 변수이름이 같아도 괜찮다.
        if str.count('-') : # 하이폰이 있다면 모두 제거하는 블럭
            str = ''.join(str.split('-'))
        str = (''.join(str.split())).upper()

        return str, str.count('N')

    s1 = 'Kang Young Min'
    s2 = ' Kang Young-Min'
    s3 = 'Park Dong Min'
    s4 = ' Park Dong-Yun'

    for i in [s1,s2,s3,s4] :
        print(f'{i}(은)는 {(modify(i))[0]}으로 수정됨')
    for i in [s1,s2,s3,s4] :
        print(f'{(modify(i))[0]} : {(modify(i))[1]} 개의 N이 나타남')

if flag == 27:
    def unit_fraction(frac=0.5):
        delta = 0
        n = 2

        dict_fraction = {}

        frac =float(input('1보다 작고 0보다 큰 소수를 입력하세요 : '))

        print(frac)
        if (1):
            while (1): # frac이 내 메모리가 연산을 충분히 커버 가능할때

                delta1 = abs(frac - (1 / n))
                n += 1
                delta2 = abs(frac - (1 / n))

                if delta1 <= delta2:  # 무조건 가까운 애들 찾는다!
                    print(f'가장 가까운 단위 분수는 1/{n-1}이며, 이 값은 {1/(n-1)}입니다.')
                    return
                else:  # 못찾았으면 계속 루프 돌림
                    continue
        else :
            frac = '%0.50f' % frac
            pure_zero_num = 0 # 소수점 아래에서의 0들을 모두 센다. 단, 0이 아닌 다른 수가 나올때까지만!
            pure_str = ''
            start_compare = 0

            print(f'바뀐 frac의 값은 {frac}')
            print(f'len(frac)의 값은 {len(frac)}')

            for i in range(len(frac)):
                if (frac[i] == '0') or (frac[i] == '.') :
                    pure_zero_num +=1

            print(f'pure_zero_num의 값은 {pure_zero_num}')

            pure_zero_num -=2 # 소수점 왼쪽의 0과 '.' 센거 제외한 0의 갯수
            pure_str = frac[pure_zero_num+2:]

            print(pure_str)
            for i in range(4*(10**6)) : # 1/2 부터 1/4000000까지의 모든 단위 분수를 싹다 저장하는 딕셔너리를 만들자.
                dict_fraction[str(i+1)] = 1/(i+1) # 메모리에 저장 완료

            frac_result = int((dict_fraction[pure_str])*(10**(len(frac)-2)))
            print(f'가장 가까운 단위 분수는 1/{frac_result}이며, 이 값은 {1 / frac_result}입니다.')

    unit_fraction()
