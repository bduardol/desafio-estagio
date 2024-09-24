'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, 
na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
Estes dias devem ser ignorados no cálculo da média;'''

import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

count = 0
total = 0
dia_min, dia_max, min, max = int(), int(), 999999999, 0
maior_media = 0

for i in dados:
    if list(i.values())[1] != 0:
        count+=1
        if list(i.values())[1] < min:
            dia_min = list(i.values())[0]
            min = list(i.values())[1]
        if list(i.values())[1] > max:
            dia_max = list(i.values())[0]
            max = list(i.values())[1]

    total+=list(i.values())[1]

media = total/count

for i in dados:
    if list(i.values())[1] > media:
        maior_media += 1


print(f'O dia com o menor faturamento do mês foi o dia {dia_min}.')
print(f'O dia com o maior faturamento do mês foi o dia {dia_max}.')
print(f'O número de dias no mês em que o faturamento diário superou a média mensal foi de {maior_media} dia(s).')

