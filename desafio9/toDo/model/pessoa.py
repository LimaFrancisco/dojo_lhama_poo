from typing import Type

class Pessoa:

    def __init__(self, nome: Type[str], idade: Type[int], CPF: Type[str]) -> Type[None]:
        self.__nome = nome
        self.__idade = idade
        self.__CPF = CPF

    def get_nome(self) -> Type[str]:
        return self.__nome  
    
    def get_idade(self) -> Type[int]:
        return self.__idade  

    def get_CPF(self) -> Type[str]:
        return self.__CPF     
