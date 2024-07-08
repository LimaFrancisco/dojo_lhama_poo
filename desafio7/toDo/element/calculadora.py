import math
from typing import Type

class Calculadora:

    # methods
    def calcular(self, primiero_valor: Type[float], segundo_valor: Type[float]) -> Type[float]:
        valor = self.__realizar_primeiro_calculo(primiero_valor) + self.__realizar_segundo_calculo(segundo_valor)
        valor = valor * 4.2
        return valor

    def __realizar_primeiro_calculo(self, valor: Type[float]) -> Type[float]:
        valor = math.sqrt((valor * 5) / 8) ** 3
        return valor

    def __realizar_segundo_calculo(self, valor: Type[float]) -> Type[float]:
        valor = (((valor ** 2) + valor) * 2) / 5
        valor += 5.7
        return valor
    