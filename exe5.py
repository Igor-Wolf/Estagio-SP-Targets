'''
5) Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: 
a) Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código; 
b) Evite usar funções prontas, como, por exemplo, reverse; 

NÃO SE ESQUEÇA DE INSERIR O LINK DO SEU REPOSITÓRIO NO GITHUB COM O 
CÓDIGO FONTE QUE VOCÊ DESENVOLVEU

'''

palavra = "paralelepipedo"
reverso = []

for i in range(len(palavra)):
    reverso.append(palavra[len(palavra)-1-i])

final = ''.join(reverso)
print(final)