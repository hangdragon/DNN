# -*- coding : utf - 8 -*-

class Student:
    def __init__(self,name,korea,math,english,science):
        self.name = name # 멤버 변수(인스턴스,객체 변수)는 생성자에서 self.로 접근 지정해서 해준다!
        self.korea =korea
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        pass
