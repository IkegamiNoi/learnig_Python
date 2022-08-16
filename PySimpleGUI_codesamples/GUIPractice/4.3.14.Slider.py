import PySimpleGUI as sg

layout = [
    [sg.Slider(range=(0, 100), key='-Slider1-')],
    [sg.Slider(range=(0, 100), key='-Slider2-', orientation='h',
               enable_events=True, disable_number_display=True),
     sg.Text(size=(3, 1), key='-Output-')]
]

window = sg.Window('Slider', layout, finalize=True)

while True:  # イベントの入力を待つ

    event, values = window.read()

    window['-Output-'].update(int(values['-Slider2-']))

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
