from tkinter import *


# function to show the dice character
def show_dice(labelname, objectname1, objectname2, secondlabel, text):
    dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    result1 = objectname1.roll_dice()
    result2 = objectname2.roll_dice()
    labelname.config(text=dice[result1] + dice[result2])

    # if double dice is rolled then update Label and congratulates player
    def update_label(secondlabel, text):
        secondlabel.config(text=text)

    if result1 == result2:
        update_label(secondlabel, text)
    else:
        update_label(secondlabel, '')


# function to change dice color
def change_color(col, name, place):
    current = name.cget('fg')
    name.config(fg=col)
    place.update()

# Function to create button
def btn_creation(x: int, btn_name, emplacement, text, bg, fg, command, posx: int, posy: int, intervalX: int, intervalY: int):
    for btn_name in range(x):
        btn_name = Button(emplacement, text=text, bg=bg, fg=fg, command=command)
        btn_name.pack()
        btn_name.place(x=str(posx), y=str(posy))
        posx += intervalX
        posy += intervalY
