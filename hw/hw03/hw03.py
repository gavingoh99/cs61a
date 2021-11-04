HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    #2 base cases for when x is single digit, if x is 7 then recursive call returns 1
    #else returns 0
    #each recursive call calls itself on n // 10 while checking in the process if last_digit is 7
    if x == 7:
        return 1
    elif x // 10 == 0 and x != 7:
        return 0
    elif x % 10 == 7:
        return 1 + num_sevens(x // 10)
    else:
        return num_sevens(x // 10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # i, value = 1, 1
    # decreasing = False
    # while i <= n:
    #     if i % 7 == 0 or num_sevens(i):
    #         if not decreasing:
    #             value += 1
    #             decreasing = True
    #         else:
    #             value -= 1
    #             decreasing = False
    #     else:
    #         if not decreasing:
    #             value += 1
    #         elif decreasing:
    #             value -= 1
    #     i += 1
    # return value
    def helper(value, index, increment):
        if index == n:
            return value
        elif index % 7 == 0 or num_sevens(index):
            if increment > 0:
                #flip the increment from plus to subtract or vice versa
                return helper(value-increment, index+1, -increment)
        else:
            return helper(value+increment, index+1, increment)
    return helper(1, 1, 1)

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
    "*** YOUR CODE HERE ***"
    #find coin higher than total to cover all possible combinations
    def largest_coin(i):
        if i > total:
            return i
        else:
            return largest_coin(2 * i)
    def helper(total, coins):
        if total == 1:
            return 1
        elif total < 0:
            return 0
        elif coins == 1:
            return 1
        else:
            return helper(total - coins, coins) + helper(total, coins // 2)
    return helper(total, largest_coin(1))
    # if total > 16:
    #     helper(total, 16)
    # elif total > 8:
    #     helper(total, 8)
    # elif total > 4:
    #     helper(total, 4)
    # elif total > 2:
    #     helper(total, 2)
    # else:
    #     helper(total, 1)
    #use function to determine which coin to start with: see above


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
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    #to solve for n we must solve for n-1
    #how do we strip n into smaller versions of itself? to make 1248 become 124
    #we can try to get 124 from 1248 using floor division and store 8 as a separate variable
    #then we can compare last digit of 124 with 8, notice that if there are no missing digits 
    #as per 12345, the difference between last and second last digit is == 1
    #so if last digit of 124 and 8 have a difference of more than 1, then we 
    #can calculate number of missing digits, missing digits are 5, 6 and 7
    #from 8 - 4 = 4 if we subtract 1 we get 3 which is equal to number of missing digits
    #we have a condition to be checked each call: whether last - second last > 1
    #now a base case: the approach is to divide n by 10 each call so the recursion
    #must stop when n can no longer be divided by 10 or in other words when n == 0
    #so if no missing digits we should return helper(count, n // 10, n % 10)
    #passing the new n and reassigning the new last digit to last_digit
    def helper(count, all_but_last, last_digit):
        if all_but_last == 0:
            return count
        else:
            if last_digit - all_but_last % 10 > 1:
                return helper(count + last_digit - all_but_last % 10 - 1, n // 10, n % 10)
            else:
                return helper(count, n // 10, n % 10)
    return helper(0, n, 0)


###################
# Extra Questions #
###################

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
    "*** YOUR CODE HERE ***"
    #let start be rod 1 and end be rod 3
    #first we look at when n = 1, we move top disk from 1 to 3
    #n = 2, we move top disk from 1 to 2, top disk from 1 to 3, then top disk from 2 to 3
    #n = 3, we move top disk from 1 to 3, top disk from 1 to 2, top disk from 3 to 2, top disk from 1 to 3, top disk from 2 to 1, top disk from 2 to 3, top disk from 1 to 3
    if n == 1:
        print_move(start, end)
    else:
        #find the middle peg
        other_peg = 6 - start - end
        #recall that to move n stack, need to move n-1 stack to middle
        move_stack(n-1, start, other_peg)
        #move the nth disk from start to end
        print_move(start, end)
        #then move the n-1 stack from middle to end
        move_stack(n-1, other_peg, end)
from operator import sub, mul, xor

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    #lambda f: f(f) refers to function f taking in f as argument and returning
    #f as a parameterless f, in the form ff() which results in
    #f(f(f(f(f(1))))) where f(1) is computed and returned to the second inner f...
    #so f(1) * that value of n until it reaches f(4) * n to give f(5)
    #https://lptk.github.io/programming/2019/10/15/simple-essence-y-combinator.html
    #for more info on y-combinator which uses this concept
    #when called in lambda f: lambda n: ... it makes it such that
    #make_anonymous_factorial() becomes make_anonymous_factorial on function call
    #such that the return value lambda n: 1 if n == 1 else mul(n, f(f)(n-1)) is called on the next argument
    #note also that f(f) is a function call of lambda n since f(f) points to lambda n
    #via the lambda f: f(f) (lambda f: lambda n: ...) notation
    return (lambda f:f(f))(lambda f: lambda n: 1 if n == 1 else mul(n, f(f)(n - 1)))