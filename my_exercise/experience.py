# -*- coding : utf -8 -*-

import random
import sys

sys.argv.append(input('파일명을 입력하시오: '))
list_first = '강김나박성이장태한'
list_name = ('지용','상와','태현','지우','기섭','웅이')
with open(sys.argv[-1],'w') as f:
    for i in range(10) :
        name = random.choice(list_first) + random.choice(list_name) #random.choice([컨테이너])
        weight = random.randrange(40,100) # randon.randrange() , 무작위 정수 추출
        height = random.randrange(140,200)

        f.write(f'{name}, {weight}, {height}\n')

with open(sys.argv[-1],'r') as f:
    for line in f :
        name,weight,height = line.strip().split(", ")

        if (not name) or (not weight) or (not height) :
            continue
        bmi = int(weight) / ((int(height)/100)**2)
        result = ''
        if 25 <= bmi :
            result = '과체중'
        elif 18.5 <= bmi :
            result = "정상 체중"
        else :
            result = '저체중'

        print('\n'.join([
            "이름 : {}",
            "몸무게 : {}",
            "키 : {}",
            "BMI : {}",
            "결과 : {}"
        ]).format(name,weight,height,bmi,result))
        print()