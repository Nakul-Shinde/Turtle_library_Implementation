

from turtle import Turtle,Screen

timmy=Turtle()
timmy.shape('turtle')
timmy.color('#DC143C')
timmy.pencolor('blue')
timmy.pensize(3)


i=0
while i!=10:
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)
    i+=1


screen=Screen()
screen.exitonclick()

#-----------------------------------------------------------------------------



from turtle import Turtle,Screen


colors=['#DC143C','#FFD700','#8A2BE2','#FF1493','#00FF00','#0000FF','#C71585','#000000']
timmy=Turtle()
timmy.shape('turtle')
timmy.color('#DC143C')
timmy.pencolor('blue')
timmy.pensize(3)



        
for i in range(3,11):        
    for j in range(1,i+1):
        timmy.color(colors[i-3])
        timmy.forward(50)
        timmy.left(360/i)
        timmy.forward(50)
           
    
  
screen=Screen()
screen.exitonclick()


#-----------------------------------------------------------------------------
import random
from turtle import Turtle,Screen

colors=['#DC143C','#FFD700','#8A2BE2','#FF1493','#00FF00','#0000FF','#C71585','#000000']
timmy=Turtle()
timmy.shape('turtle')
timmy.color('#DC143C')
timmy.pencolor('blue')
timmy.pensize(10)

for i in range(0,110): 
    val=random.randint(1,4)
    val_color=random.choice(colors)
    if val==1:
        timmy.color(val_color)
        timmy.forward(15)
        timmy.speed(0)
    elif val==2:
        timmy.color(val_color)
        timmy.backward(15) 
        timmy.speed(0)
    elif val==3:
        timmy.color(val_color)
        timmy.left(90) 
        timmy.forward(15)
        timmy.speed(0)

    else:
        timmy.color(val_color)
        timmy.right(90)
        timmy.forward(15)
        timmy.speed(0)


screen=Screen()
screen.exitonclick()

#--------------------------------------------------------------------------------

import random
from turtle import Turtle,Screen

colors=['#DC143C','#FFD700','#8A2BE2','#FF1493','#00FF00','#0000FF','#C71585','#000000']
angle=[0,90,180,270,360,0,90,180,270,360]

timmy=Turtle()
timmy.shape('turtle')
timmy.color('#DC143C')
timmy.pencolor('blue')
timmy.pensize(10)

def random_turtle(val_color,random_angle):
    timmy.color(val_color)
    timmy.left(random_angle)
    timmy.speed(0)
    timmy.forward(30)


for i in range(0,110):
    val_color=random.choice(colors)
    random_angle=random.choice(angle)
    random_turtle(val_color,random_angle)

screen=Screen()
screen.exitonclick()