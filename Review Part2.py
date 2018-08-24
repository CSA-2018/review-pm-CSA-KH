class Person:
    def __init__(self, un, a, c, pn):
        self.UserName = un
        self.Age = a
        self.City = c
        self.PhoneNumber = pn

    def __str__(self):  #__str__ can only return, cant pring
        UN = self.UserName
        A = self.Age
        C = self.City
        PH = self.PhoneNumber
        return('%s is %s years old and lives in %s. His/Her phone number is %s' % (UN, A, C, PH))


def uac():
    u = input('What is your username ')
    a = input('What is your age ')
    c = input('What is your city ')
    p = PhoneN()
    P1 = Person(u, a, c, p)
    print(P1)



def PhoneN():
    while True:
        
        try:
            phone = int(input('What is your phone number '))
            if len(str(phone)) != 10:
                print('You did not input a valid phone number')
                PhoneN()
            else:
                return phone
        except ValueError:
            print('You did not input a valid phone number')



uac()
