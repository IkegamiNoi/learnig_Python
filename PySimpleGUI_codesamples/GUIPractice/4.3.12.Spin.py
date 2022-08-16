import PySimpleGUI as sg

layout = [
    [sg.Text('年齢を入力して下さい。')],
    [sg.Spin(values=[i for i in range(20, 40)], key='-Spin1-')],
    [sg.Button('入力確認', key='-Btn-')]
]

window = sg.Window('Spin', layout,finalize=True)

while True:
    event, value = window.read()  # イベントの入力を待つ

    if event == '-Btn-':
        message = 'あなたの年齢は、' + str(value['-Spin1-']) + '才で間違いありませんか？'
        sg.popup(message)
        break

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
