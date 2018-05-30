#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count = 0
    for s in words:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1

    return count


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    xs = []
    non_xs = []

    for word in words:
        if word.startswith('x'):
            xs.append(word)
        else:
            non_xs.append(word)

    result = sorted(xs)
    result.extend(sorted(non_xs))
    return result


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    return sorted(tuples, key=last_of_tuple)


def last_of_tuple(t):
    return t[-1]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# DD: Modified to print input value if supplied
def test(got, expected, in_list=None):
    for_input = '' if in_list is None else 'for input=' + repr(in_list)

    if got == expected:
        print ' OK  %s got: %s' % (for_input, repr(got))

    else:
        print '  X  %s got: %s expected: %s' % (for_input, repr(got), repr(expected))


def test_match_ends(in_list, expected):
    test(match_ends(in_list), expected, in_list)


def test_front_x(in_list, expected):
    test(front_x(in_list), expected, in_list)


def test_sort_last(t, expected):
    test(sort_last(t), expected, t)


# Calls the above functions with interesting inputs.
def main():
    print 'match_ends'
    test_match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test_match_ends(['', 'x', 'xy', 'xyx', 'xx'], 2)
    test_match_ends(['aaa', 'be', 'abc', 'hello'], 1)

    print
    print 'front_x'
    test_front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
                 ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test_front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
                 ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test_front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'],
                 ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print
    print 'sort_last'
    test_sort_last([(1, 3), (3, 2), (2, 1)],
                   [(2, 1), (3, 2), (1, 3)])
    test_sort_last([(2, 3), (1, 2), (3, 1)],
                   [(3, 1), (1, 2), (2, 3)])
    test_sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)],
                   [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
