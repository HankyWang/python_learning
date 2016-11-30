def gcd(a, b) :
    if b == 0 :
        return a
    else :
        return gcd(b, a % b)

class rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, s):
        return rational(self.p * s.q + self.q * s.p, self.q * s.q)
    def __sub__(self,s):
        return rational(self.p * s.q - self.q * s.p, self.q * s.q)
    def __mul__(self,s):
        return rational(self.p * s.p, self.q * s.q)
    def __div__(self,s):
        return rational(self.p * s.q, self.q * s.p)
    def __str__(self):
        k = gcd(self.p,self.q)
        return '%d/%d' %(self.p / k, self.q / k)
    __repr__=__str__

r1 = rational(1,2)
r2 = rational(1,4)

print r1+r2
print r1-r2
print r1 * r2
print r1 / r2


