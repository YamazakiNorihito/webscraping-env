from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlparse
import threading

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def visit_page(url, domain, url_condition):
    visited_urls = set()
    stack = [url]

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

def scrape_page(url, css_selector):
    chrome_webdriver = webdriver.Chrome('chromedriver', options=options)

    chrome_webdriver.get(url)
    time.sleep(1)
    target_element = chrome_webdriver.find_element(By.CSS_SELECTOR, css_selector)
    text = target_element.text

    chrome_webdriver.quit()

    return text
