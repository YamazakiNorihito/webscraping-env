import csv
from concurrent.futures import ThreadPoolExecutor
from typing import Sequence, Optional

input_file = 'output_20230514_080351.csv'  # 入力ファイル名
output_file = f'transformed_{input_file}'  # 出力ファイル名

# テキストの整形と改行処理を行う関数
def format_text(text):
    text = text.strip()
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    return text

def process_row(row):
    formatted_text = format_text(row['Text'])
    row['Text'] = formatted_text
    return row

# Sequence[str] | Noneを文字列の配列に変換する関数
def convert_sequence_to_list(seq: Optional[Sequence[str]]) -> list[str]:
    if seq is None:
        return []  # Noneの場合は空のリストを返す
    return list(seq)

def process_file(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = convert_sequence_to_list(reader.fieldnames)

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            with ThreadPoolExecutor() as executor:
                futures = []
                for row in reader:
                    future = executor.submit(process_row, row)
                    futures.append(future)

                for future in futures:
                    row = future.result()
                    writer.writerow(row)

    print(f"Formatted output saved to '{output_file}'")

# ファイルの並列処理を実行
process_file(input_file, output_file)
