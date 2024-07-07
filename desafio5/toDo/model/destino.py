from typing import Type

class Destino:

    def __init__(self, destino: Type[str]) -> Type[None]:
        self.__destino = self.__escolher_destino(destino)

    def mostrar_dados(self) -> Type[str]:
        return f'destino: {self.__destino}\natividade: {self.__fazer_atividade()}'

    def __fazer_atividade(self) -> Type[str]:
        if self.__destino == 'niteroi':
            return 'ir para a praia'
        elif self.__destino == 'belo horizonte':
            return 'visitar inhotim'
        elif self.__destino == 'fortaleza':
            return 'ir para beach park'
        else:
            return ''

    def __escolher_destino(self, destino: Type[str]) -> Type[str]:
        if destino in ['niteroi', 'belo horizonte', 'fortaleza']:
            return destino
        else:
            raise ValueError(f'Destino inválido: {destino}')
