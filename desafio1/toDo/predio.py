from typing import Type
from elevador import Elevador

class Predio:

    # contrutor 
    def __init__(self) -> None:
        self.__andares = ["atual", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
        self.__elevador = Elevador()

    # metodos 
    def mostrar_andar_atual(self) -> Type[str]:
        return f"O seu andar atual é {self.__andares.index("atual") + 1}"
    
    def mudar_andar(self, novo_andar: int) -> Type[None]:
        if self.__verificar_andar(novo_andar):
            self.__andares = self.__elevador.mudar_andar(novo_andar, self.__andares)

    def __verificar_andar(self, novo_andar) -> Type[bool]:
        if novo_andar >= 1 and novo_andar <= 15:
            return True
        else: 
            return False