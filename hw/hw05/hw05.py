


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.quantity = 0
        self.money = 0
    def restock(self, quantity):
        self.quantity = self.quantity + quantity
        return 'Current '+str(self.item)+' stock: '+str(self.quantity)
    def add_funds(self, money):
        if not self.quantity:
            return 'Machine is out of stock. Here is your $'+str(money)+'.'
        else:
            self.money = self.money + money
            return 'Current balance: $'+str(self.money)
    def vend(self):
        if not self.quantity:
            return 'Machine is out of stock.'
        elif self.money >= self.price:
            self.quantity -= 1
            change = self.money - self.price
            self.money = 0
            if change == 0:
                return 'Here is your '+str(self.item)+'.'
            else:
                return 'Here is your '+str(self.item)+' and $'+str(change)+' change.'
        else:
            return 'You must add $'+str(self.price-self.money)+' more funds.'

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    entries = []
    def helper(t):
        entries.append(t.label)
        for branch in t.branches:
            helper(branch)
    helper(t)
    return entries

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    "*** YOUR CODE HERE ***"
    # prev_link = None
    # front_of_list = None
    # for char in str(n):
    #     current_link = Link(int(char))
    #     if prev_link:
    #         prev_link.rest = current_link
    #     prev_link = current_link
    #     if not front_of_list:
    #         front_of_list = prev_link
    # return eval(repr(front_of_list))

    #handle base case that n is single digit
    if n < 10:
        return Link(n)
    first = int(str(n)[0])
    #handle recursive call of store_digits on rest of digits
    rest = store_digits(int(str(n)[1:]))
    #return a linked list with first and the return value from rest
    return Link(first, rest)

def generate_paths(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    "*** YOUR CODE HERE ***"
    if t.label == value:
        yield [t.label]
    for branch in t.branches:
        for branch_label in generate_paths(branch, value):
            yield [t.label] + branch_label
    

## Optional Questions
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"
    #at most two children, leaf is automatically a bst
    #children are valid bsts
    #entry of left child is less than or equal to label of t
    #entry of right child is greater than label of t
    def bst_min(t): #bst_min is a function that finds the smallest label in a tree
        if t.is_leaf(): #if the tree is a leaf the smallest label is its label
            return t.label
        return min(bst_min(t.branches[0]), t.label) #else find the min value of its left branch then take the min between the label and the smallest value in the left branch
    def bst_max(t): #bst_max is a function that finds the largest label in a tree
        if t.is_leaf(): #return label if it is a leaf
            return t.label
        return max(bst_min(t.branches[-1]), t.label) #else find the max value by comparing the right branch and the label

    if t.is_leaf(): #a leaf is a binary search tree
        return True
    if len(t.branches) == 1: #if there is only one branch, let it satisfy either the left or right branch criteria
        return bst_max(t.branches[0]) <= t.label or bst_min(t.branches[0]) > t.label
    left_branch, right_branch = t.branches[0], t.branches[1]
    #else return the truth value of checking if both left and right are bsts and that the max value of the left branch is <= label and min value of right branch is > label
    return is_bst(left_branch) and is_bst(right_branch) and bst_max(left_branch) <= t.label and bst_min(right_branch) > t.label
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125

    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        return kind(self.year)
    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Mint.current_year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        return self.cents + max(0, Mint.current_year - self.year - 50)

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

def remove_all(link , value):
    """Remove all the nodes containing value in link. Assume that the
    first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    #link = Link(first, rest)
    #first element is never removed so we look into rest which we can access using [1]
    #rest itself is also of the structure Link(first, rest)
    while link.rest != Link.empty and link.rest.first == value:
        link.rest = link.rest.rest
    if link.rest == Link.empty: 
    #consider the base case when link.rest is empty,
    # we are unable to call the first instance attribute from the empty attribute thus we must exit the function once the end of the linked list is reached to prevent an error
        return None
    elif link.rest.first != Link.empty:
        remove_all(link.rest, value)

def deep_map(f, link):
    """Return a Link with the same structure as link but with fn mapped over
    its elements. If an element is an instance of a linked list, recursively
    apply f inside that linked list as well.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print(s) # unchanged
    <1 <2 3> 4>
    >>> print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
    <<2 <4 6> 8> <<10>>>
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        return Link.empty
    if isinstance(link.first, Link):
        first = deep_map(f, link.first)
    else:
        first = f(link.first)
    return Link(first, deep_map(f, link.rest))
## Link Class ##

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

## Tree ADT ##

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
