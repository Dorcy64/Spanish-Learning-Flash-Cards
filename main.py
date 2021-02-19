from tkinter import *
import random
import pandas

NPATH = "data/original_spanish_words.csv"
DPATH = "data/spanish_words.csv"
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------------------READING DATA----------------------------------------------
WORDS_LIST = pandas.read_csv(DPATH)
WORDS_DICT = WORDS_LIST.to_dict()


WORD_NUMBER = random.randint(1, len(WORDS_DICT["Spanish"]))
SPANISH_WORD = WORDS_DICT["Spanish"][WORD_NUMBER]


# ----------------------------------------BUTTON FUNCTIONS------------------------------------------
def right():
    WORDS_DICT["Spanish"].pop(WORD_NUMBER)
    WORDS_DICT["English"].pop(WORD_NUMBER)
    NEW_WORD_DICT = {"Spanish": WORDS_DICT["Spanish"], "English": WORDS_DICT["English"]}
    NEW_WORD_LIST = pandas.DataFrame.from_dict(NEW_WORD_DICT)
    with open(file=DPATH, mode="w") as new_file:
        NEW_WORD_LIST.to_csv(new_file)
    random_word()


def wrong():
    random_word()


# ----------------------------------REVEAL THE WORD IN ENGLISH------------------------------------------
def reveal_word():
    ENGLISH_WORD = WORDS_DICT["English"][WORD_NUMBER]
    canvas.itemconfig(canvas_display, image=english_background)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word_display, text=ENGLISH_WORD, fill="white")


# ---------------------------------------THE WORD IN SPANISH-------------------------------------------
def random_word():
    global SPANISH_WORD, WORD_NUMBER
    WORD_NUMBER = random.randint(1, 1000)
    SPANISH_WORD = WORDS_DICT["Spanish"][WORD_NUMBER]
    canvas.itemconfig(canvas_display, image=spanish_background)
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(word_display, text=SPANISH_WORD, fill="black")
    window.after(3000, func=reveal_word)


# --------------------------------------------UI Design-----------------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# -------------------------------------First Words in Spanish ----------------------------------------


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
english_background = PhotoImage(file="images/card_back.png")
spanish_background = PhotoImage(file="images/card_front.png")
canvas_display = canvas.create_image(400, 263, image=spanish_background)
word_display = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text=SPANISH_WORD)
language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Spanish")
canvas.grid(column=1, row=1, columnspan=2)
window.after(3000, func=reveal_word)

# ---------------------------------------------Buttons------------------------------------------------

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
wrong_button.grid(column=1, row=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
right_button.grid(column=2, row=2)

window.mainloop()
