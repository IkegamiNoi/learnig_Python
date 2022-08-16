import PySimpleGUI as sg

BAR_MAX = 100

layout = [[sg.Text('プログレスバー進捗')],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20, 20), key='-Progress-')],
          [sg.Button('実行', key='-Run-')]]

window = sg.Window('プログレスバー', layout, finalize=True)

while True:  # Event Loop
    event, values = window.read()
    if event == '-Run-':
        for i in range(100):
            event, values = window.read(timeout=10)
            window['-Progress-'].update(i + 1)
        break

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
