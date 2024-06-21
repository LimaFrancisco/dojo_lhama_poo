from typing import Type

class Elevador:

    # metodos
    def mudar_andar(self, novo_andar: Type[int]) -> Type[int]:
        if self.__verificar_andar(novo_andar):
            return novo_andar
    
    def mostrar_andar_atual(self, andar: Type[int]) -> Type[str]:
        if andar == 1:
            return f"O seu andar atual é o terreo"
        else:
            return f"O seu andar atual é {andar}"
    
    def __verificar_andar(self, novo_andar: Type[int]) -> Type[bool]:
        if novo_andar >= 1 and novo_andar <= 15:
            return True
        else: 
            return False
        