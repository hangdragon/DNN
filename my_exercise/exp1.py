# -*- coding : utf -8 -*-

"""

읽기 모드로 파일 객체를 만들었을 떄, 파일 객체는 이터러블이자 이터레이터이다...
이터레이터나 제너레이터는 list() 캐스트, next() , for문을 통하여 1개씩 순차적으로 사용이 된다.

한편, 읽기 모드 파일 객체는 메소드를 사용해도
"""
with open('imargv', 'r') as f:
    print("f의 값은 {}이고, 타입은 {}입니다.".format(f,type(f)))

    print(next(f))
    for line in f : # 헐... 읽기모드의 파일 객체는 이터러블이다.
        print("f의 값은 {}이고, 타입은 {}입니다.".format(line,type(line)))

    for line in f : # 헐... 읽기모드의 파일 객체는 이터러블이다.
        print("f의 값은 {}이고, 타입은 {}입니다.".format(line,type(line)))
