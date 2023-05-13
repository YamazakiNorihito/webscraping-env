
from scraping_functions import visit_pages_in_parallel

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
