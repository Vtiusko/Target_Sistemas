import json
from faker import Faker
import random
import calendar

fk = Faker('pt_BR')  # Define a localidade para português do Brasil


def gerar_dados_distribuidora(ano):

    distribuidora = {
        'nome': fk.company(),
        'endereco': fk.address(),
        'telefone': fk.phone_number(),
        'cnpj': fk.cnpj(),
        'faturamento' : {}
    }
    
    meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro']

    for i, mes in enumerate(meses):
        num_dias = calendar.monthrange(ano, i + 1)[1] # Com esse [1], estamos acessando o 2º elemento da tupla, que no caso é: Dia
        faturamento_mes = {}

        for dia in range(1, num_dias + 1):
            faturamento_mes[f'dia {dia}'] = random.randint(0, 1000)

        distribuidora['faturamento'][f'{mes}'] = faturamento_mes
    
    return distribuidora


# Exemplo de uso, gerando dados para o ano de 2024
dados_distribuidora = gerar_dados_distribuidora(2024)


# Salvando em um arquivo JSON
with open('distribuidora.json', 'w', encoding='utf-8') as f:
    json.dump(dados_distribuidora, f, indent=4, default=str)