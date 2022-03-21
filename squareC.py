import turtle

t = turtle.Turtle()
s =  turtle.Screen()
s.bgcolor("navyblue")
t.pencolor("white")
t.speed(0)
t.pensize(0.1)
c = 0
d = 0
while True:
    for i in range(4):
        turtle.circle
        t.forward(120)
        t.right(90)
    t.right(5)  
    c +=1
    if c>=360/5:
        t.forward(60)
        t.right(60)
        c=0
        d +=1
        if d>=6:
          break
    t.hideturtle()        
turtle.done()