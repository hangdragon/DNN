# -*- coding : utf-8 -*-

import random

print('하이스텝 글램핑 인원들을 랜덤하게 4개의 조로 편성할 예정이다.\n')

dict_teams = {
    '1조' : [],
    '2조' : [],
    '3조' : [],
    '4조' : []
}
people = []

print('글램핑 엠티를 가는 인원들을 추가하세요.\n')
while('quit' not in people) :
    people.append(input('>>> '))
people.pop() # quit제거

select = ['1조','2조','3조','4조']
for i in people :
    if len(select) == 0 :
        select = ['1조', '2조', '3조', '4조'] # key space 다시 초기화 

    key = random.choice(select)
    select.remove(key)
    dict_teams[key].append(i)

print(dict_teams)
