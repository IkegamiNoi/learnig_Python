import PySimpleGUI as sg

activity_list = ['温泉', '登山', '遊園地']

layout = [
    [sg.Text('旅行に行きたい場所を１つ選択して下さい')],
    [sg.Listbox(('北海道', '東京', '大阪'), key='-Destination-', size=(10, 5))],
    [sg.Text('旅先でしたいアクティビティーを複数選択して下さい')],
    [sg.Listbox(values=activity_list, key='-Activity-',
                size=(10, 5), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)],
    [sg.Button('回答', key='-Btn-')]
]

window = sg.Window('ListBox', layout, finalize=True)

while True:
    event, values = window.read()  # イベントの入力を待つ

    if event == '-Btn-':
        destination = values['-Destination-']
        activity = values['-Activity-']
        sg.popup('旅先は、', destination, 'アクティビティーは、', activity, 'が選択されました')

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
