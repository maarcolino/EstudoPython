# Open é uma função que permite abrir um arquivo
# ler ou escrever neste arquivo
arq = open("dados.txt","a")
# A função write (a) , permite escrever em um arquivo
arq.write("Ola\n")
# a função close fecha o arquivo retirando-o da 
# memória
arq.close()