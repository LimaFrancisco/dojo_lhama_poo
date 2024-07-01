from typing import Type
from .pessoa import Pessoa

class Controlador:

    def __init__(self, jogador1: Type[Pessoa], jogador2: Type[Pessoa]) -> Type[None]:
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2

    def comecar_rodada(self) -> Type[None]:
        jogador1_jogada = self.__jogador1.jogar()
        jogador2_jogada = self.__jogador2.jogar()

        resultado_rodada = self.__verificar_jogada(jogador1_jogada, jogador2_jogada)

        if resultado_rodada == 1:
            self.__jogador1.marcar_ponto()
        if resultado_rodada == 2:
            self.__jogador2.marcar_ponto()
         
        return self.__apresentar_resultados()

    def __verificar_jogada(self, jogador1_jogada, jogador2_jogada) -> Type[int]:
        if jogador1_jogada == jogador2_jogada:
            return 0
        if (jogador1_jogada == 'pedra' and jogador2_jogada == 'tesoura') or (jogador1_jogada == 'papel' and jogador2_jogada == 'pedra') or (jogador1_jogada == 'tesoura' and jogador2_jogada == 'papel'):
            return 1
        
        return 2

    def __apresentar_resultados(self):
        return f'{self.__jogador1.exibir_dados()}\n----------------------------- \n{self.__jogador2.exibir_dados()}'
    