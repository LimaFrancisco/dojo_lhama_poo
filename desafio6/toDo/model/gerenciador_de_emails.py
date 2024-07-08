from .email import Email
from typing import Type

class GerenciadorDeEmails:

    # constructor
    def __init__(self, nome_da_empresa: Type[str], email_da_empresa: Type[str]) -> Type[None]:
        self.__nome_da_empresa = nome_da_empresa
        self.__email_da_empresa = email_da_empresa

    # methods
    def enviar_email(self, descricao: Type[str], texto: Type[str]) -> Type[Email]:
        email = Email(descricao, texto)
        return email