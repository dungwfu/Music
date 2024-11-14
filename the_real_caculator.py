import math
import turtle as tur

class just_a_simple_caculator:
    def caculate(self,x,y): #1
        return x+y
    def sub(self,x,y):#2
        return x-y
    def multi(self,x,y):#3
        return x*y
    def divisor(self,x,y):#4
        return x/y
    def divisors(self,x,y):
        return x//y#5
    def square(self,x,y):
        return x**y#6
    def square_root(self,x):
        return math.sqrt(x)
    def Sin(self,x,y):
        y=math.radians(x)
        return math.cos(y)
    def Cos(self,x,y):
        y=math.radians(x)
        return math.cos(y)
    def Tan(self,x,y):
        y=math.radians(x)
        return math.tan(y)
    def logarit(self,x):
        return math.log(x)
    def logarit10(self,x):
        return math.log10(x)
    def divisorss(self,x,y):
        if x%y==0:
            return True
        return False
    def pythagor(self,x,y,z): 
        xs=x**2
        ys=y**2
        z**2==xs+ys
        return z**2
    def pythagors(self,x,y):
        return math.sqrt(x**2+y**2)
    def boolean1(self,x,y,z):
        if x*y==z:
            return True
        return False
    def boolean2(self,x,y,z):
        if x+y==z:
            return True
        return False
    def radian(self,x,y):
        x_rad=math.radians(x)
        y_rad=math.radians(y)
        return (y*math.sin(x_rad))/x
    # area moment
    def tryangle(self,x,y):#x la day y la chieu cao
        return x*y/2
    def retengle(self,x,y):
        return x*y#x chieu dai y la chieu rong hoac co the nguoc lai
    def trapezoid(self,x,y,z):
        return (x+y)/2*z
    def real_square(self,x):
        return x*x
    def circle(self,x):
        return math.pi*(x**2)
    def parallelogram(self,x,y):
        return x*y
    def roundingnumber(self,x):
        return round(x)
    def decimal_to_binary(self,x):
        return int(bin(x)[2:])
    def bin_to_decimal(self,x):
        return int(x,2)
    def primechecker(self,x):
        if x >1:
            return False
        for i in range(2,(x//2)+1):
            if x%i==0:
                return False
            else:
                return True
    def drawingtryange(self,x):
        
            for i in range(x*4):
                tur.forward(i*8)
                tur.right(120)
    def realtryangle(self,x):
        for i in range(x,2):
            tur.forward(x)
            tur.right(120)
    def retuangle(self,x):
        for i in range(4):
            tur.forward(x)
            tur.right(90)
    def anyshape(self,x):
        

Cac=just_a_simple_caculator()
x=int(input("enter x"))
y=int(input("enter y"))
z=int(input("enter z"))
print("1")
print("2")  
print("3")
print("4")
print("5")
print("6")
print("7")
print(Cac.anyshape(x,y))


