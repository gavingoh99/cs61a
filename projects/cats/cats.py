"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    #select is a function that takes in paragraphs and returns a boolean value
    #apply select onto paragraphs and index to the kth paragraph that returns true
    #else return ''
    currK = -1
    for currParagraph in paragraphs:
        if select(currParagraph):
            currK += 1
            if currK == k:
                return currParagraph
    if k > currK:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    #function takes a list as input
    #returns a function that returns a boolean value if paragraph contains any words in list
    def select(currParagraph):
        currParagraph = split(remove_punctuation(lower(currParagraph)))
        for word in topic:
            if word in currParagraph:
                return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    #function takes in two strings which are split into two lists of words
    #compare word at nth index of typed_words with word at nth index of reference_words
    #use enumerate to keep tab of current index
    if typed_words == [] or reference_words == []:
        return 0.0
    correct_words, total_words = 0, 0
    for count, word in enumerate(typed_words):
        if count <= len(reference_words) - 1:
            if word == reference_words[count]:
                correct_words += 1
        total_words += 1
    return (correct_words / total_words) * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    #typed is a string input, elapsed is positive and in seconds, need to convert
    #to minutes via / 60
    #wpm formula: convert len to numwords by / 5
    return (len(typed) * 60)/ (elapsed * 5)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    #function takes in string user_word, list of strings called valid_words
    #diff_function takes in two strings, user_word and word in valid_words and limit
    #base case is that user_word in valid_words, then we simply return user_word
    if user_word in valid_words:
        return user_word
    smallest_word = min(valid_words, key=lambda valid_word: diff_function(user_word, valid_word, limit))
    if diff_function(user_word, smallest_word, limit) > limit:
        return user_word
    else:
        return smallest_word

    # END PROBLEM 5


def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    #takes two strings, and returns minimum number of characters needed to change
    #from start word to goal word
    #if unequal length then diff in length is added to total
    #if number of characters greater than limit then return any number larger than limit
    #limit + 1 and minimize computation
    #use recursion
    def helper(start, goal, curr_char):
        if curr_char > limit:
            return limit + 1
        m, n = len(start), len(goal)
        if m == 0 and n == 0:
            return curr_char
        if m == n:
            if start[0] != goal[0]:
                return helper(start[1:], goal[1:], curr_char + 1)
            else: return helper(start[1:], goal[1:], curr_char)
        elif m > n:
            return helper(start[:n], goal, curr_char + m - n)
        else:
            return helper(start, goal[:m], curr_char + n - m)    
    return helper(start, goal, 0)
    # END PROBLEM 6


def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    #three operations are add, remove or substitute
    #tree recursion example where all three operations are executed on start word
    #each time an operation is executed, limit - 1 since limit defines number of 
    #allowable operations
    #base case is if limit < 0 whereby if limit < 0, number of operations exceeds limits
    #and len(start) or len(goal) == 0 to stop recursion from going to infinity
    #for addtion, treat it as if goal word is sliced from 1th letter onwards since
    #adding a letter to start to match first letter of goal would mean 0th index
    #letters match
    #for removing, treat it as if start word is sliced from 1th letter since
    #removing a letter from start is akin to taking the rest of the letters from start
    #other than the 0th letter
    #substitution of letter in start means that both letters at 0th index match
    #so recursively call feline_fixes on start and goal from the 1th letter
    #if 0th letter of start and goal are already the same, no operations need to be taken
    #recursively call on 1th letter onward of start and goal without reducing limit
    if limit < 0: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start) or len(goal)
        # END

    else:
        # BEGIN
        "*** YOUR CODE HERE ***"
        if start[0] == goal[0]:
            return feline_fixes(start[1:], goal[1:], limit)
        add_diff = feline_fixes(start, goal[1:], limit-1)
        remove_diff = feline_fixes(start[1:], goal, limit-1)
        substitute_diff = feline_fixes(start[1:], goal[1:], limit-1)
        return min(add_diff, remove_diff, substitute_diff) + 1
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    #takes in typed and prompt, and calculates progress: the ratio of correct words
    #up to the first incorrect word divided by prompt words
    #then stores id and progress in a dictionary as keys
    correct_words = 0
    for count, word in enumerate(typed):
        if word == prompt[count]:
            correct_words += 1
        else: break
    progress = correct_words / len(prompt)
    message = {'id': id, 'progress': progress}
    send(message)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    #takes in a list of lists
    #returns a list of lists containing the difference between timestamps
    #this is done by taking the nth element subtracted by the n-1th and appending it to times
    times = []
    for player_timestamp in times_per_player:
        times.append([player_timestamp[i] - player_timestamp[i-1] for i in range(1, len(player_timestamp))])
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    #takes in game, a data abstraction of a list containing a list of words, and a list of lists called times
    #returns a list of the list of words each player typed fastest, ie 
    #[['Hello'], ['world']], here p0 typed 'Hello' the fastest while p1 typed 'world' the fastest
    #create a compound list containing empty lists for all players first
    #then iterate through all the words, looking for the fastest time among players
    #then go to index of fastest player for that word and append that word into their list
    #repeat for all words then return the compound list
    fastest = [[] for _ in players] #compound list creation recall that _ is used when iteration variable is not directly used in computation
    for word in words:
        fastest_time = None
        fastest_player = None
        for player in players:
            if not fastest_time or time(game, player, word) < fastest_time:
                fastest_time = time(game, player, word)
                fastest_player = player
        fastest[fastest_player].append(word_at(game, word))
    return fastest

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)