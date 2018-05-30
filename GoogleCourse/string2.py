#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):

    if len(s) < 3: return s

    if s[-3:] == 'ing':
        return s + 'ly'

    return s + 'ing'


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    index_not = s.find('not')
    index_bad = s.find('bad')
    if index_bad > index_not:
        return s[0:index_not] + 'good' + s[index_bad+3:]
    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    mid_a = midpoint(a)
    mid_b = midpoint(b)
    return a[:mid_a] + b[:mid_b] + a[mid_a:] + b[mid_b:]


def midpoint(b):
    return (len(b) + 1) / 2


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# DD: Modified to print input value if supplied
def test(got, expected, instring=''):
    forinput = ('for input=' + instring) if len(instring) > 0 else instring
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s %s got: %s expected: %s' % (prefix, forinput, repr(got), repr(expected))


def test_not_bad(instring, expected):
    test(not_bad(instring), expected, instring)


def test_front_back(s1, s2, expected):
    test(front_back(s1, s2), expected, ('"' + s1 + '"+"' + s2 + '"'))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing', 'hail')
    test(verbing('swiming'), 'swimingly', 'swiming')
    test(verbing('do'), 'do', 'do')
    test(verbing('happen'), 'happening', 'happen')

    print
    print 'not_bad'
    test_not_bad('This movie is not so bad', 'This movie is good')
    test_not_bad('This dinner is not that bad!', 'This dinner is good!')
    test_not_bad('This tea is not hot', 'This tea is not hot')
    test_not_bad("It's bad yet not", "It's bad yet not")

    print
    print 'front_back'
    test_front_back('abcd', 'xy', 'abxcdy')
    test_front_back('abcde', 'xyz', 'abcxydez')
    test_front_back('Kitten', 'Donut', 'KitDontenut')



if __name__ == '__main__':
    main()
