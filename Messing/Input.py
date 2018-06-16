def main():
    # print "How old are you?",
    age = raw_input("How old are you? ")
    print "How tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()

    print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


if __name__ == '__main__':
    main()
