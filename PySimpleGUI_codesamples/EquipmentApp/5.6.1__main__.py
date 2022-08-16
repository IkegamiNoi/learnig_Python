import PySimpleGUI as sg
import configparser
from pathlib import Path
import openpyxl
import pyqrcode
import gui


def main():    
    # 最初に表示するウィンドウを指定する。
    window = gui.main_window()
    
    
    # 設定ファイルを読み込む
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # 各種イベント処理
    while True:       
        window2 = gui.initialize_window() 
        window3 = gui.registration_window() 
        window4 = gui.change_window()
        window, event, values = sg.read_all_windows()   
       

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
        # アプリの初期設定

        # データ保存先が選択された場合、初期設定ボタンを有効化
        
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


if __name__ == '__main__':
    main()