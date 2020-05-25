# -*- coding : utf-8 -*-

def show_queue(tmp) :
    window = '현재 queue의 상태는 : '
    print_buffer = []
    for i in tmp :
        window += f'{str(i):>10}|'
    print_buffer.append(window)
    return list(map(print,print_buffer)) # 리턴값을 줄때, 실행문을 실행까지 시킬 수 있다.

def queue(n) :
    tmp = []
    for i in range(n):
        tmp.append(int(input('>>> ')))
    yield show_queue(tmp)

    for i in range(len(tmp)):
        pop = tmp[i]
        tmp[i] = '\000' * 10
        yield (pop,show_queue(tmp))

queue = queue(10) # 제너레이터 객체 생성.

next(queue)
list_x = []

for i in range(10) :
    list_x.append(next(queue)[0])

print(list_x)