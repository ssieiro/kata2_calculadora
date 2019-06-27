from tkinter import *
from tkinter import ttk

_heightBtn = 50
_widthBtn = 68

class CalcDisplay (ttk.Frame): #Display donde sale el resultado
    _value = '0'
    _espositivo = True
    def __init__(self, parent, **kwargs):
        
        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn*4)

        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt') #cambiar el estilo por defecto
        s.configure('my.TLabel', font="Helvetica 42") #definimos un estilo genérico al que llamamos con el nombre 'my.TLabel'

        self.lblDisplay = ttk.Label(self, text=self._value, style='my.TLabel', anchor=E, foreground= "white", background='#234aa0')
        #al hacer esto nos coge el estilo de s.configure
        self.lblDisplay.pack(fill=BOTH, expand=True)

    def addDigit(self, digito):
        if len(self._value) >= 12 or \
            (len(self._value) >= 11 and (self._value[0] != '-' or '.' not in self._value)) or \
            (len(self._value) >= 10 and self._value[0] != "-" and '.' not in self._value):
            return
        if '.' in self._value and digito == '.':
            return
        '''
            if self.value[0] == "-":
                if len(self._value) == 10:
                    longmax= 11
                else:
                    longmax = 10
            
            if len(self._value) >= longmax:
                return
        '''
        if self._value == '0' and digito != '.':
            self._value = digito
        else:
            self._value += digito
        
        self.pintar()
        
    
    def pintar (self):
        self.lblDisplay.configure(text=self._value)
    
    def reset (self):
        self._value = '0'
        self._espositivo = True
        self.pintar()

    def signo(self):
        if self._value == '0':
            return
        if self._espositivo:
            self._value = '-' + self._value
        else:
            self._value = self._value[1:] #elimina el primer caracter, porque elimina el carácter 0
        self._espositivo = not self._espositivo
        self.pintar()
        




class CalcButton(ttk.Frame):

    def __init__(self, parent, **kwargs):
        if 'bw' in kwargs:
            bw = kwargs['bw']
        else:
            bw = 1

        # bw = kwargs ['bw'] if 'bw' in kwargs else 1 # esta expresión equivale al if de arriba

        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn * bw)
        self.pack_propagate(0) #en 0 los botones se expanden, en 1 no lo hacen y cogen su tamaño por defecto

        self.button = ttk.Button(self, text=kwargs['text'], command=kwargs['command'])
        #le estamos diciendo que va a haber que mandarle un texto(que irá dentro del botón)
        self.button.pack(fill=BOTH, expand=True)


class Calculator(ttk.Frame):
    _op1 = None
    _op2 = None
    _operador = None
    _swBorrado = True

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])
        self.display = CalcDisplay(self) #Instancia de objeto Display
        self.display.grid(column=0, row=0, columnspan=4)

        CalcButton(self, text='C', command=self.reset).grid(column=0) #instancias de cada botón
        CalcButton(self, text='CE', command=None).grid(column=1, row=1)
        CalcButton(self, text='+/-', command=self.display.signo).grid(column=2, row=1)
        CalcButton(self, text='÷', command=lambda: self.opera('÷')).grid(column=3, row=1)
        CalcButton(self, text='7', command=lambda : self.addDigit('7')).grid(column=0, row=2)
        CalcButton(self, text='8', command=lambda : self.addDigit('8')).grid(column=1, row=2)
        CalcButton(self, text='9', command=lambda : self.addDigit('9')).grid(column=2, row=2)
        CalcButton(self, text='x', command=lambda: self.opera('x')).grid(column=3, row=2)
        CalcButton(self, text='4', command=lambda : self.addDigit('4')).grid(column=0, row=3)
        CalcButton(self, text='5', command=lambda : self.addDigit('5')).grid(column=1, row=3)
        CalcButton(self, text='6', command=lambda : self.addDigit('6')).grid(column=2, row=3)
        CalcButton(self, text='-', command=lambda: self.opera('-')).grid(column=3, row=3)
        CalcButton(self, text='1', command=lambda : self.addDigit('1')).grid(column=0, row=4)
        CalcButton(self, text='2', command=lambda : self.addDigit('2')).grid(column=1, row=4)
        CalcButton(self, text='3', command=lambda : self.addDigit('3')).grid(column=2, row=4)
        CalcButton(self, text='+', command=lambda: self.opera('+')).grid(column=3, row=4)
        CalcButton(self, text='0', command=lambda : self.addDigit('0'), bw=2).grid(column=0, row=5, columnspan=2)
        CalcButton(self, text='.', command=lambda: self.addDigit('.')).grid(column=2, row=5)
        CalcButton(self, text='=', command=lambda: self.opera('=')).grid(column=3, row=5)
        #Usamos lambda porque command no permite funciones con parámetros, así que usamos una funcion anonima para enviar un valor

    def addDigit(self, digito):
        if self._swBorrado:
            self.display.reset()
            self._swBorrado = False

        self.display.addDigit(digito)

    def reset(self):
        self._op1 = None
        self._op2 = None
        self._operador = None
        self.display.reset()

    def opera(self, operador):
        if self._op1 is None:
            self._op1 = float(self.display._value)
            self._operador = operador
            self._swBorrado = True
        else:
            if self._op2 == None:
                self._op2 = float(self.display._value)
            if self._operador == '+':
                resultado = self._op1 + self._op2
            elif self._operador == '-':
                resultado = self._op1 - self._op2
            elif self._operador == 'x':
                resultado = self._op1 * self._op2
            elif self._operador == '÷':
                resultado = self._op1 / self._op2
            else:
                print('operador incorrecto')
            
            self._operador1 = resultado
            if operador != '=':
                self._operador = operador
                self._op2 = None
            
            resultado = str(round(resultado, 9))
            self.display._value = resultado
            self.display.pintar()

        self._swBorrado = True


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