class student:
    def __init__(self, name):
        self.name = name

s1 = student("azeem")

del s1  # s1 is not defined

print(s1.name)