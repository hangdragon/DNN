# -*- coding : utf-8 -*-

def show_queue(tmp) :
    window = '현재 queue의 상태는 : '
    print_buffer = []
    for i in tmp :
        window += f'{str(i):>10}|'
    print_buffer.append(window)
    return list(map(print,print_buffer)) # 리턴값을 줄때, 실행문을 실행까지 시킬 수 있다.

def queue(list_x) :
    yield show_queue(list_x)

    for i in range(len(list_x)):
        dequeue = list_x[i]
        list_x[i] = '\000' * 10
        yield dequeue

input_list = list(range(100,1001,100))
queue1 = queue(input_list) # 제너레이터 객체 생성.

next(queue1); print(); #초기화

for i in queue1 : #내가 만든건 제너레이터이고, for문을 통해 하나씩 나오는 i는 각 yield값을 말한다.
    print(f'큐의 원소는 {i}')
