'''
Para este exercício, pesquisei mais afundo como obter dados fictícios(já que não conseguia encontrar algum arquivo em JSON ou XML) e, descobri a biblioteca Faker().

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
    • O menor valor de faturamento ocorrido em um dia do mês;
    • O maior valor de faturamento ocorrido em um dia do mês;
    • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
from colorama import Fore
import json


# Cor
ciano = Fore.CYAN
resetar = Fore.RESET


# Abrindo o arquivo "Ex03-Distribuidora.json"
with open('Ex03-Distribuidora.json', 'r') as arquivo:
    dados = json.load(arquivo)


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

faturamento = []
dias_acima_media = []
maior_faturamento = []
menor_faturamento = []
media_meses = []


for dados_mensais in dados['faturamento']: # Acessa "Meses : Dias" 

    for dias in dados_mensais.values(): # Acessa "Dias" em Meses
        fat_mensal = [] # Lista auxiliar

        for valor_dia in dias.values(): # Acessa "Valores" dos dias

            if valor_dia == 0:
                continue
            else:
                fat_mensal.append(valor_dia)
        

        media_mes = sum(fat_mensal) / len(fat_mensal) # Calcula a média mensal
        media_alta = sum(1 for valor in fat_mensal if valor > media_mes) # Conta +1 para cada valor acima da média
 
 
        maior_faturamento.append(max(fat_mensal)) # Maior faturamento
        menor_faturamento.append(min(fat_mensal)) # Menor faturamento
        dias_acima_media.append(media_alta) # Adiciona quantidade de dias acima da média
        media_meses.append(f'{media_mes:.2f}') # Adiciona a média


# =============================================================================
# ============================================================ TELA DE MENSAGEM
print(f'{ciano}{" ANÁLISE FATURAMENTO MENSAL ":=^115}{resetar}',end='\n\n')

for i in range(len(meses)):
    mes = f'{meses[i] + " ":-<13}'
    menor_valor = f'{str(menor_faturamento[i]) + " ":-<6}'
    maior_valor = f'{str(maior_faturamento[i]) + " ":-<7}'
    acima_media = f'{str(dias_acima_media[i]):-<5}'
    media = f'{str(media_meses[i]):<10}'

    print(f'>>> {ciano}{mes}{resetar} Menor valor: {ciano}R$ {menor_valor}{resetar} Maior valor: {ciano}R$ {maior_valor}{resetar} Dias acima da média: {ciano}{acima_media}{resetar} Media mensal: {ciano}R$ {media}{resetar}')

print()