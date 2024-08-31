'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
 informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 
'''

firstNumber = 0
secondNumber = 1
result = 0
listFibo = []

# valor definido
userNumber = 57 

listFibo.append(secondNumber)

for i in range(userNumber):
    result = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = result
    if userNumber <=0:
        break
    elif result <= userNumber:
        listFibo.append(result)
    else:
        break

# for i in listFibo:
#     print(i)

if userNumber <= 0:
    print(f'{userNumber} não pertence à sequencia fibonacci')
elif userNumber in listFibo:
    print(f'{userNumber} pertence à sequencia fibonacci')
else:
    print(f'{userNumber} não pertence à sequencia fibonacci')




