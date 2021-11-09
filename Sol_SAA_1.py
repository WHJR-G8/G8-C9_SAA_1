import turtle
import random

colors = ["red","green","black","blue","yellow","grey","cyan","orange"]
radius = 20

def draw_circle():
    turtle.fillcolor(random.choice(colors))
    turtle.begin_fill()
    turtle.stamp()
    turtle.circle(radius)
    turtle.end_fill()
    
for i in range(3):
    while radius >= 40:
        radius += 10
        draw_circle()
        break
    radius += 20
    draw_circle()
