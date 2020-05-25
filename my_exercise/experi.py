# -*- coding : utf -8 -*-

import sys

sys.argv.append(input('생성할 파일의 이름을 입력하세요 : ')) # sys.argv[1]에 파일의 이름이 들어갔다.

"""파일 이름을 입력 받고 , 그 파일 안에 계속 글을 쓴다."""
with open(sys.argv[-1] , 'a') as f: # with 키워드를 이용하여 해당 모드에 대한 파일 객체를 생성함!
    buffer = '1'
    print('파일 안의 내용을 그만 쓰고싶다면 quit을 입력하세요.')

    while buffer != 'quit' :
        buffer = input('>>> ')
        f.write(buffer)
        f.write('\n') #파이썬 스크립트 파일 안에 이스케이프 코드를 넣게되면 그것을 그대로 실행하여서 쓰기에 반영하지만, 키보드로 이스케이프 코드롤 입력하게되면 그런거는 무시되고 글자 그대로 쓰여진다.

    f.close()

with open(sys.argv[-1],'r') as f: # 읽기모드로 만든 파일 객체는 이터레이터이고, 큐이다. 그리고
    print(f' f는 {f}이고 , f의 타입은 {type(f)}이다.') # 이터레이터는 리스트등으로 캐스트해주거나 next()함수들 참조를 하지 않는 이상 그대로 남아있는다. 여기서는 이터레이터에서 사용을 하지 않았으므로 살아있음.

    for i in f.readlines():
        if i != '\n' :
            exec(i) #모든 행 전부다 실행

    f.close()