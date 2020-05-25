# -*- coding:utf-8 -*-

with open('MyDiary.txt', 'w') as f:
    f.writelines([
        "2020년 05 02일. 나른하지만은 않은 오후.\n",
        '\n',
        '나는 오늘도 무언가를 열심히 한다. 요즘 나에게 있어서 가장 관심있는 것은 상화,친구들 만나기와 클라이밍이다.\n',
        '음악에 대한 열정은 사라진지 오래이다. 작곡은 이전부터 손에서 놓았고, 그나마 관심있던 보컬도 레슨이 끝난 이후에 실력이 감퇴하면서 관심이 줄었다.\n',
        '대학원 석사까지는 무조건 마쳐야게다는 생각이다. 그리하여 겨울에 컨택도 한 것인데, 요즘들어 분야에 대한 확신도 안서고 잘 모르겠다..\n',
        '학점만이라도 잘 챙겨야지 나중에 선택의 폭이 넓어지는데.. 복습은 너무 밀렸다.\n' ,
        '\n',
        '그러나 마냥 포기할수만은 없다. 이번학기에 열린 마음으로 클라이밍, 사람들, 그리고 정말 많은 지식들을 불티나게 습득한다면 나에게 또 다른 미래가 펼치질 지 모른다.\n\n'
        '화이탕!!'
    ])
    f.writable()
    f.close()

with open('MyDiary.txt', 'r') as f:

    for line in f:
        print(line)

        #글을 쓸 때, f.write()도 가능하고 , f.writelines()도 가능하다. 그리고 한편, 파일 객체 안에 글을 쓸떄는 무조건 'str'만 허용된다.