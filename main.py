from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    tim = Turtle()
    tim.color("white")
    tim.shape("square")
    tim.goto(position)

screen.exitonclick()
