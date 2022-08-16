import PySimpleGUI as sg
import configparser
from pathlib import Path
import openpyxl
import pyqrcode
import gui


def main():    
    # 最初に表示するウィンドウを指定する。
    window = gui.main_window()    
    
    try:
        # 設定ファイルを読み込む
        config = configparser.ConfigParser()
        config.read('config.ini', 'utf-8')
        # 初期設定が完了しているか確認
        qrfolder_path = config['setting']['qrfolder_path']
        itemlist_path = config['setting']['itemlist_path']
        # 新規登録と備品管理ボタンを有効化
        window['-Move_change_window-'].update(disabled=False)
        window['-Move_registration_window-'].update(disabled=False)
    except Exception as e:
        sg.popup('初期設定を行ってください。', e)
        
    
    # 各種イベント処理
    while True:       
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit' or event == '終了':
            break        
            
        # ---------------------------------------
        # メイン画面のイベント　
        # ---------------------------------------        
        # 初期設定画面へ移動
        if event == '初期設定':
            window.close()
            window = gui.initialize_window()        

        # 新規登録画面に移動
        if event == '-Move_registration_window-':
            window.close()
            window = gui.registration_window()
                
        # 備品管理画面へ移動        
        if event == '-Move_change_window-':
            window.close()
            window = gui.change_window()
            # 備品一覧.xlsxから値を読み込み管理番号リストボックスに反映
                #pass        
        # ---------------------------------------
        # 初期設定画面のイベント
        # ---------------------------------------        
        # データ保存先が選択された場合、初期設定ボタンを有効化
        if event == '-Folder_path-':
            window['-Initialize-'].update(disabled=False)

        # アプリの初期設定（必要なフォルダ、ファイル類の作成と設定ファイル更新）
        if event == '-Initialize-':
            # データの保存先を取得
            folder_path = values['-Folder_path-']
            # アプリの初期設定
            initialize_app(folder_path)
            # 初期設定画面をクローズし、メイン画面へ切り替え
            window.close()
            window = gui.main_window()

            # 初備品登録と備品管理ボタンを有効化
            window['-Move_change_window-'].update(disabled=False)
            window['-Move_registration_window-'].update(disabled=False)


        # ---------------------------------------
        # 新規登録画面のイベント
        # ---------------------------------------
        # 備品の新規登録
        
        # ---------------------------------------
        # 備品管理画面のイベント
        # ---------------------------------------
        
        # 備品情報の更新
        
        # 備品情報の削除
        

    window.close()

def initialize_app(path):
    # ディレクトリの作成
    folder_path = path
    # 備品フォルダの作成
    root_path = folder_path + '/備品管理'
    Path(root_path).mkdir()
    # QRコードフォルダの作成
    qrfolder_path = root_path + '/QRコード'
    Path(qrfolder_path).mkdir()
    # 備品一覧.xlsxを作成
    itemlist_path = root_path + '/備品一覧.xlsx'
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '備品シート'
    # 列幅の設定
    column_widths = {'A': 16, 'B': 16, 'C': 16, 'D': 16, 'E': 30}
    # 列の見出しの設定
    column_name = {
        'A': '管理番号', 'B': '品名', 'C': '棚番号', 'D': '管理者', 'E': 'QRコード'}
    for count, column_index in enumerate(column_widths):
        count += 1
        sheet.column_dimensions[column_index].width = column_widths[column_index]
        sheet.cell(1, count).value = column_name[column_index]
    wb.save(itemlist_path)
    # 設定ファイルconfig.iniを更新
    config = configparser.ConfigParser()
    config.read('config.ini', 'utf-8')
    # 設定ファイルにsettingセクションが無い場合のみセクション追加
    if config.has_section('setting') is not True:
        config.add_section('setting')
        config['setting']['root_path'] = root_path
        config['setting']['qrfolder_path'] = qrfolder_path
        config['setting']['itemlist_path'] = itemlist_path
    configpath = Path('config.ini')
    with configpath.open(mode='w', encoding='utf-8') as f:
        config.write(f)

    return sg.popup('初期設定が完了しました。')


if __name__ == '__main__':
    main()