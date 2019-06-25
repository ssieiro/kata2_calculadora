from tkinter import *
from tkinter import ttk

_heightBtn = 50
_widthBtn = 68

class CalcDisplay (ttk.Frame): #Display donde sale el resultado
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn*4)

        self.pack_propagate(0)

        s = ttk.Style()
        s.configure('my.TLabel', font="Helvetica 42") #definimos un estilo genérico al que llamamos con el nombre 'my.TLabel'

        self.lblDisplay = ttk.Label(self, text='0', style='my.TLabel', anchor=E, foreground= "white")
        #al hacer esto nos coge el estilo de s.configure
        self.lblDisplay.pack(fill=BOTH, expand=True)

class CalcButton(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn)
        self.pack_propagate(0) #en 0 los botones se expanden, en 1 no lo hacen y cogen su tamaño por defecto

        self.button = ttk.Button(self, text=kwargs['text'], command=kwargs['command'])
        #le estamos diciendo que va a haber que mandarle un texto(que irá dentro del botón)
        self.button.pack(fill=BOTH, expand=True)


class Calculator(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])
        self.display = CalcDisplay(self) #Instancia de objeto Display
        self.display.grid(column=0, row=0, columnspan=4)

        CalcButton(self, text='C', command=None).grid(column=0, row=1) #instancias de cada botón
        CalcButton(self, text='+/-', command=None).grid(column=1, row=1)
        CalcButton(self, text='%', command=None).grid(column=2, row=1)
        CalcButton(self, text='÷', command=None).grid(column=3, row=1)
        CalcButton(self, text='7', command=None).grid(column=0, row=2)
        CalcButton(self, text='8', command=None).grid(column=1, row=2)
        CalcButton(self, text='9', command=None).grid(column=2, row=2)
        CalcButton(self, text='x', command=None).grid(column=3, row=2)
        CalcButton(self, text='4', command=None).grid(column=0, row=3)
        CalcButton(self, text='5', command=None).grid(column=1, row=3)
        CalcButton(self, text='6', command=None).grid(column=2, row=3)
        CalcButton(self, text='-', command=None).grid(column=3, row=3)
        CalcButton(self, text='1', command=None).grid(column=0, row=4)
        CalcButton(self, text='2', command=None).grid(column=1, row=4)
        CalcButton(self, text='3', command=None).grid(column=2, row=4)
        CalcButton(self, text='+', command=None).grid(column=3, row=4)
        CalcButton(self, text='0', command=None).grid(column=0, row=5, columnspan=2)
        CalcButton(self, text=',', command=None).grid(column=2, row=5)
        CalcButton(self, text='=', command=None).grid(column=3, row=5)

        

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculator")
        self.geometry("{}x{}".format(_widthBtn*4,_heightBtn*6))

        self.calculator = Calculator(self, height=300, width=272) #Para que haya una ventana encima que no toque mainApp
        self.calculator.place(x=0, y=0)


    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.start()