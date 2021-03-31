import turtle
kt = turtle.Turtle()
kt.speed(10)


kt.getscreen().bgcolor("cyan")

for i in range(80):
   kt.pensize(30)
   kt.pencolor("brown")
   kt.goto(0,-300)

kt.penup()
kt.goto(0,0)
kt.pendown()

for i in range(19):
   kt.pensize(10)
   kt.pencolor("green")
   kt.goto(200,85)
   kt.forward(50)
   kt.left(20)
kt.penup()
kt.goto(0,0)
kt.pendown()

for i in range(30):
   kt.pensize(10)
   kt.pencolor("green")
   kt.goto(-200,185)
   kt.forward(100)
   kt.left(50)

kt.penup()
kt.goto(0,0)
kt.pendown()



for i in range(30):
   kt.pensize(5)
   kt.pencolor("green")
   kt.speed(10)
   kt.goto(60,200)
   kt.circle(50)
   
   kt.right(30)
   kt.penspeed(10)
  
turtle.done()

