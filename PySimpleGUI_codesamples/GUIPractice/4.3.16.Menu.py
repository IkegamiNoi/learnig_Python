import PySimpleGUI as sg

menu_layout = [['File', ['Open', 'Save']],
               ['Edit', ['Paste', 'Redo', 'Undo']],
               ['Popup', ['Hello']],
               ]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Menuの設定')],
]

window = sg.Window('Menuの設定', layout, size=(300, 100), finalize=True)

while True:
    event, value = window.read()  # イベント入力を待つ

    if event == 'Hello':
        sg.popup('Hello Popup')

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
