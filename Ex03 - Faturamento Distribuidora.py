'''
Para este exercício, pesquisei mais afubdo como obter dados fictícios e, descobri a biblioteca Faker().

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
    • O menor valor de faturamento ocorrido em um dia do mês;
    • O maior valor de faturamento ocorrido em um dia do mês;
    • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
import json


# Abrindo o arquivo "Ex03-Distribuidora.json"
with open('Ex03-Distribuidora.json', 'r') as arquivo:
    dados = json.load(arquivo)


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
faturamento = []


for meses in dados['faturamento']:# Acessa "Meses : Dias" 

    for dias in meses.values():# Acessa "Dias" em Meses
        valor = 0

        for valor_dia in dias.values():# Acessa "Valores" dos dias
            
            if valor_dia == 0:
                continue
            else:
                valor += valor_dia

        faturamento.append(valor)


            
    
    # Extrair os valores de faturamento de todos os dias
        # for dia, valor in dias.items():

        



# valores = list(dias.values()) # Pega o Faturamento mensal de cada mês em forma de lista
# print(sum(valores))
# faturamento.append(dia)