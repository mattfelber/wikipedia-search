from tkinter import *
import wikipedia as wiki

root = Tk()
root.title('')
icon = PhotoImage(file='lupa.png')
root.iconphoto(True, icon)
root.geometry("900x875")


# clear
def clear():
    my_entry.delete(0, END)
    my_text.delete(0.0, END)


# search
def search():
    data = wiki.summary(my_entry.get(), sentences=33)
    # clear screen
    clear()
    # output wikipedia to textbox
    my_text.insert(0.0, data)


my_label_frame = LabelFrame(root, text="Search Wikipedia")
my_label_frame.pack(pady=20)

my_entry = Entry(my_label_frame, font=("Helvetica", 18), fg="black", width=47)
my_entry.pack(pady=20, padx=20)

# textbox frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# vertical scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# text box
my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap="word", xscrollcommand=hor_scroll, bg="white",
               fg="black",
               font=("Helvetica", 15))
my_text.pack()

# config scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.yview)

# button-frame
button_frame = Frame(root)
button_frame.pack(pady=10)

# Two Buttons:
search_button = Button(button_frame, text="Search", font=("Helvetica", 33), fg="black", command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = Button(button_frame, text="Clear", font=("Helvetica", 33), fg="black", command=clear)
clear_button.grid(row=0, column=1)

root.mainloop()
