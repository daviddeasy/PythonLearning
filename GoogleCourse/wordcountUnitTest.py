import unittest
import wordcount

unique_words        = ['apple', 'banana', 'cucumber']
more_unique_words   = ['date', 'gooseberry', 'lemon']


# noinspection PyMethodMayBeStatic
class WordCountTest(unittest.TestCase):

    wordcounts_dict = {}

    def setUp(self):
        self.wordcounts_dict = {}


    def test_counts_unique_words(self):

        wordcount.count_words(self.wordcounts_dict, unique_words)

        self.verify_keys_are_exactly(unique_words)
        self.verify_all_counts(unique_words, 1)


    def test_adds_more_unique_words(self):

        self.set_up_dict_with(unique_words, 1)

        wordcount.count_words(self.wordcounts_dict, more_unique_words)

        self.verify_keys_are_exactly(unique_words + more_unique_words)
        self.verify_all_counts(unique_words + more_unique_words, 1)


    def test_counts_repeated_words(self):

        self.set_up_dict_with(unique_words + more_unique_words, 1)

        wordcount.count_words(self.wordcounts_dict, unique_words + more_unique_words + unique_words)

        self.verify_keys_are_exactly(unique_words + more_unique_words)
        self.verify_all_counts(unique_words, 3)
        self.verify_all_counts(more_unique_words, 2)


    def test_one_repeating_word(self):

        word = unique_words[0]
        wordcount.count_words(self.wordcounts_dict, [word] * 5)

        self.verify_keys_are_exactly({word})
        self.verify_all_counts({word}, 5)


    def test_converts_wordlist_to_lowercase(self):

        self.assertEqual(['apple', 'banana', 'pear'], wordcount.tolower(['APPLE', 'Banana', 'pear']))


    def test_counts_lowercase_of_unique_words_in_a_line(self):

        line_of_unique_words = self.space_separated_uppercase_string_from(unique_words)

        wordcount.count_lowercase_words(self.wordcounts_dict, line_of_unique_words)

        self.verify_keys_are_exactly(unique_words)
        self.verify_all_counts(unique_words, 1)

    def test_counts_lowercase_of_repeated_words_in_a_line(self):

        line_of_repeated_words = self.space_separated_uppercase_string_from(unique_words + unique_words)

        wordcount.count_lowercase_words(self.wordcounts_dict, line_of_repeated_words)

        self.verify_keys_are_exactly(unique_words)
        self.verify_all_counts(unique_words, 2)

    def space_separated_uppercase_string_from(self, word_list):
        line = ""
        for word in word_list: line += ' ' + word.upper()
        line += ' '
        return line


    def test_strips_trailing_comma(self):
        self.strips_trailing_punctuation(',')

    def test_strips_trailing_period(self):
        self.strips_trailing_punctuation('.')

    def test_strips_trailing_multiple_punctuation(self):
        self.strips_trailing_punctuation(':.')

    def strips_trailing_punctuation(self, punct):
        expected = 'hello'
        self.assertEqual(expected, wordcount.strip_trailing_punct_from(expected + punct))


    def test_does_not_strip_middle_hyphen(self):
        self.strip_trailing_punct_does_not_change('see-saw')

    def test_does_not_strip_leading_comma(self):
        self.strip_trailing_punct_does_not_change(',hello')

    def test_strip_trailing_punct_handles_one_letter_with_leading_comma(self):
        self.strip_trailing_punct_does_not_change(',a')

    def test_strip_trailing_punct_handles_empty_string(self):
        self.strip_trailing_punct_does_not_change('')

    def strip_trailing_punct_does_not_change(self, s):
        self.assertEqual(s, wordcount.strip_trailing_punct_from(s))


    def set_up_dict_with(self, words, count):
        for word in words: self.wordcounts_dict[word] = count


    def verify_keys_are_exactly(self, keys):
        self.verify_num_keys(len(keys))
        for word in keys:
            self.assertTrue(word in self.wordcounts_dict, 'Missing word=' + word)

    def verify_num_keys(self, num_expected_keys):
        num_keys = len(self.wordcounts_dict)
        self.assertEqual(num_expected_keys, num_keys,
                         'Expected %d unique words but got %d' % (num_expected_keys, num_keys))

    def verify_all_counts(self, keys, count):
        for word in keys:
            self.assertEqual(count, self.wordcounts_dict[word])



if __name__ == '__main__':
    unittest.main()
