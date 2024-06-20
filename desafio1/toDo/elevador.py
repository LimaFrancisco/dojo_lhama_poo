from typing import Type, List

class Elevador:

    # metodos
    def mudar_andar(self, novo_andar: Type[int], andares: Type[List]) -> Type[list]:
        posicao = andares.index("atual")
        andares[posicao] = posicao + 1
        andares[novo_andar - 1] = "atual"
        return andares
    