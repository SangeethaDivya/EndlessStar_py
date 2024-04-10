import turtle
col=('yellow','red','green','blue','pink','orange')
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(40)
for i in range(200):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(200)
    t.width(2)
   # t.stamp()
