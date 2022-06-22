#1. Quais são os dados de entrada necessários?
""""Girar o dado, sair"""
#2. O que devo fazer com estes dados?
""""Girar os dados = gerar 2 numeros radomicamente
sair = fechar o aplicativo"""
#3. Quais as retrições desse problema?
"""" Gerar apenas 2 numeros, sendo eles de 1 a 6"""
#4. Qual é o resultado esperado?
"""" uma interface grafica com botão de girar o dado e um botão de sair"""
#5. Qual é a sequencia de passos a ser feita para
"""" 
importar simplegui
text: apresentar um texto: 'Os números sorteados são:'
text: definir local onde irà fica os numeros
inputs: definir o local onde irão ficar os botões

"""
#chegar ao resultado esperado ?

import PySimpleGUI as sg
import random

dice_one_roll = random.randint(0, 6)
dice_two_roll = random.randint(0, 6)

def window():
    [sg.theme('DarkBlue9')]

    layout = [
        [sg.Text('Bem-vindo ao Sorteador de dados')],
        [sg.Button('Girar')], [sg.Button('Sair')],

    ]

    return sg.Window('Sorteador de Dados', layout=layout, finalize=True)


def results():
    dice_one = dice_one_roll
    dice_two = dice_two_roll

    [sg.theme('DarkBlue9')]

    layout = [
        [sg.Text('Números sorteados:')],
        [sg.Text(f'{dice_one} e {dice_two}')],
        [sg.Button('Girar Novamente')], [sg.Button('Sair')]
]
    return sg.Window('Sorteador de Dados', layout=layout, finalize=True)

window_dice = window()
window_roll = re(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == window_dice and event == sg.WINDOW_CLOSED:
        break
    if window == window_roll and event == sg.WINDOW_CLOSED:
        break
    if window == window_dice and event == 'Sair':
        break
    if window == window_roll and event == 'Sair':
        break
    if window == window_dice and event == 'Girar':
        window_roll = results()
        if window == window_roll and event == 'Girar Novamente':
            break
            # dice_one = (random.randint(0, 6))
            #
            # dice_two = (random.randint(0, 6))

