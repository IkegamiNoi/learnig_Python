import PySimpleGUI as sg

tab1_layout = [[sg.Text('タブ1のレイアウト')], [sg.Image(source='goal.png')]]

tab2_layout = [[sg.Text('タブ2のレイアウト')],
               [sg.Button('ボタン', key='-Btn-', pad=(50, 100))]]

layout = [
    [sg.TabGroup([[
        sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)
    ]])
    ],
]

window = sg.Window('Tab & Tab Group', layout, finalize=True)

while True:
    event, values = window.read()

    if event == '-Btn-':
        sg.popup('ボタンのイベント')

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
