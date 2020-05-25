# -*- coding : utf-8 -*-

def make_nth_key():
    n = int(input('키를 몇개 만들 예정인가요:'))
    buffer = ''
    for i in range(n) :
        buffer += 'key'
        buffer += str(i+1)
        buffer += ' '
    #다돌면 buffer에 'key1 key2...'생김

    return buffer.split()

dict_a = {}.fromkeys(make_nth_key(),[])

print(dict_a)
