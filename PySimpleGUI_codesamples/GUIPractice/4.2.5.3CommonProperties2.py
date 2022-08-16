import PySimpleGUI as sg

layout = [
    [sg.Text('オリジナルテキスト')],
    [sg.Text('-' * 100)],
    [sg.Text('テキスト1', pad=(50, 0))],
    [sg.Text('-' * 100)],
    [sg.Text('テキスト2', pad=(150, 100))],
    [sg.Text('-' * 100)],
    [sg.Text('テキスト3', pad=((50, 200),(0, 100)))],
    [sg.Text('-' * 100)],
]

window = sg.Window('ウィジェット位置の設定', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()