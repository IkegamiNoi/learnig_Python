import PySimpleGUI as sg

layout = [
    [sg.Text('テキストを表示します')],
    [sg.InputText()],
    [sg.Button('ボタン１')]
]

window = sg.Window('windowのタイトル', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()