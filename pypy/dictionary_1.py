# -*- coding : utf-8 -*-

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풆플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str:
        print(key,":",character[key])
    elif type(character[key]) is int:
        print(key,":",character[key])
    elif type(character[key]) is dict:
        for i in ["sword", "armor"] :
            print(key,":",character[key][i])
    else :
        for i in character[key] :
            print(key , ":" , i)