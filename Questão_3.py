#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import pandas as pd
import json
with open('dados.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

df = pd.DataFrame(dados)

df_filtrado = df[df['valor'] != 0.0]

menor_valor = df_filtrado['valor'].min()

maior_valor = df_filtrado['valor'].max()

media_faturamento = df_filtrado['valor'].mean()

dias_acima_da_media = df_filtrado[df_filtrado['valor'] > media_faturamento].shape[0]

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
