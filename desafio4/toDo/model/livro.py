from typing import Type

class Livro:

    # constructor
    def __init__(self, titulo: Type[str], autor: Type[str], ano: Type[int], id: Type[int]) -> Type[None]:
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__id = id

    # method
    def get_titulo(self) -> Type[str]:
        return self.__titulo

    def get_autor(self) -> Type[str]:
        return self.__autor

    def get_ano(self) -> Type[int]:
        return self.__ano
    
    def get_id(self) -> Type[int]:
        return self.__id
    