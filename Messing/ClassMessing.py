
class MyClass:
    a = 5
    # b = 0

    def __init__(self, b=0):
        self.b = b
        print 'constructor:'
        print 'a=' + str(self.a)
        print 'b=' + str(self.b)

    def test_fields(self):
        print 'test_fields:'
        print 'a=' + str(self.a)
        print 'b=' + str(self.b)
        print 'In Myclass.test_fields(): __name__=' + __name__


def main():
    print '\nEntered main()'

    print '\nMyClass(3):'
    my_object = MyClass(3)
    my_object.test_fields()

    print '\nMyClass():'
    my_object = MyClass()
    my_object.test_fields()


if __name__ == '__main__':
    main()

