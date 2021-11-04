from operator import add, sub, mul

def prune_min(t):
    """Prune the tree mutatively from the bottom up.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    #      6
    #     / \
    #    3   4
    "*** YOUR CODE HERE ***"
    if not t.is_leaf():
        left = t.branches[0]
        right = t.branches[1]
        if left.label > right.label:
            t.branches.remove(left)
            prune_min(right)
        else:
            t.branches.remove(right)
            prune_min(left)



def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def inner(x):
        for num in naturals():
            if num % m == x:
                yield num
    for x in range(m):
        yield inner(x)

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return z
    return fn(link.first, foldr(link.rest, fn, z))
    
def mapl(lst, fn):
    """ Maps FN on LST
    >>> lst = Link(3, Link(2, Link(1)))
    >>> mapl(lst, lambda x: x*x)
    Link(9, Link(4, Link(1)))
    """
    "*** YOUR CODE HERE ***"
    return foldr(lst, lambda x, xs: Link(fn(x), xs), Link.empty)

# Account
class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven's money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    "*** YOUR CODE HERE ***"
    def deposit_check(self, check):
        if check.payable_to == self.holder and not check.deposited: 
            Account.deposit(self, check.quantity)
            check.deposited = True
            return self.balance
        else:
            print('The police have been notified.')


class Check(object):
    "*** YOUR CODE HERE ***"
    def __init__(self, payable_to, quantity):
        self.payable_to = payable_to
        self.quantity = quantity
        self.deposited = False

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    #fn(z, link.first)
    #fn(fn(z, link.first), link.rest.first)
    #fn(fn(fn(z, link.first), link.rest.first), link.rest.rest.first...)
    #for left fold, accumulate the z parameter with the nested fn.. then when
    #link is empty, return z which contains all the nested fn..
    return foldl(link.rest, fn, fn(z, link.first))

def filterl(lst, pred):
    """ Filters LST based on PRED
    >>> lst = Link(4, Link(3, Link(2, Link(1))))
    >>> filterl(lst, lambda x: x % 2 == 0)
    Link(4, Link(2))
    """
    "*** YOUR CODE HERE ***"
    def helper(fir, sec):
        if pred(fir):
            return Link(fir, sec)
        else:
            return sec
    return foldr(lst, helper, Link.empty)

def reverse(lst):
    """ Reverses LST with foldl
    >>> reverse(Link(3, Link(2, Link(1))))
    Link(1, Link(2, Link(3)))
    >>> reverse(Link(1))
    Link(1)
    >>> reversed = reverse(Link.empty)
    >>> reversed is Link.empty
    True
    """
    "*** YOUR CODE HERE ***"
    if lst is Link.empty:
        return Link.empty
    def helper(fir, sec):
        return Link(sec, fir)
    return foldl(lst, helper, Link.empty)

identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    #Link(3, Link(2, Link(1)))
    #foldr(_, mul, 1)
    #mul(3, mul(2, mul(1, 1)))
    #foldl(_, mul, 1)
    #mul(mul(mul(1, 1), 2), 3)
    #foldl2(_, mul, 1)
    #expect mul(mul(mul(1, 1), 2), 3)
    #foldr(_, step, identity)(z)
    #step(3, step(2, step(1, identity)))(1)
    #f(f(f(1))) where f = fn(g(y), x)
    #mul(mul(mul(identity(1), 1), 2), 3)
    #mul(mul(mul(1, 1), 2), 3)
    #this is the hardest function i've done so far :)
    def step(x, g):
        # if g == identity:
        #     return fn(z, x)
        # else:
        #     return fn(g, x)
        #if g is identity, we can simply apply g onto z on the inner most step
        #we need a higher order function that takes in z as argument
        def f(y):
            return fn(g(y), x)
        return f
        #result is returning nested f with an inner z,
        #each nested f acts on the return value of the inner f
        #starting from mul(identity(1), 1)
    return foldr(link, step, identity)(z) #z is outside so foldr(link, step, identity) must include a function that returns a function

def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    "*** YOUR CODE HERE ***"
    sum_s = sum(s)
    #create a list of lists containing possible combinations with s[0]
    combinations = [[]]
    for i in s[1:]:
        all_combinations = combinations.copy()
        for combination in all_combinations:
            combinations.append(combination + [i])
    #create map instance applying sum on each list within combinations
    sum_combinations = map(lambda x: sum(x), combinations)
    #filter possible combinations
    #notice that to take the diff in sums between two combinations
    #for [1, 5, 4], if combination is [1, 4] and [5]
    #combination with s[0] is [4]
    #the difference in sum between [1,4] and [5] is 1+4-5 = 0
    #using combination with s[0], notice that the mapped instance contains sum(combination with s[0])
    #to take the diff in sums, with respect to sum_s which contains one instance of each number
    #sum_s = 1 + 5 + 4
    #we can find the sum of numbers not included in combination with s[0] by
    #subtracting s[0] + sum(combination with s[0]) from sum_s
    #but the difference between sum of numbers not included with s[0] and 
    #combination with s[0] is what we want
    #so we have to take the sum of these numbers and again subtract s[0] + sum(combination with s[0])
    #and check with d
    #notice we subtracted s[0] and sum(combination with s[0]) twice
    #so we could just take the absolute value of 2*s[0] + 2*x where lambda x (mapped instance)
    #subtract the sum_s and compare that with d
    possible_combinations_within_d = filter(lambda x: abs(2*x + 2*s[0] - sum_s) <= d, sum_combinations)
    return len(list(possible_combinations_within_d))
        

# Link Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Tree Class
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

# naturals
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