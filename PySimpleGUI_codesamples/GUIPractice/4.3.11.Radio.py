import PySimpleGUI as sg

layout = [
    [sg.Text('次の連休は、どこへ一番行きたいですか？')],
    [sg.Radio('ディズニーランド', group_id='destination', key='-Disney-')],
    [sg.Radio('レゴランド', group_id='destination', key='-Lego-')],
    [sg.Radio('ＵＳＪ', group_id='destination', default=True, key='-USJ-')],
    [sg.Button('回答', key='-Btn-')]
]

window = sg.Window('旅の目的地を選択', layout, finalize=True)

while True:
    event, value = window.read()  # イベントの入力を待つ

    if event == '-Btn-':
        if value['-Disney-'] == True:
            output = 'ディズニーランド'
        elif value['-Lego-'] == True:
            output = 'レゴランド'
        else:
            output = 'ＵＳＪ'
        sg.popup(output + 'として回答を受け付けました。')
        break

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
