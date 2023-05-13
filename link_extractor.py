from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlparse
from selenium.common.exceptions import StaleElementReferenceException
import threading

def visit_page(url, domain, url_condition):
    visited_urls = set()
    stack = [url]

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_webdriver = webdriver.Chrome('chromedriver', options=options)

    while stack:
        current_url = stack.pop()
        visited_urls.add(current_url)
        
        chrome_webdriver.get(current_url)
        time.sleep(1)

        a_tags = chrome_webdriver.find_elements(By.CSS_SELECTOR, 'a[href]')

        for a in a_tags:
            href = a.get_attribute('href')
            if href:
                parsed_url = urlparse(href)
                current_domain = parsed_url.netloc
                if current_domain == domain and parsed_url.geturl() not in visited_urls and url_condition in parsed_url.geturl():
                    stack.append(parsed_url.geturl())

    chrome_webdriver.quit()

    return visited_urls

def visit_pages_in_parallel(urls, domain, url_condition):
    visited_urls = set()
    lock = threading.Lock()

    def visit(url):
        nonlocal visited_urls
        result = visit_page(url, domain, url_condition)
        with lock:
            visited_urls.update(result)

    threads = []
    for url in urls:
        thread = threading.Thread(target=visit, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return visited_urls

# トップページを開く
urls = ['']
# ドメインとURLの条件を指定してページを並列に訪れる
visited_urls = visit_pages_in_parallel(urls, '', '')

# 訪れたページのURLを表示
# ファイルに保存
file_path_visited_urls = 'visited_urls.txt'
with open(file_path_visited_urls, 'w') as file:
    for url in visited_urls:
        file.write(url + '\n')
