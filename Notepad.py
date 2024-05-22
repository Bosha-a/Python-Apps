from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("650x650")
root.title("My Notepad")
root.config(bg='lightgray')
root.resizable(False , False)

def save_file():
    open_file=filedialog.asksaveasfile(mode = 'w' , defaultextension='.txt')
    if open_file is None:
        return
    text = str(entry.get(1.0 , END))
    open_file.write(text)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode = 'r',filetype = [('text files','*.txt')])
    if file is None:
        content=file.read()
    entry.insert(INSERT,content)


b1 = Button(root,width='20',height='2',bg='#4569ed',text='Save File' , command=save_file).place(x = 125 , y = 15)
b1 = Button(root,width='20',height='2',bg='#4569ed',text='Open File' , command=open_file).place(x = 325 , y = 15)

entry = Text(root,width='79',height='35' , wrap=WORD)
entry.place(x=6,y=79)

root.mainloop()