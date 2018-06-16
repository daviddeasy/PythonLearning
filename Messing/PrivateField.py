class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email
        self.__private_name = 'old_private_name'

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email

    def private_name(self):
        return self.__private_name


def main():
    p = Person('david', 'old@email')
    print 'name:', p.first_name, ', _email:', p._email, ', private_name():', p.private_name()
    p._email = 'NEW@email'
    print 'after assigning to "protected" p._email:'
    print '_email:', p._email

    # AttributeError thrown if you try to access p.__private_name before assigning to it
    # See description of "name mangling" in python documentation for Classes
    # print '__private_name:', p.__private_name

    # The next line defines a NEW field called __private_name
    # - NOT the same as (name mangled) __private_name field defined in the constructor
    p.__private_name = 'NEW_private_name'
    print 'after assigning to "private" p.__private_name:'
    print '__private_name:', p.__private_name
    print 'private_name():', p.private_name()
    


if __name__ == '__main__': main()
