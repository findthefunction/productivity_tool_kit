from tkinter import *
from tkinter import messagebox

# Add Task function

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning('warning','Please enter some task.')
        
# Delete Task function

def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('400x275+1000+400')
ws.title("Today's Quests")
ws.config(bg='#121212')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=5)

lb= Listbox(
    frame,
    width=25,
    height=6,
    font=('Times', 18),
    bd=0,
    bg="#820000",
    fg="#f7af05",
    highlightthickness=0,
    selectbackground='#ff3b3b',
    activestyle='none',
    
)
lb.pack(side=LEFT, fill=BOTH)

#Sample list items can be deleted

task_list = [
    'Drink water',
    'Exercise',
    'Practice Server Spin up',
    'Read a Chapter',
    'Organize'
]
# END to add to bottom of list 0 to add to top
for item in task_list:
    lb.insert(END, item)

# Scroll bar functionality

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Entry Box

my_entry = Entry(
    ws,
    font=('times', 24),
    bg="#820000",
    fg="#f7af05"
)

my_entry.pack(pady=10)

# Frame for buttons

button_frame = Frame(ws)
button_frame.pack(pady=5)

#Buttons

addTask_btn =Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#5085d9',
    padx=10,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Completed',
    font=('times 14'),
    bg='#66e84f',
    padx=10,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()

