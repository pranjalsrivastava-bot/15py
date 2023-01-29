from tkinter import *
from PIL import ImageTk, Image
import random

root = tk()
root.title("Dice game")
root.geometry("600x400")
root.configure(backgroud="aqua")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg")
            
player1 = Label(root, text = "Player 1", bg = "pink", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player1=2.place(relx = 0.9, rely = 0.3 , anchor = CENTER)

player_1_score_label = Label(root , bg = "green", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root , bg = "yellow", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = "orange", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5 , anchor = CENTER)

player1_score = 0
def player1():
    global player1_score
    random_no = randome.randint(1,6)
    random_dice_label["text"] = "Player 1 Dice Random Number : " + str(randome_no)
    player1_score = player1_score + random_no
    player_1_score_label["text"] = str( player1_score)
    
    player_1_btn = Button(root, image = img, command = player1)
    player_1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)