from tkinter import *
account_bal=0
def check_balance():
    global scvalue
    result_label.config(text=f"Your balance is: {account_bal}")
def deposit():
    global account_bal
    amount = int(scvalue.get())
    account_bal += amount
    result_label.config(text=f"Deposited: {amount}. New balance: {account_bal}")
def withdraw():
    global account_bal
    amount = int(scvalue.get())
    if account_bal<amount:
        result_label.config(text="Insufficent Balance")
    else:
        account_bal -= amount
        result_label.config(text=f"withdrawn: {amount}. New balance: {account_bal}")
        scvalue.set("")
def on_click(event):
     scvalue.set("")
     screen.update()

root=Tk()
root.geometry("600x700")
root.title("ATM")

background_image = PhotoImage(file="img3.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

lavel = Label( text="Welcome to the ATM", font=("Arial", 20))
lavel.pack(pady=10)

amount = Label(text="Amount:",font="bold")
amount.pack(pady=20)

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvar=scvalue, font="bookman, 12")
screen.pack( ipadx=70, padx=20,pady=70, ipady=20)
# amount_entry =Entry()
# amount_entry.pack(pady=30,padx=70,ipadx=70,ipady=30)
# amount_entry.setvar()
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

check_balance_button = Button( text="Check Balance", width=20, command=check_balance)
check_balance_button.pack(pady=5)

deposit_button =Button( text="Deposit Money", width=20, command=deposit)
deposit_button.pack(pady=5)

withdraw_button = Button( text="Withdraw Money", width=20, command=withdraw)
withdraw_button.pack(pady=5)

exit_button =Button( text="Exit", width=20, command=quit)
exit_button.pack(pady=5)

b1=Button(text="C",fg="black", width=2, height=1,font=("Raleway", 24))
b1.pack(padx=5,pady=5)
b1.bind("<Button-1>",on_click)

root.mainloop()