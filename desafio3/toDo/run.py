from models import Controlador, Pessoa

jogador1 = Pessoa('Fernando')
jogador2 = Pessoa('Thiago')
controle = Controlador(jogador1, jogador2)

while (True):
    input()
    resultado = controle.comecar_rodada()
    print(resultado)
    print()
    