# -*- coding : utf-8 -*-

"""try 안에 에러가 N개 있다면, 실행중에 제일 먼저 얻어걸리는 에러가 단 1개만 뜨고 그 뒤로는 프로그램 강제 종료!"""
list_x = list(range(1,100))

try :
    tmp = int(input('인덱스를 입력하세요:'))
    print(f'해당 인덱스에 대한 값은 : {list_x[tmp]}\n')
    raise NotImplementedError(
        '아무 문제도 예외도 없는데 그냥 강제로 예외 밣생시켜 봤어 ㅎㅎ\n'
    )
except Exception as e:
    print(f'에러 타입 : {type(e)}\n에러 내용 : {e}')
finally :
    print("나는 파워 파이널리 웅이!")