from tkinter import Tk , Entry , Button , StringVar
class Calculator:
    def __init__(self,master):
        master.title("My Calculator")
        master.geometry('360x420+0+0')
        master.config(bg='gray')
        master.resizable(False,False)

        self.equation = StringVar()
        self.entry_value=''
        Entry(width=17 , bg = '#C0C0C0' , font =('Arial Bold',28),textvariable=self.equation).place(x=0 , y=0)

        Button(width =11 , height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0, y=50)
        Button(width =11 , height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90 , y=50)
        Button(width =11 , height=4,text='Square',relief='flat',bg='white',command=self.powerr).place(x=180 , y=50)
        Button(width =11 , height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270 , y=50)
        Button(width =11 , height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270 , y=125)
        Button(width =11 , height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270 , y=200)
        Button(width =11 , height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270 , y=275)
        Button(width =11 , height=4,text='=',relief='flat',bg='blue',command=self.solve).place(x=270 , y=350)
        Button(width =11 , height=4,text='7',relief='flat',bg='white',command=lambda:self.show('7')).place(x=0 , y=125)
        Button(width =11 , height=4,text='8',relief='flat',bg='white',command=lambda:self.show('8')).place(x=90 , y=125)
        Button(width =11 , height=4,text='9',relief='flat',bg='white',command=lambda:self.show('9')).place(x=180 , y=125)
        Button(width =11 , height=4,text='4',relief='flat',bg='white',command=lambda:self.show('4')).place(x=0 , y=200)
        Button(width =11 , height=4,text='5',relief='flat',bg='white',command=lambda:self.show('5')).place(x=90 , y=200)
        Button(width =11 , height=4,text='6',relief='flat',bg='white',command=lambda:self.show('6')).place(x=180 , y=200)
        Button(width =11 , height=4,text='1',relief='flat',bg='white',command=lambda:self.show('1')).place(x=0 , y=275)
        Button(width =11 , height=4,text='2',relief='flat',bg='white',command=lambda:self.show('2')).place(x=90 , y=275)
        Button(width =11 , height=4,text='3',relief='flat',bg='white',command=lambda:self.show('3')).place(x=180 , y=275)
        Button(width =11 , height=4,text='Clear',relief='flat',bg='white',command=self.clear).place(x=0 , y=350)
        Button(width =11 , height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=90 , y=350)
        Button(width =11 , height=4,text='0',relief='flat',bg='white',command=lambda:self.show('0')).place(x=180 , y=350)

    def show(self , value):
        self.entry_value += str(value) 
        self.equation.set(self.entry_value) 

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

    def powerr(self):
        result1 = eval(self.entry_value)
        power = 2 
        result_powered = result1 ** power
        self.entry_value = str(result_powered)
        self.equation.set(self.entry_value)


root = Tk()
Calculator = Calculator(root)
root.mainloop()