'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
 faça um programa, na linguagem que desejar, que calcule e retorne: 
• O menor valor de faturamento ocorrido em um dia do mês; 
• O maior valor de faturamento ocorrido em um dia do mês; 
• Número de dias no mês em que o valor de faturamento diário foi superior 
à média mensal. 

IMPORTANTE: 
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
Estes dias devem ser ignorados no cálculo da média; 

'''
import json
from collections import namedtuple

# Definindo o namedtuple
Faturamento = namedtuple('Faturamento', ['dia', 'valor'])

#--------------------------------------Resgatando os dados

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    #print(dados)

faturamentos = [Faturamento(**item) for item in dados]

#--------------------------------------Resgatando os faturamentos válidos
soma = 0.0
listaFaturamento = []

for item in faturamentos:
    if item.valor >0:
        soma += item.valor       
        listaFaturamento.append(item.valor)

#--------------------------------------Realizando as verificações 
if listaFaturamento:
    media = soma / len(listaFaturamento)
    #print(len(listaFaturamento))
    
else:
    media = 0

menorValor = min(listaFaturamento, default=0)
maiorValor = max(listaFaturamento, default=0)
contador = 0

for item in listaFaturamento:
    if item > media:
        contador += 1    

#--------------------------------------Retornando 

print(f'O maior valor foi de {maiorValor}')
print(f'O menor valor foi de {menorValor}')
print(f'A media de faturamento foi {media}')
print(f'O número de dias acima da média de faturamento foi {contador}')
