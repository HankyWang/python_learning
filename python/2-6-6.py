from __future__ import division
class rational(object):
    def __init__(self,p,q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return self.p / self.q
print int(rational(1,2))
print float(rational(1,2))