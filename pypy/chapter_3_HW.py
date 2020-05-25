# -*- coding: utf-8 -*-

flag_test = 31

if flag_test == 1 :
    #1번문제

    str = []

    #(1)~(6)
    str.append("{} {} {} = {}".format(100,">",200,100>200))
    str.append("{} {} {} = {}".format(100, ">=", 200, 100 >= 200))
    str.append("{} {} {} = {}".format(100, "<", 200, 100 < 200))
    str.append("{} {} {} = {}".format(100, "<=", 200, 100 <= 200))
    str.append("{} {} {} = {}".format(100, "==", 200, 100 == 200))
    str.append("{} {} {} = {}".format(100, "!=", 200, 100 != 200))

    #(7),(8)
    str.append("{} {} {} = {}".format(200, "==", 200, 200 == 200))
    str.append("{} {} {} = {}".format(200, "!=", 200, 200 > 200))

    #(9)~(12)

    str.append("{} {} {} = {}".format(True,"or",True,True or True))
    str.append("{} {} {} = {}".format(True, "or", False, True or False))
    str.append("{} {} {} = {}".format(True, "and", False, True and False))
    str.append("{} {} {} = {}".format(True, "and", True, True and True))

    #(13),(14)
    str.append("{} {} {} {} {}= {}".format(True, "or", True, "and", False, True or True and False)) #??질문
    str.append("{} {} {} {} {}= {}".format(True, "and", True, "or", False, True and True or False))

    #(15)
    str.append("{} {} {} = {}".format('Morning', "<", 'morning', 'Morning' < 'morning'))

    #(16)
    str.append("{} {} {} = {}".format("A", ">", "B", "A" > "B"))

    print("\n".join(str))

if flag_test == 2 :
    #2번문제

    name = input("이름을 입력하시오: ")
    height = float(input("키를 입력하시오(단위 cm) : "))
    if height > 140 :
        print("{} 님은 놀이기구를 탈 수 {}.".format(name, "있습니다"))
    else :
        print("{} 님은 놀이기구를 탈 수 {}.".format(name, "없습니다"))

if flag_test == 3 :
    #3번문제

    age = int(input("나이를 입력하시오: "))
    height = float(input("키를 입력하시오(단위 cm) : "))

    if (age >=19) and (height >=150) :
        print("입장할 수 {}.".format("있습니다"))
    else :
        print("입장할 수 {}.".format("없습니다"))

if flag_test == 4 :
    #4번문제

    age = int(input("나이를 입력하시오: "))

    if age >= 20 :
        print("{}".format("Adult"))
    elif age >= 10 :
        print("{}".format("Youth"))
    else :
        print("{}".format("Kid"))

if flag_test == 5 :
    #5번문제

    tmp1 ,tmp2 = input("두 정수를 입력하시오 : ").split() #split()을 이용하여 input함수로 여러개의 변수를 입력받으면, 그떄는 str형의 element를 가진 list형태이다.

    tmp1 = int(tmp1)
    tmp2 = int(tmp2)

    if tmp1>= tmp2 :
        print("{} {}".format(tmp2,tmp1))
    else :
        print("{} {}".format(tmp1,tmp2))

if flag_test == 6 :
    #6번문제

    tmp1 ,tmp2, tmp3 = input("세 정수를 입력하시오 : ").split()

    tmp1 = int(tmp1)
    tmp2 = int(tmp2)

    if tmp1 >= tmp2 :
        smaller = tmp2
        other = tmp1
    else :
        smaller = tmp1
        other =tmp2

    tmp3 = int(tmp3)

    if smaller >= tmp3 :
        smallest = tmp3
        print("{} {} {}".format(smallest, smaller , other))
    else :
        smallest = smaller
        if other >= tmp3 :
            print("{} {} {}".format(smallest , tmp3,other))
        else :
            print("{} {} {}".format(smallest , other , tmp3))

if flag_test == 7 :
    #7번문제

    game_score = int(input("게임점수를 입력하시오 : "))
    if game_score >= 1000 :
        print("{}입니다.".format("고수"))
    else :
        print("{}입니다.".format("입문자"))

