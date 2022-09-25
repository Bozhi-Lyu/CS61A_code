HW_SOURCE_FILE=__file__


def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    def func_adder(g=lambda x: x):
        f = lambda x: func( g(x) )
        return composer(f)
    
    func = lambda x: func_adder(func(x))

    return func, func_adder

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)
    

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n <= 3:
        return n
    
    i = 4
    g3, g2, g1 = 1, 2, 3
    while i <= n:
        gi = g1 + 2*g2 + 3*g3 #max is g1, min is g3
        g1, g2, g3 = gi, g1, g2
        i += 1
    return gi


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    def md(n_left, num = 0):
        print("DEBUG:", n_left, num)
        if n_left // 10 == 0:
            return num
        
        TenDigit = ((n_left % 100)-(n_left % 10)) // 10
        if (n_left % 10 - TenDigit) >= 1:
            delta_num = n_left % 10 - TenDigit - 1
        else:
            delta_num = 0
        return md(n_left // 10, num + delta_num)
    return md(n)

def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    import math
    MaxCoin = 2 ** ( int(math.log2(total)) )
    
    def g( LeftVaule, mc):
        if mc == 1:     #base case: all min coin
            return 1
        elif LeftVaule == 0:    #base case: none min coin
            return 1
        elif mc > LeftVaule:
            return g(LeftVaule, mc//2)
        else:
            return g(LeftVaule - mc, mc) + g(LeftVaule, mc//2)

    return g( total, MaxCoin)

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(start, end)  #base case
        return
    
    move_stack(n-1, start, 6-start-end)
    print_move(start, end)
    move_stack(n-1, 6-start-end, end)
#region: editor's note: 
# 1. According to HINT 2: "The strategy used in Towers of Hanoi is to 
#   move all but the bottom disc to the second peg, then moving the bottom disc to 
#   the third peg, then moving all but the second disc from the second to the third peg."
#
# 2. editor's note: the base case of the recursion need to return "None" to finish the call.
#endregion

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda k: lambda f: f(f, k)(lambda f, k: k if k == 1 else k*f(f, k-1))
#region: editor's note:
# 1. m_a_f() is an anonymous function λ(k)
#
# 2. According to the function fact: 
#           fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
#   we can replace the function fact by a lambda function which can be referred by itself, which means 
#   that this lambda function has two arguments, n and the function itself.
#
# 3. Define a function λ(f, k): 
#           k if k == 1 else k*f(f, k-1)
#   f is this function itself, k is the argument passed by the function m_a_f().
#
# 4. Because of 2 and 3, the return expression shuould be:
#           return λ(k): operand
#   the operand is λ(f, k), in which f is λ(f, k). Namely, the operand is:
#           λ(f, k): k if k == 1 else k*f(f, k-1)
#   As a result, the return expression should be:
#           return λ(k): ( λ(f): f(f, k) )( f = λ(f, k) )
#
# 5. Which is the right one and what's the difference between 
#           return lambda k: (lambda f: f(f, k))(lambda f, k: k if k == 1 else k*f(f, k-1))
#   and
#           return (lambda k, f: f(f, k))(lambda f, k: k if k == 1 else k*f(f, k-1))
#   ?
#   The 1st is right. Actually it's:
#           return λ(k): (  λ(f)|f = ...  ) 
#   but:    
#           return ( λ(k, f)|f = ... )
#   because if a function takes two positional arguments, they cann't be given seperately.
#endregion