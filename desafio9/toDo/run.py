from typing import Type
from model import Pessoa
from sistema_de_login import SistemDeLogin

class TextoSecreto:
    def apresentar_texto(self, sistema: Type[SistemDeLogin], pessoa: Type[Pessoa]):
        lista_de_cadastrados = sistema.exibir_usuarios_cadastrados().split()
        if pessoa.get_nome() in lista_de_cadastrados:
            print('Ola, esse é meu texto secreto!')
        else:
            print('Pessoa não cadastrada')

texto_secreto = TextoSecreto()
texto_secreto.apresentar_texto


nattan = Pessoa('Nattan', 21, '4123412341234')
fabio = Pessoa('Fabio', 19, '2134123412')
maria = Pessoa('Maria', 25, '34214123412')
fernando = Pessoa('Fernando', 25, '34214123412')

sistema = SistemDeLogin()

sistema.cadastrar_usuario(nattan, 'AA##aa**e')
sistema.cadastrar_usuario(fabio, 'AA##aa**e')
sistema.cadastrar_usuario(maria, 'AA##aa**d')
# sistema.cadastrar_usuario(fernando, 'AA##aa**d')

print(sistema.exibir_usuarios_cadastrados())

texto_secreto = TextoSecreto()
texto_secreto.apresentar_texto(sistema, nattan)
texto_secreto.apresentar_texto(sistema, fernando)
