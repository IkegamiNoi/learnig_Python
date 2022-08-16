import PySimpleGUI as sg

left_col = [
    [sg.Text('左側のコンテナ')],
    [sg.Multiline('', key='-l_container-', size=(35, 10))],
]

center_col = [
    [sg.Text('中央のコンテナ')],
    [sg.Multiline('', key='-c_container-', size=(25, 5))],
]

right_col = [
    [sg.Text('右側のコンテナ')],
    [sg.Multiline('', key='-r_container-', size=(35, 10))],
]

layout = [[sg.Column(left_col, element_justification='c'),
           sg.VSeperator(color='#eeeeee'),
           sg.Column(center_col, element_justification='c'),
           sg.Column(right_col, element_justification='c')]]

window = sg.Window('レイアウトの分割', layout,finalize=True)

while True:
    event, value = window.read()  # イベント入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()