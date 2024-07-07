from model import Destino

while (True):

    destino_da_viajem = input('Selecione o destino da viajem: ')

    destino = Destino(destino_da_viajem)

    print(f'{destino.mostrar_dados()}\n')
