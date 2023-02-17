from PySimpleGUI import PySimpleGUI as sg

# Layout

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='Usuário', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char="*", size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Janela

janela = sg.Window('Tela de Login', layout)

# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'Gabriel' and valores['Senha'] == '123456':
            print('Bem-Vindo à sua primeira página de login')