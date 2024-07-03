from typing import Type
from .livro import Livro

class Biblioteca: 

    # contructor
    def __init__(self) -> Type[None]:
        self.__lista_de_livros = []

    # methods
    def cadastrar_livro(self, livro: Type[Livro]) -> Type[None]:
        self.__lista_de_livros.append(livro)

    def listar_livros(self) -> Type[None]:
        cadastrados = 15 * '*' + ' Livros disponíveis ' + 15 * '*' + '\n\n'

        for item in self.__lista_de_livros:
            cadastrados += f'Titulo: {item.get_titulo()} - {item.get_autor()} : {item.get_ano()}, {item.get_id()}\n'

        cadastrados += '\n' + '*' * 50

        return cadastrados
    