# -*- coding : utf-8 -*-

output = map(sum,[[1,2,3],(4,5),[10,20,30]]) #sum 함수의 매개변수로는 iterable 만이 와야험
#map이나 filter는 타입이 builtin_function_or_method가 아니고, type이라는 타입임...)

print(list(output)) # map이나 filter함수의 리턴값은 제너레이터이므로 list로 캐스트를 해줘야함

