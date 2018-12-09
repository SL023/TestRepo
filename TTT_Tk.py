from tkinter import *
import tkinter.messagebox
import tkinter.font

played = [False, False, False, False, False, False, False, False, False]
click = True
tk = Tk()
tk.title("Tic Tac Toe")
button_width = 16
button_height = 8
button_colour = "light green"

width_of_window = 600
height_of_window = 580

screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)

tk.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))


def play(buttons):
    global click
    global played
    global button_colour
    if buttons["text"] == " " and click is True:
        buttons["text"] = "X"
        click = False
        win()
        b_full()
    elif buttons["text"] == " " and click is False:
        buttons["text"] = "O"
        click = True
        win()
        b_full()


def win():
    if button1["text"] == button2["text"] == button3["text"] == "X" or \
        button4["text"] == button5["text"] == button6["text"] == "X" or \
        button7["text"] == button8["text"] == button9["text"] == "X" or \
        button1["text"] == button4["text"] == button7["text"] == "X" or \
        button2["text"] == button5["text"] == button8["text"] == "X" or \
        button3["text"] == button6["text"] == button9["text"] == "X" or \
        button1["text"] == button5["text"] == button9["text"] == "X" or \
            button3["text"] == button5["text"] == button7["text"] == "X":
            tkinter.messagebox.showinfo("Winner", " Player X you have won")
            restart()

    elif button1["text"] == button2["text"] == button3["text"] == "O" or \
        button4["text"] == button5["text"] == button6["text"] == "O" or \
        button7["text"] == button8["text"] == button9["text"] == "O" or \
        button1["text"] == button4["text"] == button7["text"] == "O" or \
        button2["text"] == button5["text"] == button8["text"] == "O" or \
        button3["text"] == button6["text"] == button9["text"] == "O" or \
        button1["text"] == button5["text"] == button9["text"] == "O" or \
            button3["text"] == button5["text"] == button7["text"] == "O":
            tkinter.messagebox.showinfo("Winner", " Player O you have won")
            restart()


def restart():
    global click
    restart1 = tkinter.messagebox.askquestion("Restart", "Would you like to restart?")
    if restart1 == "yes":
        if click is False:
            click = True
        button1["text"] = " "
        button2["text"] = " "
        button3["text"] = " "
        button4["text"] = " "
        button5["text"] = " "
        button6["text"] = " "
        button7["text"] = " "
        button8["text"] = " "
        button9["text"] = " "
        played[0] = False
        played[1] = False
        played[2] = False
        played[3] = False
        played[4] = False
        played[5] = False
        played[6] = False
        played[7] = False
        played[8] = False
    elif restart1 == "no":
        tk.quit()


def b_full():
    global played
    if button1["text"] != " ":
        played[0] = True
    if button2["text"] != " ":
        played[1] = True
    if button3["text"] != " ":
        played[2] = True
    if button4["text"] != " ":
        played[3] = True
    if button5["text"] != " ":
        played[4] = True
    if button6["text"] != " ":
        played[5] = True
    if button7["text"] != " ":
        played[6] = True
    if button8["text"] != " ":
        played[7] = True
    if button9["text"] != " ":
        played[8] = True

    if played[0] == played[1] == played[2] == played[3] == played[4] == played[5] == played[6] == played[7] == \
            played[8] is True:
        tkinter.messagebox.showinfo("Draw", "You have both drawn")
        restart()


helv = tkinter.font.Font(family="Helvetica", size=14, weight="bold")
button1 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button1))
button1.grid(row=1, column=0)
button2 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button2))
button2.grid(row=1, column=1)
button3 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button3))
button3.grid(row=1, column=2)
button4 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button4))
button4.grid(row=2, column=0)
button5 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button5))
button5.grid(row=2, column=1)
button6 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button6))
button6.grid(row=2, column=2)
button7 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button7))
button7.grid(row=3, column=0)
button8 = Button(tk, text=" ", bg=button_colour, font=helv, height=button_height, width=button_width, command=lambda: play(button8))
button8.grid(row=3, column=1)
button9 = Button(tk, text=" ", bg=button_colour, font=helv, height=8, width=button_width, command=lambda: play(button9))
button9.grid(row=3, column=2)


tk.mainloop()
