from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*',
    size=(20,1))],
    [sg.Button('Entrar')],
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Aleck' and valores['senha'] == '123456':
            print('Bem-Vendo, Aleck!')

