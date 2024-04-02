# Requestsライブラリ

"""インポート"""
import requests

"""ウェブページの取得"""
# URLの指定
url = 'https://finance.yahoo.co.jp/stocks/ranking/volume?market=all&term=daily'
# ユーザーエージェントの指定 
# 以下のページへアクセスしてコピペで取得する。
#   https://testpage.jp/tool/ip_user_agent.php
user_agent = 'Mozilla/5.0'
# hedersを辞書で作成する
headers = {'User-agent': user_agent}
# requests.getにurlとheadersを渡して、ウェブページを取得する
response = requests.get(url, headers).text
