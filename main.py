import turtle
import pandas
import numpy
from turtle import Turtle,Screen
screen=Screen()
screen.title("U.S. States Game")
t=Turtle()
t.penup()
image="us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("us-states-game-start/50_states.csv")
states_list=list(data["state"])

for state in states_list:
    answer=screen.textinput(title="Guess the state",prompt="What's another state name?").title()
    if answer in states_list:
        state_name=data[data["state"]==answer]
        xcor=state_name.x.values[0]
        ycor=state_name.y.values[0]
        t.goto(xcor,ycor)
        t.write(answer,align="center",font="24")
        
t.hideturtle()
   
    
























turtle.mainloop()
screen.exitonclick()