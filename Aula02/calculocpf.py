print("Programa que verifica se o cpf é valido")
# Variável que guarda o cpf digitado pelo usuário

cpf_usuario = input("Digite seu cpf: ")
cpf_calc = ""

#essa variavel foi criada para calcular o peso
# de 10 até 2

peso10 = 10
peso11 = 11

# A variável resultado guarda a soma das multiplicações
# entre os digitos do cpf e os pesos
resultado = 0


# para obter os 9 primeiros digitos do cpf foi necessario
# usar uma estrutura "for" com uma contagem de 0 até 9

for i in range(0,9):

    # exibindo um digito por vez em tela

    print(cpf_usuario[i])

    cpf_calc += cpf_usuario
    print(int(cpf_usuario[i])*peso10)

    # Para calcular um digitor por vez com o peso foi
    # necessário converter cada digito em número inteiro
    # depois, somamos os resultados obtidos armazenando
    # na variável resultado.

    resultado+=int(cpf_usuario[i])*peso10

    # Todas as vezes que o laço "for" rodar, será subtraído
    # o valor 1 da variável "peso10"

    peso10-=1


# Exibindo o resultado encontrado

print(resultado)

# A variável resto, guarda o resto da divisão
resto = resultado % 11

# Se o resto da divisão for menor que 2, então o
# primeiro digito será 0(zero); Caso contrário o
# devemos subtrair 11 pelo valor encontrado em resto
if( resto < 2 ):
    print("Primeiro digito é 0")
    cpf_calc+="0"
else:
    print("Primeiro digito é "+str(11-resto))
    cpf_calc+=str(11-resto)


resultado = 0
for i in range(0,10):
    resultado+=int(cpf_calc[i]*peso10)


resto = resultado % 11
if(resto < 2):
    cpf_calc+="0"
else:
    cpf_calc+=str(11-resto)


if(cpf_usuario==cpf_calc):
    print("CPF é válido")
else:
    print("CPF inválido")