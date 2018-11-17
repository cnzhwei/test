from turtle import *

##正方型螺旋线

penup()
fd(-100)
seth(-90)
fd(100)
seth(0)
pendown()
r = 200
d = 4   ##每次减少距离
while r >= 0:
    seth(90)
    fd(r-d)
    r=r-d
    seth(0)
    fd(r-d)
    r=r - d
    seth(-90)
    fd(r-d)
    r=r-d
    seth(0)
    fd(d-r)
    r=r-d