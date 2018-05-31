import unittest
import list2

# noinspection PyMethodMayBeStatic
class list2UnitTest(unittest.TestCase):


    def test_remove_adjacent_in_middle(self):
        self.assertEqual([1, 2, 3], list2.remove_adjacent([1, 2, 2, 3]))

    def test_remove_adjacent_at_start(self):
        self.assertEqual([2, 3], list2.remove_adjacent([2, 2, 2, 3]))

    def test_remove_adjacent_at_end(self):
        self.assertEqual([1, 3], list2.remove_adjacent([1, 3, 3]))

    def test_remove_multiple_adjacent_groups(self):
        self.assertEqual([1, 2, 3], list2.remove_adjacent([1, 1, 2, 2, 2, 3, 3, 3]))

    def test_remove_multiple_adjacent_from_empty(self):
        self.assertEqual([], list2.remove_adjacent([]))



    def test_merges_non_overlapping_lists(self):

        list_1      = ['aa', 'bb']
        list_2      = ['dd', 'ee', 'ff']
        expected    = ['aa', 'bb', 'dd', 'ee', 'ff']

        self.do_test_merge(expected, list_1, list_2)


    def test_merges_overlapping_lists(self):

        list_1      = ['aa', 'xx', 'zz']
        list_2      = ['bb', 'cc']
        expected    = ['aa', 'bb', 'cc', 'xx', 'zz']

        self.do_test_merge(expected, list_1, list_2)


    def test_merges_mixed_up_lists(self):

        list_1      = ['aa', 'dd', 'ee']
        list_2      = ['bb', 'cc', 'ff']
        expected    = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']

        self.do_test_merge(expected, list_1, list_2)


    def test_merges_lists_with_duplicates(self):

        list_1      = ['aa', 'aa']
        list_2      = ['aa', 'bb', 'bb', 'cc', 'ff']
        expected    = ['aa', 'aa', 'aa', 'bb', 'bb', 'cc', 'ff']

        self.do_test_merge(expected, list_1, list_2)


    def test_merges_two_empty_lists(self):

        list_1      = []
        list_2      = []
        expected    = []

        self.do_test_merge(expected, list_1, list_2)


    def test_merges_empty_first_list(self):

        list_1      = []
        list_2      = ['xx']
        expected    = ['xx']

        self.do_test_merge(expected, list_1, list_2)


    def test_merges_empty_second_list(self):

        list_1      = ['aa', 'bb']
        list_2      = []
        expected    = ['aa', 'bb']

        self.do_test_merge(expected, list_1, list_2)


    ######################

    def do_test_merge(self, expected, list_1, list_2):

        self.assertEqual(list_1, sorted(list_1), 'TEST ERROR: Input lists must be sorted')
        self.assertEqual(list_2, sorted(list_2), 'TEST ERROR: Input lists must be sorted')

        list1_str = ', '.join(list_1)
        list2_str = ', '.join(list_2)
        # Merge modifies input lists
        list_1A = list_1[:]
        list_2A = list_2[:]

        merged = list2.merge_lists(list_1, list_2)
        self.assertEqual(expected, merged, ('merge_lists:  List1: [' + list1_str + '], List2: [' + list2_str) + ']')

        merged = list2.linear_merge(list_1A, list_2A)
        self.assertEqual(expected, merged, ('linear_merge:  List1: [' + list1_str + '], List2: [' + list2_str) + ']')



if __name__ == '__main__':
    unittest.main()
