#opcao = -1

#while opcao != 0:
#    opcao = int (input('[1] Sacar \n[2] Extrato \n[0] Sair:\n'))

#    if opcao == 1:
 #       print('sacando...')
#    elif opcao == 2:
#        print("Extrato")

for numero in range (1, 101):
    if numero % 2 == 1:
        continue
    print (numero, end=" ")