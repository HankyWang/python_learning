class student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
x = student('Lisa', 99)
try :
    print x.__score
except:
    print '?'