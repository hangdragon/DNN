# -*- coding : utf-8 -*-

"""for문 사용시 loop variable로는 n개가 올 수 있는데. n개가 올때에는 뒤의 iterable의 원소가 N차 벡터여야함.(n차 컨테이너)"""
list_3rd_dim_tuple = [(1,2,3),(4,5,6),(7,8,9)]

for i,j,k in list_3rd_dim_tuple :
    print("튜플의 1,2,3번째 값 ({},{},{})".format(i,j,k))