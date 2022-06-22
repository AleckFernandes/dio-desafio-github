def main():
    user_true = 'Aleck'
    try_again = 'Y'
    while try_again:
        user = str(input('Digite seu usuário: '))
        if user == user_true:
            verify_password()
            break
        else:
            try_again = input('Usuário incorreto\n Deseja tentar novamente? Y/N \n')
            if try_again == 'Y':
                pass
            elif try_again == 'N':
                print('Você escolheu sair')
                break
            else:
                print('Digite uma alternativa válida.')
                break
def verify_password():
    password_true = 1337
    try_again = 'Y'
    while try_again:
        password = int(input('Digite sua senha: '))
        if password == password_true:
            print('Parabéns, você fez login com sucesso!')
            break
        else:
            try_again = input('Senha incorreta\n Deseja tentar novamente? Y/N \n')
            if try_again == 'Y':
                pass
            elif try_again == 'N':
                print('Você escolheu sair')
                break
            else:
                print('Digite uma alternativa válida.')
                break

main()