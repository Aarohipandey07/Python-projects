from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

root=Tk()
root.geometry("600x600")
root.title("PAINT")

def __init__( root):
        canvas = Canvas(root, width=500, height=500, bg='white')
        canvas.pack()

        color = 'black'

        previous_x = None
        previous_y = None

        color_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Color", menu=color_menu)
        color_menu.add_command(label="Choose Color", command=choose_color)


        canvas.bind("<B1-Motion>", paint)
        canvas.bind("<ButtonRelease-1>", reset)
def paint(self, event):

    if self.previous_x and self.previous_y:
        self.canvas.create_line(self.previous_x, self.previous_y, event.x, event.y, width=2, fill=self.color,
                                capstyle=ROUND, smooth=TRUE)
    self.previous_x = event.x
    self.previous_y = event.y
def reset(self, event):

    self.previous_x = None
    self.previous_y = None
def choose_color(self):

    color = colorchooser.askcolor()[1]
    if color:
        self.color = color
def clear_canvas(self):

    self.canvas.delete("all")

def pack():
    pass
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
         text.delete(1.0, END)
         text.insert(INSERT, file.read())
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
          file.write(text.get(1.0, END))

def cut():
    text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")

def zoom_in():
    current_font_size = text.cget("font").split()[-1]
    new_font_size = int(current_font_size) + 2
    text.config(font=("Arial", new_font_size))
def zoom_out():
    current_font_size = text.cget("font").split()[-1]
    new_font_size = int(current_font_size) - 2
    text.config(font=("Arial", new_font_size))
def toggle_status_bar(status_bar):
    if status_bar.winfo_viewable():
        status_bar.pack_forget()
    else:
        status_bar.pack(side=BOTTOM, fill=X)
menubar = Menu(root)

m = Menu(menubar)
m.add_cascade(label="New ", command=pack)
m.add_cascade(label="Open", command=open_file)
m.add_cascade(label="Save", command=save_file)
m.add_cascade(label="Print", command=print)
m.add_cascade(label="Set as desktop background", command=pack)
m.add_separator()
m.add_cascade(label="Exit", command=quit)
menubar.add_cascade(label="FILE", menu=m)

m1=Menu(menubar)
m1.add_cascade(label="Cut", command=cut)
m1.add_cascade(label="Copy", command=copy)
m1.add_cascade(label="Paste", command=paste)
menubar.add_cascade(label="EDIT", menu=m1)

m2=Menu(menubar)
m2.add_cascade(label="Zoom In", command=zoom_in)
m2.add_cascade(label="Zoom Out", command=zoom_out)
m2.add_cascade(label="Status bar", command=toggle_status_bar)
menubar.add_cascade(label="VIEW", menu=m2)

root.config(menu=menubar)

text = Text(root, wrap='word')
text.pack(expand=1, fill='both', padx=10, pady=5)

root.mainloop()