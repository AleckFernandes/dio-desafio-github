# Enunciado da questão:
#
# Faça um algoritmo para ler um número que é um código de usuário.
#
# Caso este código seja diferente de um código armazenado internamente no algoritmo
# (igual a 1234) deve ser apresentada a mensagem "Usuário inválido!" e o sistema será encerrado.
#
# Caso o código seja correto, deve ser lido outro valor que é a senha.
#
# Se a senha estiver correta (a certa é 9999), deve ser exibida a mensagem "Acesso permitido".
#
# Se a senha estiver incorreta deve ser exibida a mensagem "Senha incorreta", e também uma mensagem com as seguintes opções:
#
# 1 - tentar novamente
# 0 - encerrar sistema
#

def main():
    user_true = 'Alecsia'
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
                pass


def verify_password():
    password_true = 3.14
    try_again = 'Y'
    prize_congratulations = (' Tenha um feliz aniversário cheio de sorrisos e  =\n'
                            '= gargalhadas repleto de paz amor e muita alegria.=\n'
                            '=       Parabéns por mais um ano de vida!')
    prize_text = ('Aproveite a viagem!')
    prize_lines = '=' * 51
    while try_again:
        password = float(input('Digite a senha \n Dica Pi = ?: '))
        if password == password_true:
            print('''quu..__
             $$$b  `---.__
              "$$b        `--.                          ___.---uuudP
               `$$b           `.__.------.__     __.---'      $$$$"              .
                 "$b          -'            `-.-'            $$$"              .'|
                   ".                                       d$"             _.'  |
                     `.   /                              ..."             .'     |
                       `./                           ..::-'            _.'       |
                        /                         .:::-'            .-'         .'
                       :                          ::''\          _.'            |
                      .' .-.             .-.           `.      .'               |
                      : /'$$|           .@"$\           `.   .'              _.-'
                     .'|$u$$|          |$$,$$|           |  <            _.-'
                     | `:$$:'          :$$$$$:           `.  `.       .-'
                     :                  `"--'             |    `-.     
                    :##.       ==             .###.       `.      `.    `
                    |##:                      :###:        |        >     >
                    |#'     `..'`..'          `###'        x:      /     /
                     \                                   xXX|     /    ./
                      \                                xXXX'|    /   ./
                      /`-.                                  `.  /   /
                     :    `-  ...........,                   | /  .'
                     |         ``:::::::'       .            |<    `.
                     |             ```          |           x| \ `.:``.
                     |                         .'    /'   xXX|  `:`M`M':.
                     |    |                    ;    /:' xXXX'|  -'MMMMM:'
                     `.  .'                   :    /:'       |-'MMMM.-'
                      |  |                   .'   /'        .'MMM.-'
                      `'`'                   :  ,'          |MMM<
                        |                     `'            |tbap
                         \                                  :MM.-'
                          \                 |              .''
                           \.               `.            /
                            /     .:::::::.. :           /
                           |     .:::::::::::`.         /
                           |   .:::------------\       /
                          /   .''               >::'  /
                          `',:                 :    .'
                                               `:.:' ''')
            print(prize_lines)
            print('=', ' ' * 47, '=')
            print('=', ' ' * 47, '=')
            print('=', ' ' * 47, '=')
            print('=', ' ' * 47, '=')
            print('=', ' ' * 47, '=')
            print('='+prize_congratulations.center(48)+' '*8, '=')
            print('=', ' ' * 47, '=')
            print('=', ' ' * 47, '=')
            print('='+prize_text.center(49)+'=')
            print('=', ' ' * 47, '=')
            print('=', ' ' * 47, '=')
            print('=', ' ' * 47, '=')
            print(prize_lines)
            import donut
            break
        else:
            try_again = input('Senha incorreta\n Deseja tentar novamente? Y/N \n')
            if try_again == 'Y':
                pass
            elif try_again == 'N':
                print('Você escolheu sair.')
                break
            else:
                print('Digite uma alternativa válida.')
                pass


main()