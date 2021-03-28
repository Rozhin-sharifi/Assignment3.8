import turtle


def draw(t, size, j):
   for i in range(j):
        t.forward(size)
        t.left(360/j)

wn = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
dis = 1

for i in range(2, 11):
    
    draw(t, dis,i)
    dis += 20
    t.penup()
    t.backward(10)
    t.right(360/i)
    t.forward(10)
    t.left(360/i)
    t.pendown()