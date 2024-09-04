'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código
'''

from colorama import Fore


green = Fore.GREEN
red = Fore.RED
reset = Fore.RESET


def pertence_fibonacci(numero):
    fibonacci = [0, 1]

    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return numero in fibonacci


# Lista de números a serem verificados
valores = [0, 5, 6, 7, 8, -34, 55.9, 89]
lista = ', '.join(str(num) for num in valores)


print(f'Dos valore, quais pertencem, e quais não:\n{lista}\n')

# Verifica cada número
for valor in valores:
    if pertence_fibonacci(valor):
        print(f"{green}>>>{reset} {valor} {green}pertence{reset} à sequência de Fibonacci.")
    else:
        print(f"{red}>>>{reset} {valor} {red}NÃO pertence{reset} à sequência de Fibonacci.")

print()
