from abc import ABC, abstractmethod
from typing import Type

class CalculadoraInterface(ABC):

    # methods
    @abstractmethod
    def calcular(self, primiero_valor: Type[float], segundo_valor: Type[float]) -> Type[float]:
        pass

    @abstractmethod
    def _realizar_primeiro_calculo(self, valor: Type[float]) -> Type[float]:
        pass

    @abstractmethod
    def _realizar_segundo_calculo(self, valor: Type[float]) -> Type[float]:
        pass
    