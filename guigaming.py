from tkinter import *
import random


def on_click(event):
    global scvalue, secret_no, attempts
    text = event.widget.cget("text")

    if text.isdigit():
        scvalue.set(scvalue.get() + text)
    elif text == "Guess":
        guess = scvalue.get()
        if guess.isdigit():
            guess = int(guess)
            if guess == secret_no:
                result.set("Congratulations! You guessed it right.")
                attempts = 0
            elif guess < secret_no:
                result.set(f"Try a higher number. Attempts left: {attempts - 1}")
            else:
                result.set(f"Try a lower number. Attempts left: {attempts - 1}")
            attempts -= 1
            if attempts == 0 and guess != secret_no:
                result.set(f"Game Over! The number was {secret_no}.")
        scvalue.set("")
    elif text == "C":
        scvalue.set("")
        result.set("")


root = Tk()
root.geometry("500x500")
root.title("Number Guessing Game")
icon = PhotoImage(file='GAME.png')
root.iconphoto(False, icon)

# Initialize game variables
secret_no = random.randint(1, 100)
attempts = 10

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="bookman, 12")
screen.pack(fill=X, ipadx=8, padx=8, pady=8, ipady=8)

result = StringVar()
result.set("")
result_label = Label(root, textvar=result, font="bookman, 12", fg="red")
result_label.pack()

# Frame and buttons
f1 = Frame(root, bg="yellow")
buttons = [
    '1', '2', '3', '4', '5',
    '6', '7', '8', '9', '0',
    'Guess', 'C'
]

for btn_text in buttons:
    btn = Button(f1, text=btn_text, fg="black", font=("Raleway", 24), width=2, height=1)
    btn.pack(side=LEFT, padx=5, pady=5, fill='both')
    btn.bind("<Button-1>", on_click)
f1.pack()

root.mainloop()
