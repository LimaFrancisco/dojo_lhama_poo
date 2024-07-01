from typing import Type
from random import choice

class Pessoa:

    def __init__(self, nome: Type[str]) -> Type[None]:
        self.__nome = nome
        self.__pontuacao = 0
        self.__jogadas = ['pedra', 'papel', 'tesoura']

    def jogar(self) -> Type[str]:
        return choice(self.__jogadas)

    def marcar_ponto(self) -> Type[None]:
        self.__pontuacao += 1 

    def exibir_dados(self) -> Type[str]:
        dado = f'Nome: {self.__nome}\nPontuacao: {self.__pontuacao}'
        return dado 
    