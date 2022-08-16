import PySimpleGUI as sg

layout = [
    [sg.Input(), sg.CalendarButton('Date')],
    [sg.Input(key='-Output-')],
    [sg.CalendarButton('日付', target='-Output-', format="%Y年%m月%d日")]
]

window = sg.Window('カレンダーからの入力', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
