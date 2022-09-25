from ast import Continue
from re import T


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    
    assert (k >= 0)and(isinstance(k,int)), 'k must be non-negative integer.'
    
    if k == 0:
        return 1
    
    FallingFactorial = n
    while k > 1:
        FallingFactorial = FallingFactorial * (n - 1)
        n -= 1
        k -= 1
    
    return FallingFactorial

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    assert (y >= 0)and(isinstance(y,int)), 'y must be non-negative integer.'
    SumDigits = 0
    LeftDigits = y
    while True:
        SumDigits += (LeftDigits % 10)
        LeftDigits = LeftDigits // 10
        if LeftDigits == 0:
            break
    return SumDigits


    



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    >>> double_eights(-82881)
    True
    """
    LeftDigits = abs(n)
    while True:
        
        if LeftDigits == 0:
            return False
        
        CurrentNum = LeftDigits % 10
        if CurrentNum != 8:
            LeftDigits = LeftDigits // 10
            Continue
        else:
            if ((LeftDigits // 10) % 10) == 8:
                return True
            else:
                LeftDigits = LeftDigits // 10

