#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 


from tabulate import tabulate
lista = [
{"UF": "SP", "Faturamento": 67836.43},
{"UF": "RJ", "Faturamento": 36678.66},
{"UF": "MG", "Faturamento": 29229.88},
{"UF": "ES", "Faturamento": 27165.48},
{"UF": "Outros", "Faturamento": 19849.53}
]

soma_por_estado = {}
soma_total = 0

# Iterar sobre os dados e somar valores por estado
for item in lista:
    estado = item["UF"]
    valor = item["Faturamento"]
    if estado in soma_por_estado:
        soma_por_estado[estado] += valor
    else:
        soma_por_estado[estado] = valor

    soma_total += valor

# Exibir o resultado
print(f"Total de faturamento R${soma_total:.2f}")

for uf, total  in soma_por_estado.items():
    print(f"Total de faturamento no estado {uf}: R${total:.2f}, {(total/soma_total)*100:.2f}")
