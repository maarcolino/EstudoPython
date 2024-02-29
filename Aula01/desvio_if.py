#Pede um numero e vê se é par ou impar
numero = input("Digite um número:")
# É necessário realizar a conversão de texto para
# número, pois a função input sempre retona o valor
# em formato de texto. então, utilizamos a função
# int para converter a variável numero em valor
# numérico nteiro e assim realizar os cálculos
# necessários
numero = int(numero)


if(numero % 2 == 0):
    print("O número digitado é par")
else:
    print("O número digitado é Impar")