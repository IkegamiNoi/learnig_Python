import PySimpleGUI as sg

layout = [
    [sg.Multiline(default_text='あらかじめ表示させたい文字列', size=(30, 6),
                  text_color='#ff0000')],
]

window = sg.Window('Multiline', layout, size=(300, 150), finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
