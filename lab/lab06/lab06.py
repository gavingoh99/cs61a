this_file = 'lab06.py'
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    #input is n and returns an adder function that takes in a value x such
    #that it returns n + x, then n + x + 1 next time so nonlocal x is incremented
    def adder_inc(x):
        nonlocal n
        result = n + x
        n = n + 1
        return result
    return adder_inc

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    #for fib 1 and fib 2... fib 1 = 0, prev1 prev2 none none
    #fib 2 = 1 prev1 prev2 0 none
    #fib3 = 1 prev1 prev2 1 0
    # prev1, prev2 = -1, -1
    # def fib():
    #     nonlocal prev1, prev2
    #     if prev1 == -1 and prev2 == -1: #for fib 1
    #         prev1 = 0
    #         return 0
    #     elif prev1 == 0 and prev2 == -1:
    #         prev1, prev2 = 1, prev1
    #         return 1
    #     else:
    #         fib_curr = prev1 + prev2
    #         prev1, prev2 = prev1 + prev2, prev1
    #         return fib_curr
    # return fib
    #instead we can use a third variable known as index to track the current fib call
    #to include the two base cases, fib 1 and fib 2 without affecting the 
    #prev1 and prev2 variables which on initialization contain the values of fib 1 and fib 2
    #so if index = 0, return fib 1 value which is prev2, index = 1, return fib2 value which is prev1
    #else curr_fib is the sum of previous 2 fibs fib1 and fib2 and 
    #assign prev1 and prev2 to curr_fib and prev1 then return curr_fib for each call
    prev1, prev2 = 1, 0
    index = -1
    def fib():
        nonlocal prev1, prev2, index
        if index == 0:
            return prev2
        elif index == 1:
            return prev1
        else:
            curr_fib = prev1 + prev2
            prev1, prev2 = curr_fib, prev1
            return curr_fib
    return fib

# Generators
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    #gen function that yields elements from it scaled by multiplier
    yield from map(lambda x: multiplier * x, it)

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    #hailstone sequence:
    #n is positive integer
    #if n is even divide by 2
    #if n is odd, multiply by 3 and add 1
    #if n is 1, return 1
    yield n
    if n != 1:
        if n % 2 == 0:
            yield from hailstone(n // 2)
        else:
            yield from hailstone(3 * n + 1)
        



