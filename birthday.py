import turtle
import random

screen=turtle.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("恭喜你正式比我大一岁咯！")

class Firework:
    def __init__(self):
        self.t=turtle.Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(random.randint(-350,350),random.randint(-250,250))
        self.t.pendown()
        self.t.color(random.random(),random.random(),random.random())

    def explode(self):
        for _ in range(30):
            length=random.randint(20,100)

            self.t.setheading(random.randint(0,360))
            self.t.forward(length)
            self.t.backward(length)

for _ in range(10):
    firework=Firework()
    firework.explode()

pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,-200)
pen.color("white")
pen.write("生日快乐！",align="center",font=("Arial",24,"normal"))

turtle.done()




