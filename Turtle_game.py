# turtle race
from turtle import *
from random import randint

wn=Screen()
wn.bgcolor("lightgreen")

penup()
goto(-200,200)

step=0
for step in range(20):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(130)
    penup()
    backward(140)
    left(90)
    forward(25)
clr =["red","blue","yellow","black"]
turt=[]
y=170
for i in range(4):
    turt.append(Turtle())
    turt[i].color(clr[i])
    turt[i].shape("turtle")
    turt[i].penup()
    turt[i].goto(-220,y)
    y-=30
a=("winner")
goto(0,-10)
write(a)
a1=0
a2=0
a3=0
a4=0
    
for turn in range(180):
    r=randint(1,5)
    b=randint(1,5)
    y=randint(1,5)
    bl=randint(1,5)
    turt[0].forward(r)
    turt[1].forward(b)
    turt[2].forward(y)
    turt[3].forward(bl)
    a1+=r
    a2+=b
    a3+=y
    a4+=bl    
    
    if a1>=500:
        turt[0].goto(0,10)
        break
    elif a2>=500:
        turt[1].goto(0,10)
        break
    elif a3>=500:
        turt[2].goto(0,10)
        break
    elif a4>=500:
        turt[3].goto(0,10)
        break
turtle.done("done")
