def format(s):
    return s[0].upper()+s[1::].lower()
class student(object):
    __slot__=['name','gender','age','score']
    def __init__(self,name,gender,age,score):
        self.name = format(name)
        self.gender = format(gender)
        self.age = age
        self.score =score
    def __cmp__(self,s):
        if self.score < s.score:
            return 1
        else :
            return -1
        if self.name < s.name:
            return 1
        else :
            return -1
    def __str__(self):
        return '(%s:%s, %d, %d)' %(self.name,self.gender,self.age,self.score)
    __repr__=__str__
tom = student('Tom', 'male', 17, 99)
cassy = student('CASSY', 'feMale', 18, 80)
apolo = student('apolo','Male', 18, 80)
print sorted([tom,cassy,apolo])