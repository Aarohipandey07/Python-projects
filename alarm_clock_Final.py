from tkinter import *
from tkinter import messagebox
from playsound import playsound
import datetime
import time
import threading
from PIL import Image,ImageTk
def alarm(set_timer):
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_timer:
            messagebox.showinfo("information","wake upppp")
            playsound("scary_alarm.wav")
            break

def set_alarm():
     set_timer = time_entry.get()

     if set_timer:
        messagebox.showinfo("information", "your alarm has been raised")
        alarm_label.config(text=f"Alarm set for: {set_timer}")
        threading.Thread(target=alarm, args=(set_timer,)).start()
     else:
          messagebox.showerror("Input Error", "Please enter a valid time.")


root = Tk()
root.geometry("700x500")
root.title("ALARM CLOCK")

background_image = PhotoImage(file="photooo.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# photo = Image.open("student-removebg-preview.png")
# img_resize = photo.resize((200, 200))
# photos = ImageTk.PhotoImage(img_resize)
# image_label = Label(image=photos)
# image_label.pack(side=LEFT)

time_format = Label( root, text=" ENTER TIME IN 24 HOUR FORMAT ", font=("Arial", 20))

time_label = Label(root, text="HOUR:MIN:SEC", font=("Arial", 14))
time_label.grid(row=1, column=0, sticky='w', padx=10, pady=10)

time_entry = Entry(root, width=20, font=("Arial", 14))
time_entry.grid(row=1, column=1)


button = Button( root,text="set alarm",width=20,height=2,font=("Helvetica", 14),command=set_alarm)

alarm_label = Label(root, text="No alarm set", font=("Arial", 16))
alarm_label.grid(row=3, column=1, pady=10)

time_format.grid(row=0,column=1,sticky='w')

button.grid(row=4,column=1,sticky='e',rowspan=3)

root.mainloop()