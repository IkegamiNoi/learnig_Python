import PySimpleGUI as sg

layout = [
    [sg.Image(source='goal.png', key='-Canvas-')],
    [sg.FileBrowse('新しい画像を選択', key='-File_path-',
                   file_types=(('pngファイル', '*.png'),), enable_events=True)],
    [sg.Button('選択した画像を表示', key='-Btn-', disabled=True)],
]

window = sg.Window('Image', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == '-File_path-':
        window['-Btn-'].Update(disabled=False)

    if event == '-Btn-':
        window['-Canvas-'].Update(source=values['-File_path-'])

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
