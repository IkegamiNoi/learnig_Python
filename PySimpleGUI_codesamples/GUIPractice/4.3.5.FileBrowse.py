import PySimpleGUI as sg

layout = [
    [sg.Input(), sg.FileBrowse('ファイルを１つ選択', file_types=(('CSVファイル', '*.csv'),), )],
    [sg.Input(key='-Output-')],
    [sg.FilesBrowse('ファイルを複数選択', target='-Output-')],
]

window = sg.Window('FileBrowse', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
