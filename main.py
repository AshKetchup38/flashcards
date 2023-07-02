from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

def pick_word():
    df = pd.read_csv("data/french_words.csv")
    df.to_dict(orient="records")
    random_word = random.choice(df["French"])
    canvas.itemconfig(word, text=random_word)

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
label = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel",40,"italic"))
word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=pick_word)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=pick_word)
right_button.grid(column=1, row=1)

window.mainloop()