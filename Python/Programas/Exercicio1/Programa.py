import Prato
import Garrafa
import Detergente

pratoVerde = Prato.Prato(300, "Verde")
pratoAzul = Prato.Prato(250, "Azul")
pratoAmarelo = Prato.Prato(350, "Amarelo")

garrafaDeCafe = Garrafa.Garrafa(500)

detergente = Detergente.Detergente(250)

sair = False

while (not sair):
    print ("")
    print ("#######################################")
    print ("Digite a opção para fazer uma ação")
    print ("Opções: ")
    print ("1 - Encher Prato")
    print ("2 - Encher Garrafa")
    print ("3 - Esvaziar Prato")
    print ("4 - Esvaziar Garrafa")
    print ("5 - Limpar Prato")
    print ("6 - Limpar Garrafa")
    print ("7 - Listar Pratos")
    print ("8 - Listar Garrafas")
    print ("9 - Verificar quantidade de detergente")
    print ("0 - Sair")

    option =int(input ("Escolher: "))
    if(option == 1):
        print ("Qual prato você quer encher? ")
        print ("1 - Prato azul")
        print ("2 - Prato verde")
        print ("3 - Prato amarelo")
        prato = int(input("Escolher: "))
        if(prato == 1):
            pratoAzul.encherPrato()
        elif (prato == 2):
            pratoVerde.encherPrato()
        elif (prato == 3):
            pratoAmarelo.encherPrato()
        else:
            print ("Opção Inválida. Digite um número que esteja na lista de opções (de 1 a 3)")
    elif (option == 7):
        print ("O prato",pratoAmarelo.cor,"esta com",pratoAmarelo.quantidadeNoPrato,"ml de sopa. O prato esta", "sujo" if pratoAmarelo.estaSujo else "limpo")
        print ("O prato",pratoVerde.cor,"esta com",pratoVerde.quantidadeNoPrato,"ml de sopa. O prato esta", "sujo" if pratoVerde.estaSujo else "limpo")
        print ("O prato",pratoAzul.cor,"esta com",pratoAzul.quantidadeNoPrato,"ml de sopa. O prato esta", "sujo" if pratoAzul.estaSujo else "limpo")
    elif(option == 0):
        print ("Saindo...")
        sair = True