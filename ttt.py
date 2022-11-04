from tkinter import *
import tkinter as tk


class Thegame:

    def __init__(self):
        window = tk.Tk()
        game_frame = tk.Frame(master=window)
        game_frame.grid_rowconfigure(3, weight=1)
        game_frame.grid_columnconfigure(3, weight=1)

        #create the individual buttons
        b1 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b1))
        b2 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b2))
        b3 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b3))
        b4 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b4))
        b5 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b5))
        b6 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b6))
        b7 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b7))
        b8 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b8))
        b9 = Button(game_frame, text="", height=5, width=6, command=lambda: self.showprops(b9))

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

        game_frame.pack()
        window.mainloop()

    def showprops(self, button):
        print(button["text"])
        #has not been clicked
        if(button["text"] == ""):
            button["text"] = "X"
            #check if win

        else:
             print("already active!")
    def check_game(self):
        pass

Thegame()


