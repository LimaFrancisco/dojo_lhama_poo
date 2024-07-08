from typing import Type

class Email:

    # constructor
    def __init__(self, descricao: Type[str], texto: Type[str]) -> Type[None]:
        self.__descricao = descricao
        self.__texto = texto
        self.__destinatario = []

    # methods
    def inserir_destinatario(self, destinatario: Type[str]) -> Type[None]:
        self.__destinatario.append(destinatario)

    def mostrar_email(self) -> Type[str]:
        conteudo = f'\ndescricao: {self.__descricao}\n'
        for item in range(len(self.__destinatario)):
            conteudo += self.__destinatario[item] + ', '
        
        conteudo += f'\n{self.__texto}\n'
        return conteudo
