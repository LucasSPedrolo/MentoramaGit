#atv de numeros naturais
"""retorna os multiplos por 7/5 ou ambos"""
from moduloATV.VerNum import multiplo

NumeroNatural = int(input('coloque um numero natural '))
def numero_natural(num):
    """
    verifica se o valor é maior que 0
    """
    if num < 0:
        print('coloque um numero natural positivo')
if numero_natural(NumeroNatural):
    multiplo(NumeroNatural)
