'''
CREATE TABLEのサンプル
'''
import sqlite3

"""DB connect"""
#カレントディレクトリからのdbファイル名までのpath。
#dbファイルはなければ生成される。フォルダまでは生成されない。
#相対Pathの場合実行フォルダからの相対Pathである必要がある。
#VSCodeで実行しようとしてpythonファイルからの相対Pathにしていると実行場所がちがうのでダメだった。
db_path = "sql/sqlite/db/db.sqlite3" 
#with文でのdb接続。with文の終わりでcommitとcloseが走る。
with sqlite3.connect(db_path) as conn:
    #カーソルの準備
    cur = conn.cursor()
    #テーブルがあれば削除し、なければなにもしない。drop対象のテーブルはこのコード内にある必要あり？
    sql = "DROP TABLE IF EXISTS stock_volume_rankings_jp_tb"
    cur.execute(sql)

    #createテーブルの準備
    sql = """
        CREATE TABLE stock_volume_rankings_jp_tb (
            rankings integer,
            stock_name text,
            stock_code integer,
            date text,
            primary key (rankings, date)
        )
        """
    #SQLの実行
    cur.execute(sql)
    #カーソルのクローズ
    cur.close()