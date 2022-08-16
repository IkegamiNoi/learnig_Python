import PySimpleGUI as sg

destination = {
    '-Disney-': 'ディズニーランド',
    '-Lego-': 'レゴランド',
    '-USJ-': 'ＵＳＪ'
}

layout = [
    [sg.Text('お気に入りのテーマパークはどこですか（複数回答可）？')],
    [sg.Checkbox('ディズニーランド', default=True, key='-Disney-')],
    [sg.Checkbox('レゴランド', key='-Lego-')],
    [sg.Checkbox('ＵＳＪ', key='-USJ-')],
    [sg.Button('回答', key='-Btn-')]
]

window = sg.Window('お気に入りのテーマパーク調査', layout, finalize=True)

while True:

    event, values = window.read()  # イベントの入力を待つ

    if event == '-Btn-':
        firstloop = True
        message = '行きたい場所は、'
        for key in destination.keys():
            if values[key] == True:
                if firstloop:
                    message = message + destination[key]
                    firstloop = False
                else:
                    message = message + 'と' + destination[key]
        message = message + 'です'
        if firstloop:
            message = 'どこにも行きたくないようです'
        sg.popup(message)
        break

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
