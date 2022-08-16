import PySimpleGUI as sg

layout = [
    [sg.Button('ONボタンのDisable解除', key='-Btn1-', pad=(50, 10))],
    [sg.Button(image_filename='button.png', key='-Btn2-', pad=(80, 0),
               disabled=True)],
]

window = sg.Window('Button', layout, size=(300, 150), finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == '-Btn1-':
        window['-Btn2-'].Update(disabled=False)

    if event == '-Btn2-':
        sg.popup('ONボタンが押されました！')

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
