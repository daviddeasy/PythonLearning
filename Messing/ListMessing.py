
def test(iterable, cmp=None, key=None, reverse=False):
    print iterable, cmp, key, reverse

def main():

    a = [2, 3, 1, 5, 4]

    print 'sorted(a):', sorted(a)

    print 'sorted(a, reverse=True)', sorted(a, reverse=True)

    print 'test(a)'
    test(a)

    print 'test(a,reverse=True)'
    test(a, reverse=True)

    print "test(a, key='MickeyMouse')"
    test(a, key='MickeyMouse')

    print "test(a, reverse='Mickey')"
    test(a, reverse='Mickey')

    print "test(a, reverse=5, key='key', cmp='cmp')"
    test(a, reverse=5, key='key', cmp='cmp')


if __name__ == '__main__':
    main()