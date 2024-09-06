import json
from faker import Faker
from datetime import date
from random import randint
from calendar import monthrange


fk = Faker('pt_BR')


def gerar_dados_distribuidora(ano):
    distribuidora = {
        'nome': fk.company(),
        'endereco': fk.address(),
        'telefone': fk.phone_number(),
        'cnpj': fk.cnpj(),
        'faturamento': []
    }

    meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro']

    for mes in meses:
        faturamento_mes = {}

        for dia in range(1, monthrange(ano, meses.index(mes) + 1)[1] + 1):

            # Data recebe dados do ano de 2024
            data = date(ano, meses.index(mes) + 1, dia)

            # Se a data for sábado(índice 5) ou domingo(índice 6)
            valor = 0 if data.weekday() >= 5 else randint(0, 1000)

            faturamento_mes[f"dia {dia}"] = valor

        distribuidora['faturamento'].append({mes: faturamento_mes})

    return distribuidora


# Exemplo de uso, gerando dados para o ano de 2024
dados_distribuidora = gerar_dados_distribuidora(2024)

# Salvando em um arquivo JSON
with open('Ex03-Distribuidora.json', 'w', encoding='utf-8') as f:
    json.dump(dados_distribuidora, f, indent=4)