# Conversor de numeros



user_option = 1

while (user_option < 4):
    num_user = int(input('\nDigite um numero: '))

    print('''\nEscolha uma das conversões
    [1] - numero em binario
    [2] - numero em octal
    [3] - numero em hexadecimal
    [4] - Sair.
    [0] - voltar.
    ''')

    user_option = int(input('\nSua opção: '))
    if user_option == 4:
        break
    else:
        while True:
            if user_option == 1:
                print(f'\nSeu numero em binario: {bin(num_user)[2:]}\n')
                user_option = int(input('Sua opção: '))
            elif user_option == 2:
                print(f'\nSeu numero em octal: {oct(num_user)[2:]}\n')
                user_option = int(input('Sua opção: '))
            elif user_option == 3:
                print(f'\nSeu numero em hexadecimal: {hex(num_user)[2:]}\n')
                user_option = int(input('Sua opção: '))
            elif user_option == 0:
                break
            elif user_option == 4:
                break
            else:
                print('\nDigite uma opção válida.\n')
                user_option = int(input('Sua opção: '))