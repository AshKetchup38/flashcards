from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    dict = df.to_dict(orient="records")
    fr_word = {}

def remove_word():
    dict.remove(fr_word)
    df = pd.DataFrame.from_dict(dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    pick_word()


def flip():
    eng_word = fr_word["English"]
    canvas.itemconfig(label, text="English", fill="white")
    canvas.itemconfig(word, text=eng_word, fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)

def pick_word():
    global fr_word, flip_timer
    window.after_cancel(flip_timer)
    fr_word = random.choice(dict)
    canvas.itemconfig(label, text="French", fill="black")
    canvas.itemconfig(word, text=fr_word["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip)

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
label = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel",40,"italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=pick_word)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

pick_word()

window.mainloop()