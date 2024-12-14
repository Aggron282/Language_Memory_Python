BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *;
import pandas;
import random;
data = None;

try:
    data = pandas.read_csv("./data/known_ja.csv");
except FileExistsError:
    data = pandas.read_csv("./data/ja.csv");

guide = data.to_dict(orient="records");
random_word = None;
flip_timer = None;


def is_known():
    guide.remove(random_word);
    data = pandas.DataFrame(guide);
    data.to_csv("./data/known_ja.csv",index=False);
    next_card();

def next_card():
    global random_word,flip_timer;
    if flip_timer is not None:
        window.after_cancel(flip_timer);
    random_word = random.choice(guide);
    foreign_word = random_word["Japanese"];
    canvas.itemconfig(title,text="Japanese",fill="black");
    canvas.itemconfig(word,text=foreign_word,fill="black");
    canvas.itemconfig(card,image=card_front);
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    native_word = random_word["English"].title();
    canvas.itemconfig(title,text="English",fill="white");
    canvas.itemconfig(word,text=native_word,fill="white");
    canvas.itemconfig(card,image=card_back);
    

window = Tk();
window.title("Lang Memory");
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR);

canvas = Canvas(width=800,height=526);
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png");
card_back = PhotoImage(file="./images/card_back.png");
correct_icon = PhotoImage(file="./images/right.png");
wrong_icon = PhotoImage(file="./images/wrong.png");

canvas.grid(row=0,column=0,columnspan=2);
card = canvas.create_image(400,263,image=card_front);
title = canvas.create_text(400,150,text="Title",font=("Helvetica","30","italic"));
word = canvas.create_text(400,263,text="word",font=("Helvetica","60","normal"));

wrong_button = Button(image=wrong_icon,command=next_card);
correct_button = Button(image = correct_icon,command=is_known);

wrong_button.config(highlightthickness=0,bg=BACKGROUND_COLOR,border=None,borderwidth=0)
correct_button.config(highlightthickness=0,bg=BACKGROUND_COLOR,border=None,borderwidth=0)
wrong_button.grid(row=1,column=0);
correct_button.grid(row=1,column=1);

next_card();


window.mainloop();
