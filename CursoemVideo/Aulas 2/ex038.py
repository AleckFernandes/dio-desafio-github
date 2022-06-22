user_option = 0
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

while user_option < 1:
    print('='*30)
    value_one = int(input('\nPrimeiro valor: '))
    value_two = int(input('\nSegundo valor: '))
    if user_option > 2:
        break
    else:
        if value_one > value_two:
            print(bcolors.OK + '\nO primeiro valor é maior.\n'+ bcolors.RESET)
            print('=' * 30)
            print(bcolors.OK + '\n0 - Nova comparação.' + bcolors.RESET, bcolors.FAIL + '\n1 - Sair.' + bcolors.RESET)
            user_option = int(input(''))
        elif value_two > value_one:
            print(bcolors.OK +'\nO segundo valor é maior.\n'+ bcolors.RESET)
            print('=' * 30)
            print(bcolors.OK +'\n0 - Nova comparação.'+ bcolors.RESET, bcolors.FAIL +'\n1 - Sair.'+ bcolors.RESET)
            user_option = int(input(''))
        else:
            print(bcolors.WARNING + '\nNão existe valor maior entre o primeiro valor e o segundo valor.\n'+ bcolors.RESET)
            print('=' * 30)
            print(bcolors.OK + '\n0 - Nova comparação.' + bcolors.RESET, bcolors.FAIL + '\n1 - Sair.' + bcolors.RESET)
            user_option = int(input(''))