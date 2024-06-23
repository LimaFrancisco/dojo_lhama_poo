from typing import Type

class Elevador:

    # construtor
    def __init__(self, id: Type[int]) -> Type[None]:
        self.__elevador_id = id
        self.__andar = 1

    # metodos
    def mudar_andar(self, novo_andar: Type[int]):
        if self.__verificar_andar(novo_andar):
            self.__andar = self.__identificar_terreo(novo_andar)
        
    def mostrar_andar_atual(self) -> Type[int]:
        return self.__andar
    
    def __identificar_terreo(self, andar: Type[int]):
        if andar == 1:
            return 'terreo'
        else:
            return andar
    
    def __verificar_andar(self, novo_andar: Type[int]) -> Type[bool]:
        if 1 <= novo_andar <= 15:
            return True
        else:
            return False
 