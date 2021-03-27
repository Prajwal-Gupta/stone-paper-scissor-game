from tkinter import *
import random
import sys

def quit(event):
    sys.exit()
def click(event):
    choices = ['Stone','Paper','Scissor']
    b = (random.choice(choices))
    a = event.widget.cget("text")
    
    
    if a == 'Stone' and b == 'Paper':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.resizable(0,0)
        newWindow.geometry("300x200")
        Label(newWindow, text ="Computer selected: {}\nYou lost :(\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Stone' and b == 'Scissor':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nYou won :)\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Stone' and b == 'Stone':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nIts a tie :|\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Paper' and b == 'Paper':
       
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nIts a tie :|\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Paper' and b == 'Scissor':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nYou lost :(\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Paper' and b == 'Stone':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nYou won :)\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Scissor' and b == 'Paper':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nYou won :)\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Scissor' and b == 'Stone':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nYou lost :(\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
    if a == 'Scissor' and b == 'Scissor':
        
        newWindow = Toplevel(root)
        newWindow.title("Result")
        newWindow.geometry("300x200")
        newWindow.resizable(0,0)
        Label(newWindow, text ="Computer selected: {}\nIts a tie :|\nTry again".format(b), font="cambria 15 bold").pack(expand=TRUE)
root = Tk()
root.geometry("500x300")
root.title("STONE PAPER SCISSORS")
root.configure(bg="white")
root.minsize(500,300)
f1 = Frame(root, bg = "white", width=100, height=100)
f1.pack(expand=TRUE, anchor = CENTER)
l=Label(text = "SELECT STONE PAPER OR SCISSOR", font="cambria 12 bold", bg="white")
b1 = Button(f1,text = "Stone", height=1, width=10, font="cambria 15 bold")
b2 = Button(f1,text = "Paper", height=1, width=10, font="cambria 15 bold")
b3 = Button(f1,text = "Scissor", height=1, width=10, font="cambria 15 bold")
qb = Button(f1, text = "Exit", height=1, width=10, font="cambria 15 bold")
qb.bind('<Button-1>', quit)
b1.bind('<Button-1>', click)
b2.bind('<Button-1>', click)
b3.bind('<Button-1>', click)

l.pack(pady=(0,10))

b1.grid(row=1, column=0, padx=(10,0), pady=10)
b2.grid(row=1, column=1, padx=(10,0), pady=10)
b3.grid(row=1, column=2, padx=(10,10), pady=10)
qb.grid(row=2, column=1, padx=(10,0), pady=(0,10))

p1 = PhotoImage(file = 'stone.png')
p2 = PhotoImage(file = 'paper.png')
p3 = PhotoImage(file = 'scissor.png')

lb1 = Label(f1, image = p1)
lb2 = Label(f1, image = p2)
lb3 = Label(f1, image = p3)
lb1.grid(row=0, column=0, padx=(5,0), pady=5)
lb2.grid(row=0, column=1, padx=(5,0), pady=5)
lb3.grid(row=0, column=2, padx=(5,5), pady=5)

root.iconphoto(False, p3)
root.mainloop()