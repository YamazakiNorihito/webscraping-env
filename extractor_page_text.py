from scraping_functions import scrape_page
import csv
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

url_stack = []
with open('visited_urls.txt', 'r') as file:
    url_stack = file.read().splitlines()

css_selector = 'table[border="0"][cellspacing="1"][cellpadding="5"][width="100%"]'
result_list = []  # List to store the data rows

dry_run = False  # Set this to False to perform full processing and CSV output

with ThreadPoolExecutor() as executor:
    futures = []
    while url_stack:
        url = url_stack.pop()
        if '?mode=view&no=' in url:
            future = executor.submit(scrape_page, url, css_selector)
            futures.append((url, future))
            if dry_run and len(futures) >= 5:
                break

    for url, future in futures:
        result = future.result()
        result_list.append({'URL': url, 'Text': result})

if dry_run:
    for i, result in enumerate(result_list):
        print(f"Result {i+1}:\n{result}")
else:
    # Generate a unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_filename = f"output_{timestamp}.csv"
    fieldnames = ['URL', 'Text']

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result_list)

    print(f"Results saved to '{csv_filename}'")
