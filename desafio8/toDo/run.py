from calculadoras import PrimeiraCalculadora
from calculadoras import SegundaCalculadora

primeira_calculadora = PrimeiraCalculadora()
segunda_calculadora = SegundaCalculadora()


print('************ PRIMEIRA CALCULADORA ************')
resultado = primeira_calculadora.calcular(2,1)
print(f'resultado para 2 e 1: {resultado:.2f}')

resultado = primeira_calculadora.calcular(4,5)
print(f'resultado para 4 e 5: {resultado:.2f}')

print('************ SEGUNDA CALCULADORA ************')
resultado = segunda_calculadora.calcular(2,1)
print(f'resultado para 2 e 1: {resultado:.2f}')

resultado = segunda_calculadora.calcular(4,5)
print(f'resultado para 4 e 5: {resultado:.2f}')
