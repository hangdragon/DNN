# -*- coding : utf-8 -*-
a = """\
Python에서 범해질 수 있는 오류들(4가지)
1. IndexError : indexing , slicing이 잘못 된 경우 혹은 함수를 사용할 때 요구되는 매개변수 갯수의 불충족
2. TypeError : Type이 서로 다른 애들끼리 연산하는 경우
3. ValueError : 문자형태의 str을 숫자로 바꾸려 할때 혹은 소수점 형태의 str를 int로 바꾸려할 떄
4. IndentationError :조건, 반복문에서 tab이 제대로 되어있지 않은 경우
"""

print(a)
print(id(a), end = ' ')
print("= a의 주소")

if 0 :
    pass
else :
    pass

