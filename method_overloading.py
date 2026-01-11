class Demo:
    def add(self,a,b):
        return a+b
a=Demo()
print(a.add(2,3))


class Demo:
    def add(self,a,b,c=0):
        return a+b+c
a=Demo()
print(a.add(2,3))
print(a.add(2,3,4))


class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total+=i
        return total
a=Demo()
print(a.add(2,3,4))
print(a.add(3,4,5,3,2,1))