from typing import Type
from model import Pessoa

class SistemDeLogin:

    # constructor
    def __init__(self) -> Type[None]:
        self.__usuarios_cadastrados = [] 

    # main methods
    def cadastrar_usuario(self, usuario: Type[Pessoa], senha: Type[str]) -> Type[None]:
        if self.__verificar_senha(senha):
            self.__usuarios_cadastrados.append(usuario)
        else:
            raise ValueError ('Senha Invalida')

    def exibir_usuarios_cadastrados(self) -> Type[str]:
        usuarios = ''
        for usuario in self.__usuarios_cadastrados:
            usuarios += usuario.get_nome() + '\n'

        return usuarios

    # complementary methods
    def __verificar_senha(self, senha) -> Type[bool] :
        if (len(senha) >= 8) and (senha.lower() != senha and senha.upper() != senha): 
            return True
        else: 
            return False
