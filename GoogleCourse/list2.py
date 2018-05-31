#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    result = []
    if len(nums) > 0:
        result.append(nums[0])
        for num in nums[1:]:
            if result[-1] != num:
                result.append(num)
    return result


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def merge_lists(list1, list2):
    if len(list1) == 0: return list2
    if len(list2) == 0: return list1

    result = []
    from1 = list1.pop(0)
    from2 = list2.pop(0)

    while True:
        if from1 <= from2:
            result.append(from1)
            if len(list1) == 0:
                result.append(from2)
                result.extend(list2)
                return result
            from1 = list1.pop(0)

        else:
            result.append(from2)
            if len(list2) == 0:
                result.append(from1)
                result.extend(list1)
                return result
            from2 = list2.pop(0)


# Note: the solution above is kind of cute, but unfortunately list.pop(0)
# is not constant time with the standard python list implementation,
# so the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order.
# That solution works in linear time, but is more ugly.
def linear_merge(list1, list2):
    if len(list1) == 0: return list2
    if len(list2) == 0: return list1

    result = []
    from1 = list1.pop(-1)
    from2 = list2.pop(-1)

    while True:
        if from1 >= from2:
            result.append(from1)
            if len(list1) == 0:
                result.append(from2)
                if len(list2):
                    list2.reverse()
                    result.extend(list2)
                result.reverse()
                return result
            from1 = list1.pop(-1)

        else:
            result.append(from2)
            if len(list2) == 0:
                result.append(from1)
                if len(list1):
                    list1.reverse()
                    result.extend(list1)
                result.reverse()
                return result
            from2 = list2.pop(-1)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# DD: Modified to print input value if supplied
def test(got, expected, in_list=None):
    for_input = '' if in_list is None else 'for input=' + repr(in_list)

    if got == expected:
        print ' OK  %s got: %s' % (for_input, repr(got))

    else:
        print '  X  %s got: %s expected: %s' % (for_input, repr(got), repr(expected))


def test_remove_adjacent(in_list, expected):
    test(remove_adjacent(in_list), expected, in_list)


def test_linear_merge(list1, list2, expected):
    print
    print 'list1=', list1
    print 'list2=', list2

    list1A = copy_of(list1)
    list2A = copy_of(list2)

    print 'merge_lists()'
    test(merge_lists(list1, list2), expected)
    print 'linear_merge()'
    test(linear_merge(list1A, list2A), expected)


def copy_of(alist):
    result = []
    result.extend(alist)
    return result


# Calls the above functions with interesting inputs.
def main():
    print 'remove_adjacent'
    test_remove_adjacent([1, 2, 2, 3], [1, 2, 3])
    test_remove_adjacent([2, 2, 3, 3, 3], [2, 3])
    test_remove_adjacent([], [])

    print
    print 'linear_merge'
    test_linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'],
                      ['aa', 'bb', 'cc', 'xx', 'zz'])
    test_linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'],
                      ['aa', 'bb', 'cc', 'xx', 'zz'])
    test_linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'],
                      ['aa', 'aa', 'aa', 'bb', 'bb'])

    test_linear_merge(['aa', 'bb', 'cc'], ['xx', 'yy', 'zz'],
                      ['aa', 'bb', 'cc', 'xx', 'yy', 'zz'])
    test_linear_merge(['xx', 'yy' 'zz'], ['aa', 'bb', 'cc'],
                      ['aa', 'bb', 'cc', 'xx', 'yy' 'zz'])

    test_linear_merge([], [], [])
    test_linear_merge([], ['aa', 'bb', 'cc'], ['aa', 'bb', 'cc'])
    test_linear_merge(['aa', 'bb', 'cc'], [], ['aa', 'bb', 'cc'])


if __name__ == '__main__':
    main()