if flag_test == 8 :
    #8번문제

    x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
    x = int(x)
    y = int(y)

    if (x > 0) and (y > 0) :
        print("{}사분면에 있음".format(1))
    elif (x < 0) and (y > 0) :
        print("{}사분면에 있음".format(2))
    elif (x < 0) and (y < 0):
        print("{}사분면에 있음".format(3))
    elif (x > 0) and (y < 0):
        print("{}사분면에 있음".format(4))
    else :
        pass

if flag_test == 9 :
    #9번문제

    number = int(input("정수를 입력하시오 : "))

    if (number % 2) == 0 :
        print("{}는(은) {}(으)로 {}".format(number, 2, "나누어집니다."))
    else :
        print("{}는(은) {}(으)로 {}".format(number, 2, "나누어지지 않습니다."))

    if (number % 3) == 0 :
        print("{}는(은) {}(으)로 {}".format(number, 3, "나누어집니다."))
    else :
        print("{}는(은) {}(으)로 {}".format(number, 3, "나누어지지 않습니다."))

    if ((number % 2) == 0) and ((number%3)==0) :
        print("{}는(은) {}와(과) {} 모두로 {}".format(number, 2, 3, "나누어집니다."))
    else :
        print("{}는(은) {}와(과) {} 모두로 {}".format(number, 2, 3, "나누어지지 않습니다."))

if flag_test == 10 :
    #10번문제

    a, b = input("두 정수를 입력하시오 : ").split()
    a = int(a)
    b = int(b)

    if(a%b) == 0 :
        print("{}는(은) {}의 {}".format(a,b,"배수입니다."))
    else :
        if (b%a) == 0 :
            print("{}는(은) {}의 {}".format(b, a, "배수입니다."))
        else:
            print("{}는(은) {}의 {}".format(a, b, "배수가 아닙니다."))

if flag_test == 11 :
    #11번문제

    lottery = '239'

    a , b ,c = input("세 복권번호를 입력하시오 : ").split()
    a = int(a)
    b = int(b)
    c = int(c)

    if (a<=0) or (a>10) :
        a = 0
    if (b<=0) or (b>10) :
        b = 0
    if (c<=0) or (c>10) :
        c = 0

    total = "{}{}{}".format(a,b,c)

    if ('2' in total) and ('3' in total) and('9' in total) :
        print("상금 {}".format("1억 원"))
    elif ((('2' in total) and ('3' in total)) or (('3' in total) and ('9' in total)) or (('9' in total) and ('2' in total))) :
        print("상금 {}".format("1천만 원"))
    elif (('2' in total) or ('3' in total) or ('9' in total))  :
        print("상금 {}".format("1만 원"))
    else :
        print("다음 기회에...")

if flag_test == 12 :
    #12번문제

    x , y = input("x, y 좌표를 입력하세요 : ").split()
    x = float(x)
    y = float(y)

    if (x**2 + y**2) <100 :
        print("원의 {}에 있음".format("내부"))
    elif (x**2 + y**2) >100 :
        print("원의 {}에 있음".format("외부"))
    else :
        pass

if flag_test == 13 :
    #13번문제

    x, y = input("x, y 좌표를 입력하세요 : ").split()
    x = float(x)
    y = float(y)

    if ((x-3) ** 2 + (y-3) ** 2) < 100:
        print("원의 {}에 있음".format("내부"))
    elif ((x-3) ** 2 + (y-3) ** 2) > 100:
        print("원의 {}에 있음".format("외부"))
    else:
        pass

if flag_test == 14 :
    #14번문제

    alphabet = input("알파벳을 입력하시오 : ")
    str_vowel = 'aeiou'

    if alphabet in str_vowel :
        print("{} (은)는 {}입니다.".format(alphabet, "모음"))
    else :
        print("{} (은)는 {}입니다.".format(alphabet, "자음"))

if flag_test == 15 :
    #15번문제

    select_mode = input("for문을 사용하고 싶으면 : f , while문을 사용하고 싶으면 : w 를 입력하세요 : ")

    if select_mode == 'f' :
        for i in range(1,10) :
            print("{} {} {} {} {}".format(2,'*',i,'=',2*i))

    if select_mode == 'w' :
        i = 1
        while 2*i <20 :
            print("{} {} {} {} {}".format(2,'*',i,'=',2*i))
            i += 1

