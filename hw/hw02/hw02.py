""" Homework 2: Higher Order Functions"""

HW_SOURCE_FILE = 'hw02.py'

from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

######################
# Required Questions #
######################
def product(n, f):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    f -- a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    k, product = 1, 1
    while k <= n:
        product *= f(k)
        k += 1
    return product

def accumulate(combiner, base, n, f):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are f(1), f(2), ..., f(n).  combiner is a
    two-argument commutative, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    58
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    k, total = 1, base
    while k <= n:
        total = combiner(total, f(k))
        k += 1
    return total

def summation_using_accumulate(n, f):
    """Returns the sum of f(1) + ... + f(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, f)

def product_using_accumulate(n, f):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n , f)

def compose1(h, g):
    """Return a function f, such that f(x) = h(g(x))."""
    def f(x):
        return h(g(x))
    return f

def make_repeater(h, n):
    """Return the function that computes the nth application of h.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times! 
    5
    """
    "*** YOUR CODE HERE ***"
    # def repeater(x):
    #     k = 1
    #     total = x
    #     while k <= n:
    #         total = h(total)
    #         k += 1
    #     return total
    # return repeater
    return accumulate(compose1, identity, n, lambda k:h)
    #recall: identity = lambda x:x so identity(x) = x
    #we call compose on arguments identity and h(x) such that 
    #identity(h(x)) = h(x) on each successive iteration
    #thus accumulate will return nth application of h on x


##########################
# Just for fun Questions #
##########################

#for any natural number n, we can write it as a combination of the constant
#zero and successor function add1
# (add1(add1 0)) = 2 etc
# let n be a function that accepts one argument f that performs f n times in a row
# we let add1 be f so 
# n = lambda f: lambda x: f(f(x))
#     add 1      0        add1(add1(0))
#notice any natural number can be written as 1 + 1 + 1...+ 0
# 0 = lambda f: lambda x: x
# 1 = lambda f: lambda x: f(x)
# 2 = lambda f: lambda x: f(f(x))
#consider the function: one add1 that takes in the function and adds 1 to it one times
#general form for one add1 == n(lambda x: x + 1) where n = number of times add1 is called on the argument
#notice that if we take one add1 of zero, we can get back the value 1
#two add1 of zero, gets 2..three add1 gets 3 so on and so forth
#then we see that church numerals can be converted back to their decimal forms
#via a function that takes the church numeral as an argument n
#and returns n(lambda x: x + 1)(0) where lambda x: x + 1 is equal to add1
#thus add1 is taken in as argument into the church numeral and acts on 0
#for each f present in the numeral
#f(f(x)) is just (add1 (add1 0)) where each f takes in the add1 argument
#consider n = lambda f: lambda x: f(f(f(f(f(f(x))))))
#how can we calculate n + 1?
# observe that from 1 to 2, we need only add an additonal f
#the successor function computes the n+1 church numeral given
#church numeral n as argument
#this function should return lambda f: lambda x: f(n(f)(x))
#where n(f)(x) is equal to applying f n times onto x
#thus f(n(f)(x)) is equal to applying f (n + 1) times onto x

#how then do we do addition?
#currying: addition returns a function that takes another function to compute addition
# addition can be seen as applying the successor m times on a number n
# thus function should take in two numbers m and n in church numeral form
# and return m(f)(n(f)(x))
# for multiplication, notice that taking the product of m * n will result in
# a number mn that applies the function f mn times onto 0
# so multiplication should return m((n)(f)(x)) which means we apply f n times
# then take the result of applying f n times and apply it by m times 
# in total we would have applied f mn times
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    #calling successor(zero):
    #lambda f: lambda x: f((lambda x: x)(f)(x))
    #or f(f(x))
    return lambda f: lambda x: f(x)

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    #calling successor(one):
    #lambda f: lambda x: f((lambda f: lambda x: f(x)(f)(x)))
    #or f(f(x))
    return lambda f: lambda x: f(f(x))



def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    #call each church numeral function
    #note that zero takes in argument f and returns x 
    #x takes the value of 0 
    #one takes in argument f and returns f(x) where f = lambda x: x+1
    #f(x) takes argument of x with value 0 and returns x+1 which is 1
    return n(lambda x: x + 1)(0)

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(n(f)(x))
#still haven't found explanation for exponentiation of church numerals
def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return n(m)