# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import turtle 
from random import randint

t1=turtle.Turtle()

t1.speed(15)
t1.penup()
t1.goto(-140,140)

for steps in range(11):
    t1.write(steps,align='center')
    t1.right(90)
    t1.forward(10)
    t1.pendown()
    t1.forward(150)
    t1.penup()
    t1.backward(160)
    t1.left(90)
    t1.forward(20)
    
ada=turtle.Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

bob=turtle.Turtle()
bob.color('green')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

cc=turtle.Turtle()
cc.color('yellow')
cc.shape('turtle')

cc.penup()
cc.goto(-160,40)
cc.pendown()

dog=turtle.Turtle()
dog.color('gray')
dog.shape('turtle')

dog.penup()
dog.goto(-160,10)
dog.pendown()

for turn in range(90):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    cc.forward(randint(1,5))
    dog.forward(randint(1,5))

    
turtle.done()