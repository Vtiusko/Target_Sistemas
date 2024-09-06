'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
'''
from colorama import Fore

# Cor
ciano = Fore.CYAN
resetar = Fore.RESET


estados = ['SP', 'RJ', 'MG', 'ES', 'Outros']
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]


print(f'{ciano}{" ANÁLISE FATURAMENTO MENSAL ":=^63}{resetar}',end='\n\n')

for i in range(len(estados)):
    valor = faturamento[i] # Valor de cada estado
    faturamento_total = sum(faturamento)

    margem = valor / faturamento_total

    print(f'>>> {ciano}{estados[i]}{resetar} representou {ciano}{margem:.2%}{resetar} no faturamento total da empresa.')

print()