import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
image = "img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
        
    answer_state = screen.textinput(title = f"{guessed_states}/50 correct!",prompt = "What state's name do you know?").title()
    print(answer_state)
    
    if(answer_state == "Exit"):
        break
    
    if(answer_state in all_states):
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

# Learn missed states
missed_states = []
for missed_state in all_states:
    if missed_state not in guessed_states:
        missed_states.append(missed_state)

new_data = pandas.DataFrame(missed_states)
new_data.to_csv("States_to_learn.csv")















#
# #print(usa_states["state"][1])
# #print(type(usa_states["state"]))
# count = 0
# for i in usa_states["state"]:
#     if(answer_state == i):
#         print(usa_states["x"][count])
#         print(usa_states["y"][count])
#     count +=1
# turtle.goto(usa_states["x"][count], usa_states["y"][count])
   
#print(usa_states["state"] == "Alabama")















screen.exitonclick()


