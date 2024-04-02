# Requestsライブラリ

## インポート
``` python
import requests
```

## ウェブページの取得
### URLの指定
``` python
url = 'https://finance.yahoo.co.jp/stocks/ranking/volume?market=all&term=daily'
```
### ユーザーエージェントの指定 [こちらで確認する](https://testpage.jp/tool/ip_user_agent.php)
``` python
user_agent = 'Mozilla/5.0'
```
### hedersを辞書で作成する
``` python
headers = {'User-agent': user_agent}
```
### `requests.get`に`url`と`headers`を渡して、ウェブページを取得する
``` python
response = requests.get(url, headers).text
```
