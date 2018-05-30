import wordcount

# counts repeated words
# updates counts when adding repeated words

unique_words = ['apple', 'banana', 'cucumber']
more_unique_words = ['date', 'gooseberry', 'lemon']

# counts unique words
def counts_unique_words():
    wordcounts = {}
    test_passed = True

    wordcount.count_words(wordcounts, unique_words)

    if not len(wordcounts.keys()) == len(unique_words):
        print 'Fail: Expected %d keys, got %d' % (len(unique_words), len(wordcounts.keys()))
        test_passed = False

    for word in unique_words:
        if not word in wordcounts:
            print 'Fail: Missing', word
            test_passed = False
        else:
            if wordcounts.get(word) != 1:
                print 'Fail: for %s, expected 1, got %d' % (word, wordcounts.get(word))
                test_passed = False

    if test_passed:
        print 'PASS', 'counts_unique_words'
    else:
        print '*** FAIL ***', 'counts_unique_words'


# adds more unique words
def adds_more_unique_words():
    wordcounts = {}
    for word in unique_words: wordcounts[word] = 1
    test_passed = True

    wordcount.count_words(wordcounts, more_unique_words)

    num_words = len(unique_words) + len(more_unique_words)
    if not len(wordcounts) == num_words:
        print 'Fail: Expected %d keys, got %d' % (num_words, len(wordcounts.keys()))
        test_passed = False

    for word in unique_words + more_unique_words:
        if not word in wordcounts:
            print 'Fail: Missing', word
            test_passed = False
        else:
            if wordcounts.get(word) != 1:
                print 'Fail: for %s, expected 1, got %d' % (word, wordcounts.get(word))
                test_passed = False

    if test_passed:
        print 'PASS', 'adds_more_unique_words'
    else:
        print '*** FAIL ***', 'adds_more_unique_words'


    return


def main():
    counts_unique_words()
    adds_more_unique_words()


if __name__ == '__main__':
    main()
