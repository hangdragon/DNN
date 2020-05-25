# -*- coding: utf-8 -*-

"""리스트 평탄화 문제"""

#넘겨받은 data를 변화시킬지(파괴적 함수로 만들지) , 변화시키지 말고 buffer로 출력할지(비파괴적 함수)

#비파괴적 함수로 만들어보자

def flatten(data) :

    output = []
    for item in data : #일단 리스트만 넣어야함! 그리고 아규먼트가 아터러블이므로 실행 됨.
        if type(item) == list : #재귀를 없애는 부분을 꼭 리프로 하여 if문 초반에 박을 필요도 없다. 그러니까 여기서는 재귀를 없애는게 != list가 아니다.
            output += flatten(item)
        else :
            output.append(item)
    return output


example = [[1,2,3], [4,[5,6]]],7,[8,9]

print(example)
print(flatten(example))
