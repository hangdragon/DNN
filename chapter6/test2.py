# -*- coding : utf-8 -*-

def writing(filename,text) :
    try :
        file = open(filename,'w')

        print('나는 바보')
        # try안에 n개의 예외가 있다고 한다면, 맨 처음으로 나오는 예외만 걸리고 그 다음부터는 프로그램 다운된다. (실행 안된다)
        #웅애()
        raise NotImplementedError(
            '웅이!!!!! 강 제 종 료!!! 프로그램 실행 못하게 죽일거'
        )
        웅애()
        print('후후')
        return
        file.write(text)

    except Exception as e :
        print(f'type(Exception) : {type(e)}')
        print(f'Exception : {e}')

    finally :
        file.write(text)
        file.close()
writing('tttt.py','안녕!')