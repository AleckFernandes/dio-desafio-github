#1. Quais são os dados de entrada necessários?
#2. O que devo fazer com estes dados?
#3. Quais as retrições desse problema?
#4. Qual é o resultado esperado?
#5. Qual é a sequencia de passos a ser feita para
#chegar ao resultado esperado ?

'''num_delay = int(input('Qunatas vezes você chegou atrasado ?'))

if num_delay >= 3:
    print('Não, você está suspenso.')
elif num_delay == 1:
    print('Sim, você pode entrar, mas só pode atrasar mais 2 vezes')
elif num_delay == 2:
    print('Sim, você pode entrar, mas só pode atrasar mais 1 vezes')
else:
    print('Sem, pode entrar.')
'''

num_one = int(input('Digite o primeiro valor: '))
num_two = int(input('Digite o segundo valor: '))

if num_one > num_two:
    print('o primeiro valor é maior que o segundo!')
else:
    print('O segundo valor é maior!')