import random
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Auluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno '))
lista_original = [ a1, a2, a3, a4 ]
random.shuffle(lista_original)
print('Nova listagem dos alunos é:')
print(lista_original)
