# -*- coding : utf-8 -*-
"""

시간 카운팅 함수!!!!!!!!!!!!!!!!!!!!!!!!!


"""
import time


def time_counter():
    print("시간 카운팅 모드를 선택하셨습니다. 카운트를 시작하고 싶다면 y를 눌러주세요\n 만일, 실핼중 그만두고 싶다면 언제든 quit을 입력하시면 중단됩니다.")
    start_buffer = input("카운팅 시작을 위해 y를 입력해주세요: ")
    quit_buffer = "대기 중"

    if(start_buffer == "y") :

        number = 0
        tmp_time = time.time()
        while tmp_time :
            tmp_time = time.time() + 1
            print("현재 "+str(number)+"초 지났습니다.") # time이란 모듈을 불러낸 다음, 현재의 시간인 유닉스 타임(Unix Time)을 불러오고 싶다면, time.time() // 모듈이란 객체와 비슷

            while(tmp_time != time.time()) :
                pass
            number += 1


time_counter()