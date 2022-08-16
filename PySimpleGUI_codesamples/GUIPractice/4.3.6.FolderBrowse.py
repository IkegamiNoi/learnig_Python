import PySimpleGUI as sg

layout = [
    [sg.Input(), sg.FolderBrowse('フォルダーを選択',key = '-Folder-')],
]

window = sg.Window('FolderBrowse', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
