from tkinter import *
import tkinter.messagebox
import tkinter as tk

class Game:
    current_player = ""
    counter = 0

    def __init__(self):
        #Set up the GUI
        self.window = tk.Tk()
        self.game_frame = tk.Frame(master=self.window)
        self.game_frame.grid_rowconfigure(3, weight=1)
        self.game_frame.grid_columnconfigure(3, weight=1)

        #create the players
        Game.current_player = "X"
        self.buttons = []
        #create the individual buttons
        the_height = 20
        the_width = 30
        self.b1 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b1))
        self.b2 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b2))
        self.b3 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b3))
        self.b4 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b4))
        self.b5 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b5))
        self.b6 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b6))
        self.b7 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b7))
        self.b8 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b8))
        self.b9 = Button(self.game_frame, text="", height=the_height, width=the_width, command=lambda: self.showmove(self.b9))

        self.row1 = []
        self.b1.grid(row=0, column=0)
        self.row1.append(self.b1)
        self.b2.grid(row=0, column=1)
        self.row1.append(self.b2)
        self.b3.grid(row=0, column=2)
        self.row1.append(self.b3)
        self.buttons.append(self.row1)

        row2 = []
        self.b4.grid(row=1, column=0)
        row2.append(self.b4)
        self.b5.grid(row=1, column=1)
        row2.append(self.b5)
        self.b6.grid(row=1, column=2)
        row2.append(self.b6)
        self.buttons.append(row2)

        row3 = []
        self.b7.grid(row=2, column=0)
        row3.append(self.b7)
        self.b8.grid(row=2, column=1)
        row3.append(self.b8)
        self.b9.grid(row=2, column=2)
        row3.append(self.b9)
        self.buttons.append(row3)

        self.game_frame.pack()
        self.window.mainloop()

    def compMove(self):
        flag = 0
        for col in range(3):
            for row in range(3):
                if self.buttons[col][row]["text"] == "":
                    self.buttons[col][row]["text"] = "O"
                    Game.counter = Game.counter + 1
                    self.checkEnd( col, row)
                    self.switchPlayer()
                    flag = 1
                    break
            if flag:
                break

    def showmove(self, button):
        if(button["text"] == ""):
            button["text"] = Game.current_player
            Game.counter = Game.counter + 1
            self. checkEnd(button.grid_info()['row'], button.grid_info()['column'])
            self.switchPlayer()
            if(Game.current_player=="O"):
                self.compMove()
        else:
             print("already active!")

    def switchPlayer(self):
        if(Game.current_player == "X"):
            Game.current_player = "O"
        else:
            Game.current_player = "X"

    def checkEnd(self, row, col):
        # if all buttons have been played
        if (Game.counter == 9):
            print("Game Over")
        #check for horizontal win
        if(self.horizontalWin(col, row) == True):
            print("horizontal win!")
            self.announceEnd()
            #self.window.destroy()
        #check for vertical win
        elif(self.verticalWin(col, row) == True):
            print("vertical win!")
            self.announceEnd()
            #self.window.destroy()
        #check for diagonal win
        elif(self.diagonalWin(col, row) == True):
            print("diagonal Win")
            self.announceEnd()
            #self.window.destroy()
        else:
            print("no win")

    def announceEnd(self):
        message = "the winner is: " + Game.current_player
        tkinter.messagebox.showinfo("Winner! ", message)
        self.window.destroy()

    def horizontalWin(self, col, row):
        if(col==0):
            if(self.buttons[row][1]["text"] == self.buttons[row][0]["text"]):
                if(self.buttons[row][2]["text"] == self.buttons[row][0]["text"]):
                    return True
        elif(col==1):
            if (self.buttons[row][0]["text"] == self.buttons[row][1]["text"]):
                if (self.buttons[row][2]["text"] == self.buttons[row][1]["text"]):
                    return True
        elif(col ==2):
            if (self.buttons[row][0]["text"] == self.buttons[row][2]["text"]):
                if (self.buttons[row][1]["text"] == self.buttons[row][2]["text"]):
                    return True
        return False

    def verticalWin(self, col, row):
        if (row == 0):
            if (self.buttons[1][col]["text"] == self.buttons[0][col]["text"]):
                if (self.buttons[2][col]["text"] == self.buttons[0][col]["text"]):
                    return True
        elif (row == 1):
            if (self.buttons[0][col]["text"] == self.buttons[1][col]["text"]):
                if (self.buttons[2][col]["text"] == self.buttons[1][col]["text"]):
                    return True
        elif (row== 2):
            if (self.buttons[1][col]["text"] == self.buttons[0][col]["text"]):
                if (self.buttons[2][col]["text"] == self.buttons[0][col]["text"]):
                    return True
        return False
    def diagonalWin(self, col, row):
        if(col == 0):
            if(row == 0):
                if(self.buttons[1][1]["text"] ==self.buttons[0][0]["text"]):
                    if(self.buttons[2][2]["text"] == self.buttons[0][0]["text"]):
                        return True
            elif(row == 2):
                if (self.buttons[1][1]["text"] == self.buttons[2][0]["text"]):
                    if (self.buttons[0][2]["text"] == self.buttons[2][0]["text"]):
                        return True
        elif(col == 2):
            if(row==0):
                if (self.buttons[1][1]["text"] == self.buttons[0][2]["text"]):
                    if (self.buttons[2][0]["text"] == self.buttons[0][2]["text"]):
                        return True
            elif(row==2):
                if (self.buttons[1][1]["text"] == self.buttons[2][2]["text"]):
                    if (self.buttons[0][0]["text"] == self.buttons[2][2]["text"]):
                        return True
        elif(col == 1 and row==1):
                if (self.buttons[0][0]["text"] == self.buttons[1][1]["text"]):
                    if (self.buttons[2][2]["text"] == self.buttons[1][1]["text"]):
                        return True
                else:
                    if (self.buttons[0][2]["text"] == self.buttons[1][1]["text"]):
                        if (self.buttons[2][0]["text"] == self.buttons[1][1]["text"]):
                            return True
        else:
            return False




game = Game()



