print '\nTHIS IS THE FIRST LINE IN messing.py\n'

s = 'hiya'
print 's1=' + s[1]  # i
print 'len(' + s + ')=' + str(len(s))  # 2
print s + ' there'  # hi there
print s, 'there'

pi = 3.1417
# text = 'The value of pi is ' + pi      # NO, does not work
text = 'The value of pi iiii is ' + str(pi)  # yes
print 'text=', text

print 'text[1:3]=', text[1:3]
print 'text[-5:-1]=', text[-5:-1]
print 'text[-5:]=', text[-5:]
print 'text[:-5]=', text[:-5]

print 'Characters in "abcd":'
for ch in 'abcd': print ch

print 'Numbers in range(2)'
for i in range(2): print i

print 'Numbers in xrange(2)'
for i in xrange(2): print i

# print 'Out of Bounds: text[99]=' + text[99]

print text, s, text,
print text, s, text

print str(text.split('i'))

print text.split('i')[0]

print 'I'.join(text.split('i'))

print 'one=%d, two=%d, 0xff=0x%x, String=%s' % (1, 2, 0xff, 'string')

#does_not_exist()

def mytestsub():
    print 'greetings from messing.myTestSub()'


def main():
    print 'greetings from messing.main()'
    mytestsub()


print '__name__=' + __name__

print '\nTHIS IS THE LAST PRINT OUTSIDE OF A FUNCTION IN messing.py'

def just_another_function():
    print 'ENTERED just_another_function'


if __name__ == '__main__':
    main()
