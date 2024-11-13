import math
import turtle as tr
import numpy as np
import sys
import os
import phonenumbers
from phonenumbers import geocoder
import socket
import threading
import time


class Caculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def multi(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    def div2(self,x,y):
        return x//y
    def square(self,x,y):
        return x**y
    def sqroot(self,x):
        return math.sqrt(x)
    def sin(self,x):
        y=math.radians(x)
        return math.sin(y)
    def cos(self,x):
        y=math.radians(x)
        return math.cos(y)
    def tan(self,x):
        y=math.radians(x)
        return math.tan(y)
    def log(self,x):
        return math.log(x)
    def log10(self,x):
        return math.log10(x)
    def pytagor(self,x,y):
        return math.sqrt(x**2+y**2)
    def boolean(self,x,y):
        if x%2==0 or y%2==0:
            return True
        else:
            return False
    def phonumberchecker(self,ch_number,number):
        ch_number=phonenumbers.parse(number,"CH")
        return geocoder.description_for_number(ch_number,"en")
    def tyrangle_area(self,x,h):
        return (x*h)/2
    def tryangle(self,x):
        for i in range(3):
            tr.forward(x)
            tr.right(x)
    def square(self,x):
        for i in range(4):
            tr.forward(x)
            tr.right(90)
    def rectangle(self,x,y):
        for i in range(4):
            tr.forward(x)
            tr.right(90)
            tr.forward(y)
            tr.right(90)            
    def circle(self,x):
        tr.circle(x)
    def speed(self,x,s,t):
        x=s/t
        return x 
    def port_scaner(self,x):
        pass
    def ddos_tool(self):
        pass
    def keylogger(self):
        pass
    def socket_testing(x):
        x=socket.gethostbyname('google.com')
        print(x)
        

    

        
    

tutorial={
    "1":"add",
    "2":"sub",
    "3":"multi",
    "4":"divisor",
    "5":"divisor2",
    "6":"square",
    "7":"square root",
    "8":"sin",
    "9":"cos",
    "10":"tan",
    "11":"log",
    "12":"log10",
    "13":"pytargor",
    "14":"boolean",
    "15":"phone_number_checker",
    "16":"tryangle area",
    "17":"tryangle",
    "18":"rectangle",
    "19":"circle",
    "20":"anyshape",
    "21":"speed",
    "22":"port scanner",
    "23":"ddos tool",
    "24":"keylogger",
    "25":"socket testing"

}
print("  ____ _____    ____  __ __|  | _____ _/  |_  ___________    _________.__. _______/  |_  ____   _____")
print(" _/ ___\\__  \ _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \  /  ___<   |  |/  ___/\   __\/ __ \ /     \ ")
print(" \  \___ / __ \\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/  \___ \ \___  |\___ \  |  | \  ___/|  Y Y  \ ")
print(" \___  >____  /\___  >____/|____(____  /__|  \____/|__|    /____  >/ ____/____  > |__|  \___  >__|_|  /")
print("     \/     \/     \/                \/                         \/ \/         \/            \/      \/ ")
print("we got +,-,*,/,//,square,sqrt(square root),sin,cos,tan,log,log10,pytargor and boolean,and now here is tutorial:")
print(tutorial)
while True:
    for i in range(1,26):
        print(i)
    cac=Caculator()
    user=int(input("enter your option here user:"))
    x=float(input("enter number of x here:"))
    y=float(input("enter number of y here:"))
    s=float(input("enter s"))
    t=float(input("enter t"))
    number=input("enter ur phone number here")

    if user==1:
        print(cac.add(x,y))
    elif user==2:
        print(cac.sub(x,y))
    elif user==3:
        print(cac.multi(x,y))
    elif user==4:
        print(cac.div(x,y))
    elif user==5:
        print(cac.div2(x,y))
    elif user==6:
        print(cac.square(x,y))
    elif user==7:
        print(cac.sqroot(x,y))
    elif user==8:
        print(cac.sin(x))
    elif user==9:
        print(cac.cos(x))
    elif user==10:
        print(cac.tan(x))
    elif user==11:
        print(cac.log(x))
    elif user==12:
        print(cac.log10(x))
    elif user==13:
        print(cac.pytagor(x,y))
    elif user==14:
        print(cac.boolean(x,y))
    elif user==15:
        print(cac.phonumberchecker(number))
    elif user==16:
        print(cac.tryrangle_area(x,y))
    elif user==17:
        print(cac.tryrangle(x))
    elif user==18:
        print(cac.rectangle(x,y))
    elif user==19:
        print(cac.circle(x))
    elif user==20:
        print(cac.anyshape(x))
    elif user==21:
        print(cac.speed(x))
    elif user==22:
        print(cac.port_scaner(x))
    elif user==23:
        print(cac.ddos_tool(x))
    elif user==24:
        print(cac.keylogger(x))
    elif user==25:
        print(cac.socket_testing(x))
    else:
        print("error,try again,is not in a option lil bro")
    print("continue?Y/n")
    ans=input().lower()
    if ans=="n":
        print("see ya next time")
        break




