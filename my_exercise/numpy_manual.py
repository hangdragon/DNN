# *- coding : utf-8 -*-

"""
numpy 모듈의 사용법들은 다음과 같다.

1. 임포팅 : import numpy as np

2. list -> ndarray 캐스트 : ndarray_1 = np.array(컨테이너)

    - 1차원이나 2차원이나 type은 똑같이 numpy.ndarray이다.
    - ndarray의 정체 = 원소들끼리 쉼표(,)가 없는 리스트!(단, 트리에 대하여 ex) 2차원 ndarray에서는 [[1 2 3] , [4 5 6]]임.
    - 2차원 ndarray를 만들 때, np.array([n column 컨테이너 , n column 컨테이너 , ... , n column 컨테이너]) => 이렇게 리스트나 튜플을 혼용해도 되고, 반드시 각각 인자의 column 갯수 같아야함.
    - [ [n개] , [n개] , ... , [n개]] <= 그리고 전체 컨테이너의 원소의 갯수 = 행의 갯수 = m

3. ndarray -> list 캐스트 : (ndarray 변수).tolist()

4. int , float , list , ndarray간의 덧셈

    1) int 또는 float과 1차원 list / 1차원 list와 1차원 list간의 덧셈 : np.add(1st_ele , 2nd_ele)
        : 이때, 리턴값은 반드시 ndarray이고, in 또는 float은 더해지는 리스트의 모든 freedom slot(행)에 대하여 같다.

    2) int 또는 float과 2차원 list / 2차원 list와 2차원 list간의 덧셈 : np.add(1st_ele , 2nd_ele)
        : 이때, 리턴값은 반드시 ndarray이고, in 또는 float은 더해지는 리스트의 모든 freedom slot(행과 열)에 대하여 같다.

    3) list와 ndarray , ndarray와 ndarray간의 덧셈은 그냥 + 연산자로!

    결론)
        -list와 list , ndarray와 list, ndarray와 ndarray간의 덧셈은 무조건 element wise이므로 두 인자의 차원이 같아야함.
        - int , float, list , numpy에 대한 element wise 덧셈에 대한 리턴값의 타입은 무조건 ndarray!!!

5. 행렬의 type과 dimension을 헷갈리지 마라!
    -행렬의 type : list거나 numpy.ndarray이고, type()으로 알아낸다.
    -행렬의 차원 : (n,) (m,n)이고, (ndarray 변수).shape을 해주면 된다. dimension의 반환값은 tuple이다.

6. 기타 다른 행렬들을 만드는 방법

    1) ones : np.ones(차원,타입)을 하게되면 그 타입을 지닌 1이라는 원소들을 mxn 차원만큼 만들어줌.
        ex) tmp1 = np.ones((3,4))

    2) zeros : np.zeros(차원,타입)을 하게되면 그 타입을 지닌 0이라는 원소들을 mxn 차원만큼 만들어줌.
        ex) tmp2 = np.zeros((3,4))

    3) eye : np.eye(n)을 하게되면 float 타입의 nxn 정사각행렬을 만들어줌.
        ex) tmp3 = np.eye(4)

    4) arange : ndarray를 만들고자 할 때, np.array(컨테이너)를 쓰지 않고, np.arange(10) <- 이런식으로 range함수와 비슷하게 쓸 수 있다.
        ex) np.array(range(10) = np.arange(10)

    5) reshape : 1차원 ndarray(1차원 행렬)을 -> (ndarray 변수).reshape(차원)을 하게되면, 그 차원만큼 2차원 행렬로 바꿔주는 함수! (-1을 하게되면 그 방향으로 알아서 분배해준다)




#str는 컨테이너라고 보지 말자. 컨테이너는 5가지임. list set tuple dictionary ndarray
"""