if flag_test == 16 :
    #16번문제

    tmp = int(input("1에서 9까지의 수를 입력하세요:"))
    while not(1<= tmp <= 9) :
        tmp = int(input("1에서 9까지의 수를 다시 입력하세요:"))

    select_mode = input("for문을 사용하고 싶으면 : f , while문을 사용하고 싶으면 : w 를 입력하세요 : ")

    if select_mode == 'f' :
        for i in range(1,10) :
            print("{} {} {} {} {}".format(tmp,'*',i,'=',tmp*i))

    if select_mode == 'w' :
        i = 1
        count = 0
        while count < 9 :
            print("{} {} {} {} {}".format(tmp,'*',i,'=',tmp*i))
            i += 1
            count += 1

if flag_test == 17 :
    #17번문제

    for i in range(3) :
        print('Python ')
        print('is ')
        print('FUN! ')
    print()

    for i in range(3) :
        print('Python ')
        print('is ')
    print('FUN! ')
    print()

    for i in range(3) :
        print('Python ')
    print('is ')
    print('FUN! ')

if flag_test == 18 :
    #18번문제

    print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
    print("{} {}\n{} {}\n{} {}".format('(1)','햄버거' ,'(2)', "치킨",'(3)', '피자'))
    menu = int(input("{}에서 {}까지의 메뉴를 선택하세요 : ".format(1,3)))

    while (menu != 1) and (menu != 2) and (menu !=3) :
        menu = int(input("메뉴를 다시 입력하세요 : "))

    if menu ==1 :
        print("{}을 선택하였습니다.".format("햄버거"))
    elif menu ==2 :
        print("{}을 선택하였습니다.".format("치킨"))
    else :
        print("{}을 선택하였습니다.".format("피자"))

if flag_test == 19:
    #19번문제

    print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
    print("{} {}\n{} {}\n{} {}".format('-', '햄버거(입력 b)', '-', "치킨(입력 c)", '-', '피자(입력 p)'))
    menu = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ")

    while menu not in 'bcp':
        menu = input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")

    if menu == 'b':
        print("{}을 선택하였습니다.".format("햄버거"))
    elif menu == 'c':
        print("{}을 선택하였습니다.".format("치킨"))
    else:
        print("{}을 선택하였습니다.".format("피자"))

if flag_test == 20:
    #20번문제

    layer = int(input(" 숫자를 입력하세요 : "))
    for i in range(int(layer)) :
        str_buffer = ''

        for space_bar in range(layer -(i+1)) :
            str_buffer += ' '
        for star in range(i+1) :
            str_buffer += '*'

        print(str_buffer)
        str_buffer = ''

if flag_test == 21:
    #21번문제

    num = int(input("숫자를 입력하세요 : "))
    modulus = 1
    factor_counter = 0

    if (num%2) == 0 :
        if num == 2 :
            print('{}는 {}'.format(num, '소수입니다'))
        else:
            print('{}는 {}'.format(num, '소수가 아닙니다'))

    else:
        while modulus <= (num-1):
            modulus += 2
            if (num % modulus) == 0:
                factor_counter +=1

        if factor_counter == 1 :
            print('{}는 {}'.format(num, '소수입니다'))
        else:
            print('{}는 {}'.format(num,'소수가 아닙니다'))

if flag_test == 22:
    #22번문제

    for num in range(2,13) :
        modulus = 1
        factor_counter = 0

        if (num%2) == 0 :
            if num == 2 :
                print('{:2d} : {}'.format(num, '소수'))
            else:
                print('{:2d} : {}'.format(num, '합성수'))

        else:
            while modulus <= (num-1):
                modulus += 2
                if (num % modulus) == 0:
                    factor_counter +=1

            if factor_counter == 1 :
                print('{:2d} : {}'.format(num, '소수'))
            else:
                print('{:2d} : {}'.format(num,'합성'))

if flag_test == 23:
    #23번문제

    number = int(input("숫자를 입력하시오 : "))
    total = 0

    for i in range(1,number+1):
        total += i**2

    print("결과는 {}입니다.".format(total))

