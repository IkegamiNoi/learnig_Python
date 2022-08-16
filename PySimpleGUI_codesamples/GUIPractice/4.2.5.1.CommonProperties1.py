import PySimpleGUI as sg

layout = [
    [sg.Text('オリジナルテキスト')],
    [sg.Text('テキスト１', text_color='#008000')],
    [sg.Text('テキスト２', text_color='white')],
    [sg.Text('テキスト３', text_color='#ff0000')],
]

window = sg.Window('テキストカラーの設定', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
