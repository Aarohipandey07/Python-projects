from tkinter import *
from tkinter import filedialog, messagebox

def update_status_bar(event=None):
    content = text.get(1.0, END)
    words = len(content.split())
    language = "English"  # You can set this dynamically if needed
    status_bar.config(text=f"Words: {words} | Language: {language}")

def new_window():
    new_win = Toplevel(root)
    new_win.geometry("600x500")
    new_win.title("New Window")

    # Add the same menubar and text widget to the new window
    new_text = Text(new_win, wrap='word', font=("Arial", 14), undo=True, spacing1=5)  # Font and line spacing
    new_text.pack(expand=1, fill='both', padx=20, pady=20)  # Added margin (padding)

    new_status_bar = Label(new_win, text="Status Bar", anchor=W)
    new_status_bar.pack(side=BOTTOM, fill=X)

    new_text.bind("<<Modified>>", lambda event: update_status_bar(event))

    new_menubar = Menu(new_win)

    m = Menu(new_menubar, tearoff=0)
    m.add_command(label="New tab", command=new_tab)
    m.add_command(label="New window", command=new_window)
    m.add_command(label="Open", command=lambda: open_file(new_text))
    m.add_command(label="Save", command=lambda: save_file(new_text))
    m.add_command(label="Print", command=print_file)
    m.add_command(label="Exit", command=new_win.quit)
    m.add_separator()
    new_menubar.add_cascade(label="FILE", menu=m)

    m1 = Menu(new_menubar, tearoff=0)
    m1.add_command(label="Undo", command=lambda: undo(new_text))
    m1.add_command(label="Cut", command=lambda: cut(new_text))
    m1.add_command(label="Copy", command=lambda: copy(new_text))
    m1.add_command(label="Paste", command=lambda: paste(new_text))
    m1.add_command(label="Delete", command=icon)
    m1.add_command(label="Select all", command=icon)
    m1.add_command(label="Time/Date", command=lambda: datetime(new_text))
    m1.add_command(label="Font", command=icon)
    m1.add_separator()
    new_menubar.add_cascade(label="Edit", menu=m1)

    m2 = Menu(new_menubar, tearoff=0)
    m2.add_command(label="Zoom In", command=lambda: zoom_in(new_text))
    m2.add_command(label="Zoom Out", command=lambda: zoom_out(new_text))
    m2.add_command(label="Status bar", command=icon)
    m2.add_command(label="Word wrap", command=icon)
    m2.add_separator()
    new_menubar.add_cascade(label="View", menu=m2)

    new_win.config(menu=new_menubar)

def new_tab():
    pass

def open_file(text_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_widget.delete(1.0, END)
            text_widget.insert(INSERT, file.read())
        update_status_bar()

def save_file(text_widget):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get(1.0, END))

def print_file():
    messagebox.showinfo("Print", "Printing functionality is not implemented yet.")

def undo(text_widget):
    text_widget.edit_undo()

def cut(text_widget):
    text_widget.event_generate("<<Cut>>")

def copy(text_widget):
    text_widget.event_generate("<<Copy>>")

def paste(text_widget):
    text_widget.event_generate("<<Paste>>")

def datetime(text_widget):
    import time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    text_widget.insert(INSERT, current_time)

def zoom_in(text_widget):
    current_font_size = text_widget.cget("font").split()[-1]
    new_font_size = int(current_font_size) + 2
    text_widget.config(font=("Arial", new_font_size))

def zoom_out(text_widget):
    current_font_size = text_widget.cget("font").split()[-1]
    new_font_size = int(current_font_size) - 2
    text_widget.config(font=("Arial", new_font_size))

def icon():
    messagebox.showinfo("Info", "This is a placeholder function.")

root = Tk()
root.geometry("600x500")
root.title("NOTEPAD")

menubar = Menu(root)

m = Menu(menubar, tearoff=0)
m.add_command(label="New tab", command=new_tab)
m.add_command(label="New window", command=new_window)
m.add_command(label="Open", command=lambda: open_file(text))
m.add_command(label="Save", command=lambda: save_file(text))
m.add_command(label="Print", command=print_file)
m.add_command(label="Exit", command=root.quit)
m.add_separator()
menubar.add_cascade(label="FILE", menu=m)

m1 = Menu(menubar, tearoff=0)
m1.add_command(label="Undo", command=lambda: undo(text))
m1.add_command(label="Cut", command=lambda: cut(text))
m1.add_command(label="Copy", command=lambda: copy(text))
m1.add_command(label="Paste", command=lambda: paste(text))
m1.add_command(label="Delete", command=icon)
m1.add_command(label="Select all", command=icon)
m1.add_command(label="Time/Date", command=lambda: datetime(text))
m1.add_command(label="Font", command=icon)
m1.add_separator()
menubar.add_cascade(label="Edit", menu=m1)

m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Zoom In", command=lambda: zoom_in(text))
m2.add_command(label="Zoom Out", command=lambda: zoom_out(text))
m2.add_command(label="Status bar", command=icon)
m2.add_command(label="Word wrap", command=icon)
m2.add_separator()
menubar.add_cascade(label="View", menu=m2)

root.config(menu=menubar)

# Added padding/margin, and line spacing to the text widget
text = Text(root, wrap='word', font=("Arial", 14), undo=True, spacing1=5)  # Font, spacing, line spacing
text.pack(expand=1, fill='both', padx=20, pady=20)  # Added margin

status_bar = Label(root, text="Words: 0 | Language: English", anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

text.bind("<<Modified>>", update_status_bar)

root.mainloop()
