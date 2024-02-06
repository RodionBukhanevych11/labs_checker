from typing import List, Dict


def Task3(params: Dict) -> List:
    a = params["a"]
    xn1 = 1
    xn = 0
    while abs(xn1 - xn) > 1e-4:        
        xn = xn1
        xn1 = 1/2*(xn + a/xn)
        
    return (xn1,)


def Task4(params: Dict) -> List:
    a = params["a"]
    return (123, a[0] == 0, 'abc')