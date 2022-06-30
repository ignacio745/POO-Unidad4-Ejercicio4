from functools import partial
import tkinter as tk
from tkinter import ttk
from Fraccion import Fraccion

class Calculadora:
    __aux:Fraccion
    def __init__(self) -> None:
        self.__ventana = tk.Tk()
        self.__ventana.title("Calculadora")
        self.__mainframe = ttk.Frame(self.__ventana)
        self.__mainframe.grid(row=0, column=0)
        self.__valor = tk.StringVar()
        self.__aux = 0
        self.__operacion = None
        self.__entrada = ttk.Entry(self.__mainframe, textvariable=self.__valor)
        self.__entrada.grid(row=0, column=1, columnspan=2)
        for r in range(3):
            for c in range(3):
                boton = ttk.Button(self.__mainframe, text="{}".format(r*3+c+1), command=partial(self.ponerNumero, "{}".format(r*3+c+1)))
                boton.grid(row=r+1, column=c)
        
        ttk.Button(self.__mainframe, text="0", command=partial(self.ponerNumero, "0")).grid(row=4, column=0)
        ttk.Button(self.__mainframe, text="+", command=partial(self.ponerOperacion, "+")).grid(row=4, column=1)
        ttk.Button(self.__mainframe, text="-", command=partial(self.ponerOperacion, "-")).grid(row=4, column=2)
        ttk.Button(self.__mainframe, text="*", command=partial(self.ponerOperacion, "*")).grid(row=5, column=0)
        ttk.Button(self.__mainframe, text="%", command=partial(self.ponerOperacion, "%")).grid(row=5, column=1)
        ttk.Button(self.__mainframe, text="/", command=partial(self.ponerNumero, "/")).grid(row=5, column=2)
        ttk.Button(self.__mainframe, text="=", command=self.calcular).grid(row=6, column=0)
        ttk.Button(self.__mainframe, text="AC", command=self.limpiar).grid(row=6, column=1)
        
        
        
        self.__ventana.mainloop()
    



    def ponerNumero(self, numero):
        self.__valor.set("{0}{1}".format(self.__valor.get(), numero))
    

    def ponerOperacion(self, operacion):
        valores = self.__valor.get()
        try:
            numerador, denominador = valores.split("/")
        except:
            numerador = int(self.__valor.get())
            denominador = 1
        else:
            numerador = int(numerador)
            denominador = int(denominador)
        
        self.__aux = Fraccion(numerador, denominador)
        
        self.__operacion = operacion

        self.__valor.set("")
    

    def calcular(self):
        valores = self.__valor.get()
        try:
            numerador, denominador = valores.split("/")
        except:
            numerador = int(self.__valor.get())
            denominador = 1
        else:
            numerador = int(numerador)
            denominador = int(denominador)
        valor = Fraccion(numerador, denominador)
        if self.__operacion == "+":
            resultado = self.__aux + valor

        elif self.__operacion == "-":
            resultado = self.__aux - valor
        
        elif self.__operacion == "*":
            resultado = self.__aux * valor
        
        elif self.__operacion == "%":
            resultado = self.__aux / valor
        
        else:
            resultado = valor
        
        if resultado.getDenominador() == 1:
            resultado = resultado.getSigno() * resultado.getNumerador()
        
        self.__valor.set(str(resultado))
    

    def limpiar(self):
        self.__aux = None
        self.__valor.set("")