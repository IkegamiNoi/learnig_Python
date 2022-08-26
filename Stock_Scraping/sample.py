import bs4
import traceback
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
 
# ドライバーのフルパス
#CHROMEDRIVER = "/Users/inouekei/Documents/GitHub/MyKabuDB/driver/chromedriver"
CHROMEDRIVER = "./driver/chromedriver"
# 改ページ（最大）
PAGE_MAX = 2
# 遷移間隔（秒）
INTERVAL_TIME = 1
 
# ドライバー準備
def get_driver():
    # ヘッドレスモードでブラウザを起動
    options = Options()
    options.add_argument('--headless')
 
    # ブラウザーを起動
    driver = webdriver.Chrome(CHROMEDRIVER, options=options)
 
    return driver
 
 
# 対象ページのソース取得
def get_source_from_page(driver, page):
    try:
        # ターゲット
        driver.get(page)
        driver.implicitly_wait(10)  # 見つからないときは、10秒まで待つ
        page_source = driver.page_source
 
        return page_source
 
    except Exception as e:
 
        print("Exception\n" + traceback.format_exc())
 
        return None
 
 
# ソースからスクレイピングする
def get_data_from_source(src):
    # スクレイピングする
    soup = bs4.BeautifulSoup(src, features='lxml')
    # print(soup)
    try:
        info = []
        table = soup.find("table", class_="yjS")
 
        if table:
            elems = table.find_all("tr")
            for elem in elems:
                td_tag = elem.find(class_="yjM")
 
                if td_tag:
                    a_tag = elem.find("a")
 
                    if a_tag:
                        href = a_tag.attrs['href']
                        match = re.findall("\/stocks\/detail\/\?code=(.*)$", href)
 
                        if len(match) > 0:
                            item_id = match[0]
                            info.append(item_id)
 
        return info
 
    except Exception as e:
 
        print("Exception\n" + traceback.format_exc())
 
        return None
 
 
# 次のページへ遷移
def next_btn_click(driver):
    try:
        # 次へボタン
        elem_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'listNext'))
        )
 
        # クリック処理
        actions = ActionChains(driver)
        actions.move_to_element(elem_btn)
        actions.click(elem_btn)
        actions.perform()
 
        # 間隔を設ける(秒単位）
        time.sleep(INTERVAL_TIME)
 
        return True
 
    except Exception as e:
 
        print("Exception\n" + traceback.format_exc())
 
        return False
 
 
if __name__ == "__main__":
    # 対象ページURL
    page = "https://stocks.finance.yahoo.co.jp/stocks/qi/"
 
    # ブラウザのdriver取得
    driver = get_driver()
 
    # ページのソース取得
    source = get_source_from_page(driver, page)
    result_flg = True
 
    # ページカウンター制御の初期化
    page_counter = 0
 
    while result_flg:
        page_counter = page_counter + 1
 
        # ソースからデータ抽出
        data = get_data_from_source(source)
 
        # データ保存
        print(data)
 
        # 改ページ処理を抜ける
        if page_counter == PAGE_MAX:
            break
 
        # 改ページ処理
        result_flg = next_btn_click(driver)
        source = driver.page_source
 
    # 閉じる
    driver.quit()