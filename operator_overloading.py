class Complex_Number:
    def __init__(self,r,i):
        self.r=r
        self.i=i
c1=Complex_Number(1,2)
c2=Complex_Number(4,5)
print(c1+c2)
#TypeError: unsupported operand type(s) for +: 'Complex_Number' and 'Complex_Number'
class Complex_Number:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,other):
        return f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
#return str(self.real+other.real)+ "+" + str(self.imaginary+other.imaginary)+"i"
c1=Complex_Number(1,2)
c2=Complex_Number(4,5)
print(c1+c2)
 #overloading greater than operator
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False
p1=Person("Likhitha",21)
p2=Person("Rithik",10)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")