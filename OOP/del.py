class student:
    def __init__(self, name):
        self.name = name

s1 = student("azeem")

del s1  # s1 is not defined

print(s1.name)

'''
Private(like)
Private __attributes and __methods are meant
to be used only within the class and are
not accessible from outside the class
'''

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass      # private attribute
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("123", "abc")
print(acc1.acc_no)
acc1.reset_pass()