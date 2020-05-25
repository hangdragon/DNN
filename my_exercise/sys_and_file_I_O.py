# -*- coding : utf-8 -*-

"""
<새로운 파일 혹은 기존의 파일들을 다루고자 할때의 프로세스>

1. 파일을 열어야함. open함수를 활용하여 정해진 파일을 정해진 모드로 _io.TextIOWrapper라는 타입의 객체를 만들어준다.
    이떄, 파일 객체가 읽기 모드이면 이터레이터임.

2. mode : 'w' -> _ioTextIOWrapper라는 타입의 객체가 가진 메소드중에 write()이라는 함수로 파일안에 데이터를 넣어주자.
                이 write()라는 함수는 매개변수로 string을 받고, 리턴값으로는 int값(넣어준 str의 길이)를 반환한다.

                만약 키보드로 입력하게 된다면 \n이라 해준건 자동으로 \\n이 된다...(개같은 상황임)
                이럴떄는 '\n'.join(str.split('\\n'))으로 \\n -> \n로 변환해주자!
                한편, 파일 이름에 .txt나 .m을 붙여주어서 파일의 종류를 지정해줄 수 있다.

   mode : 'r' -> _ioTextIOWrapper라는 타입의 객체가 가진 메소드중에 read(),readline(),readlines()이라는 함수로 파일안에 데이터를 넣어주자.
                이 read 함수들은 '이레이터처럼 1번만 읽을 수 있다'이다! 그리고 각각의 리턴값은 str,str,list이다.
"""
import sys

def str_write(n) : # str을 n개 입력하는 함수
    buffer = []
    print("string을 {}번 입력하는 함수 시작하겠습니다.".format(n))

    for i in range(n) :
        buffer.append(input('{}번째 스트링을 입력하세요'.format(i+1)))
    return buffer

print("sys.argv[0]은 {}".format(sys.argv))

sys.argv.append(input("파일의 이름을 입력하시오 :"))
print()

with open(sys.argv[-1],'a') as f:
    f.write('\n'.join(input("파일안에 넣을 데이터들을 입력해주세요: ").split('\\n'))) # 파일안에 넣을 데이터들을 만약 키보드로 직접 입력 받는다면, \n을 입력해도 실제 입력되는 것은 \\n이다. 그리고 이는 엔터키 동작을 하지 않는다.
    """
    결국 키보드로 스트링을 입력받을때의 \\n를 \n로 바꾸기 위해서는 split하고 '\n'join함수를 써야한다.!!! '
    
    """

with open(sys.argv[-1],'r') as file :
    exec(file.read())




