import PySimpleGUI as sg

def login_window():
    [sg.theme('Reddit')]
    layout = [
        [sg.Text('Usuário:'), sg.Input(key='usuario', size=(10, 1))],
        [sg.Text('Senha: '), sg.Input(key='senha', password_char='*', size=(10, 1))],
        [sg.Button('Fazer login')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def message_erro_window():
    [sg.theme('Reddit')]
    layout = [
        [sg.Text('Usuário e senha inválidos')],
        [sg.Button('Voltar'), sg.Button('Sair')]
    ]
    return sg.Window('Usuário ou senha inválidos', layout=layout, finalize=True)


def message_window():

    prize_congratulations0 = ('Tenha um feliz aniversário cheio de sorrisos e')
    prize_congratulations1 = ('gargalhadas repleto de paz amor e muita alegria.')
    prize_congratulations2 = ('Parabéns por mais um ano de vida!')
    prize_text = ('Feliz Aniversário Lekitaaa!')
    prize_lines = '=' * 80
    prize_art = (""""
          iiiiiiiiiiiiiiiiiii
     |||||||H|A|P|P|Y|||||||
__|____________|__
  |\/\/\/\/\/\/\/\/\/\/\/\/\/\|
  ||||||B|I|R|T|H|D|A|Y||||||
  |,,,,,,,,,,,,,,,,,,,,,,,,,,|
 """)

    [sg.theme('Reddit')]
    layout = [
        [sg.Text(f'{prize_lines}\n\n{prize_art}\n\n{prize_congratulations0:^130}\n{prize_congratulations1:^130}'
                 f'\n{prize_congratulations2:^130}\n\n\n{prize_text:^130}\n{prize_lines}:')]
    ]
    return sg.Window('Feliz aniverssário', layout=layout, finalize=True)


window_login, window_erro, window_message = login_window(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == window_login and event == sg.WINDOW_CLOSED:
        break
    if window == window_erro and event == sg.WINDOW_CLOSED:
        break
    if window == window_message and event == sg.WINDOW_CLOSED:
        break

    if window == window_login and event == 'Fazer login':
        if values['usuario'] == 'Aleck' and values['senha'] == '123':
            window_message = message_window()
            window_login.hide()
        if values['usuario'] != 'Aleck' or values['senha'] != '123':
            window_erro = message_erro_window()
            window_login.hide()
    if window == window_erro and event == 'Voltar':
        window_login.un_hide()
        window_erro.hide()
    if window == window_erro and event == 'Sair':
        break
