from componentes import Elevador

while (True):
    elevadorId = int(input('Defina o elevador: '))
    elevador1 = Elevador(elevadorId)
    andar = int(input('Defina um andar: '))
    elevador1.mudar_andar(andar)

    print(elevador1.mostrar_andar_atual())
