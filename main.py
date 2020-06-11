import tkinter as tk
from Dice import *
from function import *



# declaration main window and main frame
rootWindow = tk.Tk()
rootWindow.title('Dice Roll')
rootWindow.geometry('600x500')
frame = Frame(rootWindow, bg="#313131", width=600, height=500)
frame.pack()


# Declaration of the dice
dice1 = Dice('cube', 5)
dice2 = Dice('cube', 5)

# creation dice Label to show dice
diceLabel = Label(frame, text='', font=('Helvetica', 200), bg="#313131", fg="white")
diceLabel.pack()
diceLabel.place(x="100", y="150")

doubleDiceLabel = Label(frame, text="", font=('Helvetica', 23), bg="#313131", fg='white')
doubleDiceLabel.pack()
doubleDiceLabel.place(x="130", y="50")


# btn to roll the dice
btnRoll = Button(frame, text='Roll the dice!', font=("Helvetica", 15), bg='#2AB859', fg="white",
                 command=lambda: show_dice(diceLabel, dice1, dice2, doubleDiceLabel, "Nice, you rolled a double!!"))
btnRoll.pack()
btnRoll.place(x="250", y="10")


rootWindow.mainloop()
