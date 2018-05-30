#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import string


# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def print_words(filename):

    wc_dict = count_words_in_file(filename)

    print 'Number of unique words:', len(wc_dict)
    print

    for word in sorted(wc_dict.keys()):
        print word, wc_dict[word]


def print_top(filename):

    wc_dict = count_words_in_file(filename)

    # sorted_words = sorted(wc_dict.items(), key=count_for, reverse=True)
    # Sort by count then alphabetically - more interesting and easier to read
    sorted_words = sorted(wc_dict.items(), cmp=count_decreasing_then_word_increasing)
    top_20 = sorted_words if len(sorted_words) <= 20 else sorted_words[:20]

    print 'num in top 20 =', len(top_20)

    for item in top_20: print item[0], item[1]


def print_count_singles(filename):

    wc_dict = count_words_in_file(filename)

    num_singles = 0

    for word in sorted(wc_dict.keys()):
        if wc_dict[word] == 1:
            num_singles += 1

    print 'Number of words that only appear once in %s is %d' % (filename, num_singles)


def print_singles(filename):

    wc_dict = count_words_in_file(filename)

    print 'Words that only appear once in %s:' % filename
    print

    for word in sorted(wc_dict.keys()):
        if wc_dict[word] == 1:
            print word


def count_decreasing_then_word_increasing(t1, t2):
    """ Sort cmp: Compare input tuples, first by decreasing int count, then by increasing string word """

    # first sort by count descending
    if t1[1] != t2[1]:
        return t2[1] - t1[1]

    # sort words with same count
    return cmp(t1[0], t2[0])


def count_for(t):
    """ Sort key: map input tuple to count """
    return t[1]


def count_words_in_file(filename):
    wc_dict = {}
    f = open(filename, 'rU')
    for line in f:
        count_lowercase_words(wc_dict, line)
    f.close()
    remove_empty_strings_from(wc_dict)
    return wc_dict


def remove_empty_strings_from(wc_dict):
    if '' in wc_dict: del(wc_dict[''])


def count_lowercase_words(wordcounts_dict, line):
    lowercase_words = tolower(strip_trailing_punctuation_in(line.split()))
    count_words(wordcounts_dict, lowercase_words)


# def words_in(line):
#     return strip_trailing_punctuation_in(line.split())


def tolower(wordlist):
    return [word.lower() for word in wordlist]


def strip_trailing_punctuation_in(wordlist):
    return [strip_trailing_punct_from(word) for word in wordlist]


def strip_trailing_punct_from(word):
    # return word.translate(None, string.punctuation)

    i_last_letter = len(word) -1

    while i_last_letter >= 0 and word[i_last_letter] in string.punctuation:
        i_last_letter -= 1

    return '' if i_last_letter < 0 else word[:i_last_letter+1]


def count_words(wordcounts_dict, wordlist):
    """ Add a list of words to the hash of wordcounts """

    for word in wordlist:
        if word in wordcounts_dict:
            wordcounts_dict[word] = wordcounts_dict[word] + 1
        else:
            wordcounts_dict[word] = 1

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount | --countsingles | --singles} file'
        print 'argc=', len(sys.argv)
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    elif option == '--countsingles':
        print_count_singles(filename)
    elif option == '--singles':
        print_singles(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
