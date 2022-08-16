import PySimpleGUI as sg

layout = [
    [sg.Text('旅行に行きたい場所を１つ選択するか、入力して下さい')],
    [sg.Combo(('北海道', '東京', '大阪'), key='-Destination-', size=(10, 5))],
    [sg.Button('回答', key='-Btn-')]
]

window = sg.Window('Combo', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == '-Btn-':
        destination = values['-Destination-']
        sg.popup('旅先は、', destination, 'が選択されました')

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
