#modulo para atv pro tip1
"""
modulo de criação e teste sobre modulos
"""

def multiplo(num):
    """
    função para que verifique os multiplos de 5/7 ou de ambos
    """
    if (num % 5 == 0)and(num % 7 == 0):
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Fizz')
    elif num % 7 == 0:
        print('buzz')
    else:
        print('miss')
