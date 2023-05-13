import requests
from bs4 import BeautifulSoup

# スクレイピング対象のURL
url = 'https://example.com'

# URLからHTMLを取得
response = requests.get(url)
html = response.text

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html, 'html.parser')

# タイトルを取得して表示
title = soup.title.text
print('タイトル:', title)

# リンクを取得して表示
links = soup.find_all('a')
print('リンク:')
for link in links:
    print(link.get('href'))

# 特定の要素を取得して表示（例: <p>タグのテキスト）
paragraphs = soup.find_all('p')
print('本文:')
for p in paragraphs:
    print(p.text)
