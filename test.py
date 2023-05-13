from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlparse
from selenium.common.exceptions import StaleElementReferenceException

# Chromeドライバーのパスを指定してWebDriverを初期化
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome_webdriver = webdriver.Chrome('chromedriver', options=options)

def visit_page(urls, domain, url_condition):
    visited_urls = set()  # 訪れたURLを管理するためのセット
    stack = urls.copy()  # スタックを使用してURLを管理

    while stack:
        current_url = stack.pop()
        visited_urls.add(current_url)
        
        chrome_webdriver.get(current_url)
        time.sleep(1)  # ページが完全に読み込まれるまで待機

        # aタグの要素を取得
        a_tags = chrome_webdriver.find_elements(By.CSS_SELECTOR, 'a[href]')

        # ページ内のリンクをチェック
        for a in a_tags:
            href = a.get_attribute('href')
            if href:
                parsed_url = urlparse(href)
                current_domain = parsed_url.netloc
                if current_domain == domain and parsed_url.geturl() not in visited_urls and url_condition in parsed_url.geturl():
                    stack.append(parsed_url.geturl())

    return visited_urls

# トップページを開く
urls = ['http://bp3street.com/kbase/kbasbbs/bbs/1sk/i/kansai/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/1sk/i/kanto/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/1sk/k/kansai/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/1sk/k/kanto/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqga/kantou/01/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqga/kantou/02/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqga/kantou/03/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqga/kantou/04/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqga/kantou/05/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqga/kinki/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqga/oosaka/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqgn/kantou/01/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqgn/kantou/02/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqgn/kantou/03/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqgn/kantou/04/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqgn/kantou/05/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqgn/kinki/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/aqgn/oosaka/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/league/kansai/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/league/kanto/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mb/kansai/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mb/kantou/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mb/tokyo/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mnb2/kansai/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mnb2/kanto/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mnbk/kansai/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mnbk/kantou/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/mnbk/tokyo/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/ren/kansai/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/ren/kanto/patio.cgi','http://bp3street.com/kbase/kbasbbs/bbs/sub/shinpanirai/patio.cgi']
# 初回のページ訪問
visited_urls = visit_page(urls, 'bp3street.com', 'mode=view&no=')

# 訪れたページのURLを表示
# ファイルに保存
file_path_visited_urls = 'visited_urls.txt'
with open(file_path_visited_urls, 'w') as file:
    for url in visited_urls:
        file.write(url + '\n')

# ブラウザを終了する
chrome_webdriver.quit()
