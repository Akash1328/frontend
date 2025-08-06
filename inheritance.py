class alpha:
    def fun1(self):
        print('alpha class')
class beta(alpha):
    def fun2(self):
        print('beta class')
    

class gamma(beta):
    pass
g=gamma()
g.fun1()
g.fun2()
