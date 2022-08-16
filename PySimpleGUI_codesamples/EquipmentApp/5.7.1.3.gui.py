import PySimpleGUI as sg
import font


sg.theme('Reddit')
app_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAu9JREFUeNq8Vk1oE1EQniS7zTah2bhiC6lWMYkIVRFpUigqChUUerD2kJvH4kUEqVcrKgrSi9d6KFI89BwRbxosguZQMa1IwJ82h5JQ0iTtbn422fXNshtY3Sxt3deBJe9tQuabb7753nPdvxV/EOPL0zG+BJ3C0z8M3vF5cCjeBwL8ZWPDwD5H4dv3s0+On3wXBDduX5oAdA2MQNfRkfa+VcpBNbPgKABZkoLk45K+TbmtfsSdToD//BQwfaeoM2JioFXOAUtY8PBHQEq/cLx6DNbnQ7F90be//2kBRmPtI6l+ELohAVv5ZUcB8If9pYt3mVSoV4Urt/PzJgByYQU4fV37uuA4A0qrBVsbq8fIclp/9dSkAe7EVVBrFZAJA9yZhOPJJXEbVFXtrIFa9i0IQ5PgJUAqr+9QSe5iuDJ5tWR8ZQLg9gZIG5bJJw89o4+0d//bhr8rL6iHyjfXrqc8RX71R/6ebAKA6tdaQKYBgaAYnaZ9Q6oO6BpYJM+cSQNKvaLRz0WvaUBwLJ3uua0PsGT0mvkVcHEBbQxpJO9mGUMDGUsRov2yxI7RiGhUHj0oZH4+e2x9GOEYogVrSIkdowY2X91wnPaOLcAQF2fASzQgpWfbXpBd34ZfyaTtH2HSRq0G8dgQCIKwNwAy6X9wYk4TX2DsebsN2XUR3iwl7bKDorS0ZSQc3juAJvH9OtEBihCNyBjDsXN9MDE+6xjtJu8xKZRQrtTLGgj/hSkqPbcFgC1AD+gZfaidB7STW94H0AGN25BV5HI5EEURqpKk9X6nIQgHLLXBWJ2GTQICJ8DqHOgPhRyp3LIFaETogD5yIuJ9gBbtHQGwvYPtNiADxolIK7mlBvBExAfpN1rQUhSQ9eSfPqehuFncdaJoOAKRSNgeAF7JcfaRfl9sUvMFhRTcqKvA6pUPx2P0GNj+MNNeIxBMXmu4wUXxWu7uOOd6chXoBrPb5FQ10B5Hm8qd1oBlC2jTviMN7Ff8EWAAxLu0pwhMdo8AAAAASUVORK5CYII='


def main_window():
    menu_def = [['メニュー', ['初期設定', '終了']], ]

    main_layout = [
        [sg.Menu(menu_def)],
        [sg.Text('備品管理アプリ',justification='c',font=font.hgmaru_l_b)],
        [sg.Button('新規登録', key='-Move_registration_window-', disabled=True, tooltip='備品の新規登録',font=font.udp_m_i),
        sg.Button('備品管理', key='-Move_change_window-', disabled=True, tooltip='備品の変更/削除',font=font.udp_s)],
    ]

    return sg.Window('メイン画面', main_layout, icon=app_icon, finalize=True)


def initialize_window():
    initialize_layout = [
        [sg.FolderBrowse('保存先'), sg.Input(key='-Folder_path-', enable_events=True)],
        [sg.Button('初期設定', key='-Initialize-', disabled=True, pad=(170, 0))]]

    return sg.Window('初期設定', initialize_layout, icon=app_icon, finalize=True)


def registration_window():
    registration_layout = [
        [sg.Text('管理番号', size=(8, 1)), sg.Input(key='-Item_id-', enable_events=True)],
        [sg.Text('品名', size=(8, 1)), sg.Input(key='-Item_name-')],
        [sg.Text('棚番号', size=(8, 1)), sg.Input(key='-Shelf_number-')],
        [sg.Text('管理者', size=(8, 1)), sg.Input(key='-Owner-')],
        [sg.Button('登録', key='-Register-')], ]
    return sg.Window('新規登録画面', registration_layout, icon=app_icon, finalize=True)


def change_window():
    changing_layout = [
        [sg.Text('管理番号', size=(8, 1)),
        sg.Listbox(values=[], key='-Item_id_list-', select_mode='LISTBOX_SELECT_MODE_SINGLE',
                    size=(45, 3),enable_events=True)],
        [sg.Text('品名', size=(8, 1)), sg.Input(key='-Item_name-')],
        [sg.Text('棚番号', size=(8, 1)), sg.Input(key='-Shelf_number-')],
        [sg.Text('管理者', size=(8, 1)), sg.Input(key='-Owner-')],
        [sg.Button('更新', key='-Update-'), sg.Button('削除', key='-Delete-')], ]
    return sg.Window('備品管理画面', changing_layout, icon=app_icon, finalize=True)