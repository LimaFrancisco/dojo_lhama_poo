from typing import Type
from elevador import Elevador

class Predio:

    # contrutor 
    def __init__(self) -> None:
        self.__andar = 1 
        self.__elevador = Elevador()

    # metodos
    def mudar_andar(self, novo_andar: Type[int]) -> Type[None]:
        self.__andar = self.__elevador.mudar_andar(novo_andar)

    def mostrar_andar_atual(self) -> Type[str]:
        return self.__elevador.mostrar_andar_atual(self.__andar)
