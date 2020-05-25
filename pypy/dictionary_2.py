# -*- coding : utf-8 -*-

pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 3},
    {"name" : "아지", "age" : 3},
    {"name" : "호랑이", "age" : 1}
]

print("#우리 동네 애완동물")
for number in pets :
    print(number["name"] , str(number["age"]) + "살")
