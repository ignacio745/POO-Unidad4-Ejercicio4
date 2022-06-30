from __future__ import annotations
from typing import TYPE_CHECKING
from math import gcd

if TYPE_CHECKING:
    from Fraccion import Fraccion


class Fraccion:
    __numerador = None
    __denominador = None
    
    def __init__(self, numerador:int, denominador:int=1) -> None:
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0")
        
        self.__negativo = numerador * denominador < 0
        numerador = abs(numerador)
        denominador = abs(denominador)
        mcd = gcd(numerador, denominador)
        self.__numerador = numerador//mcd
        self.__denominador = denominador//mcd
    
    def getSigno(self) -> int:
        if self.__negativo:
            signo = -1
        else:
            signo = 1
        return signo

    def getNumerador(self) -> int:
        return self.__numerador
    

    def getDenominador(self) -> int:
        return self.__denominador


    def __add__(self, otra:Fraccion) -> Fraccion:
        numerador = self.getNumerador()*otra.getDenominador()*self.getSigno() + otra.getNumerador()*self.getDenominador()*otra.getSigno()
        denominador = self.getDenominador() * otra.getDenominador()
        return Fraccion(numerador, denominador)
    

    def __sub__(self, otra:Fraccion) -> Fraccion:
        numerador = self.getNumerador()*otra.getDenominador()*self.getSigno() - otra.getNumerador()*self.getDenominador()*otra.getSigno()
        denominador = self.getDenominador() * otra.getDenominador()
        return Fraccion(numerador, denominador)
    
    def __mul__(self, otra:Fraccion) -> Fraccion:
        numerador = self.getNumerador() * otra.getNumerador() * self.getSigno() * otra.getSigno()
        denominador = self.getDenominador() * otra.getDenominador()
        return Fraccion(numerador, denominador)
    
    def __truediv__(self, otra:Fraccion) -> Fraccion:
        numerador = self.getNumerador() * otra.getDenominador() * self.getSigno() * otra.getSigno()
        denominador = self.getDenominador() * otra.getNumerador()
        return Fraccion(numerador, denominador)
    

    def __str__(self):
        if self.__negativo:
            signo = "-"
        else:
            signo = ""
        
        cadena = "{0}{1}/{2}".format(signo, self.getNumerador(), self.getDenominador())
        return cadena