print("Este programa analisa finais de placa de acordo com o rodizio veícular.")
digito = input("Entre com um número e 0 a 9: ")

match digito:
    case '1' | '2':
        print("Na Segunda-Feira você não pode rodar.")
    case '3' | '4':
        print("Na Terça-Feira você não pode rodar.")
    case '5' | '6':
        print("Na Quarta-Feira você não pode rodar.")
    case '7' | '8':
       print("Na Quinta-Feira você não pode rodar.")
    case '9' | '0':
        print("Na Sexta-Feira você não pode rodar.")