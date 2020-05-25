def unit(a) : #스칼라를 판단하는 거임.
    if a >= 0 :
        return 1
    else :
        return 0

def sigmoid(x) :
    return 1/(1+np.exp(-x))

def relu(x) :
    if x>=0 :
        return x
    else :
        return 0

def leaky_relu(x) :
    if x>=0 :
        return x
    else :
        return 0.1*x