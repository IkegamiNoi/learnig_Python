import PySimpleGUI as sg

layout = [
    [sg.Text(text="表示させたい文字列", text_color='#ff0000')],
    [sg.Input(key='-Input-')],
    [sg.Button('ボタン', key='-Btn-')]
]

window = sg.Window('FirstGUI', layout, size=(300, 150), finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == '-Btn-':
        message = values['-Input-']
        sg.popup(message)
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()