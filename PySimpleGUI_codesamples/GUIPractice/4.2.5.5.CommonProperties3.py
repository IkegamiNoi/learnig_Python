import PySimpleGUI as sg

layout = [
    [sg.Text('オリジナルテキスト')],
    [sg.Text('-' * 100)],
    [sg.Text('テキスト１', pad=(50, 0), visible=False)],
    [sg.Text('-' * 100)],
    [sg.Button('ボタン１', key='-Btn1-')],
    [sg.Text('-' * 100)],
    [sg.Button('ボタン２', key='-Btn2-',
               disabled=True, disabled_button_color=('Red',''))],
    [sg.Text('-' * 100)],
]

window = sg.Window('ウィジェットの無効化', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == '-Btn1-':
        window['-Btn2-'].Update(disabled=False)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()