if flag_test == 24:
    #24번문제

    number = int(input("정수 숫자를 입력하시오 : "))
    total = 0

    while number <= 0 :
        number = int(input("정수 숫자를 다시 입력하시오 : "))

    for i in range(1,number+1):
        total += (1/i)**2

    print("결과는 {}입니다.".format(total))

if flag_test == 25:
    #25번문제

    distance = 0
    day_count = 0

    while (distance+7) < 30 : #n번째 날의 낮이 지나고 밤을 기다리는 중에!
        distance += 7
        day_count +=1
        print("day : {}  달팽이의 위치 : {} 미터".format(day_count, distance))

        distance -= 5 #n번째 밤이 지나간다...

    print("day : {}  달팽이의 위치 : {} 미터\n".format(day_count+1,distance+7))

    print("우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(day_count+1))

if flag_test == 26:
    #26번문제

    n = int(input("n을 입력하시오 : "))
    buffer = 0
    tmp = ''

    if 1<n<10 :
        for row in range(1, n + 1):

            if row % 2 == 1:
                if row == 1:
                    for i in range(1, n + 1):
                        print("{:2d}".format(i), end=" ")
                    print()
                else:
                    for i in range(1, n + 1):
                        print("{:2d}".format(buffer + i), end=" ")
                    print()
            if row % 2 == 0:
                for i in range(n,0,-1):
                    print("{:2d}".format(buffer + i), end=" ")
                print()
            buffer += n
    else :
        pass

if flag_test == 27:
    #27번문제

    armstrong = []

    for i in range(100,1000) :
        if ((i//100)**3 + ((i-((i//100)*100))//10)**3 + (i-((i//100)*100)-(((i-((i//100)*100))//10)*10))**3) == i : #100,10,1의자리 세제곱 합이 원래 수랑 같은지 비교
            armstrong.append(str(i)) # 그 암스트롱 수 하나하나를 스트링으로 변환해서 리스트에 집어넣음
    print("세 자리의 암스트롱 수 : {}".format(" ".join(armstrong))) #스트링 원소들을 가진 리스트를 join함수를 이용해서 출력하기 좋은 스트링으로 변환

if flag_test == 28:
    #28번문제

    n = input("정수를 입력하시오 : ")

    for i in range(len(n)) :
        if n[i] != n[len(n)-(i+1)] :
            print("{}은(는) 거꾸로 {}".format(n,"정수가 아닙니다."))
            break

        if i >= (len(n) -i) :
            print("{}은(는) 거꾸로 {}".format(n, "정수입니다."))
            break

if flag_test == 29:
    #29번문제

    fuel = 500

    while fuel >=50 :
        var = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오 : "))
        fuel += var
        print("현재 탱크 양은 {} 입니다.".format(fuel))
    print("경고 : 연료가 10% 미만이니 충전하세요!")

if flag_test == 30:
    #30번문제

    select_mode = 0

    print("{}  {}  {}  {}".format("1)덧셈" , "2)뺼셈", "3)곱셈", "4)나눗셈"))
    select_mode = (input("어떤 연산을 원하는지 번호를 입력하세요 : "))
    if select_mode not in "1234" :
        print("잘못 입력하였습니다.")

    else :

        print("연산을 원하는 숫자 두개를 입력하세요 ")
        ele1 = int(input())
        ele2 = int(input())

        if select_mode == "1" :
            print("{} {} {} = {}".format(ele1,'+',ele2,ele1+ele2))
        elif select_mode == "2" :
            print("{} {} {} = {}".format(ele1,'-',ele2,ele1-ele2))
        elif select_mode == "3" :
            print("{} {} {} = {}".format(ele1,'*',ele2,ele1*ele2))
        else :
            if ele2 == 0 :
                print("잘못 입력하였습니다.")
            else:
                print("{} {} {} = {}".format(ele1,'/',ele2,ele1/ele2))

if flag_test == 31:
    #31번문제

    divisor_list = []
    sum = 0

    #안해 ㅅㅂ 답지 볼거임 ㅅㄱ