import csv
from concurrent.futures import ThreadPoolExecutor
from typing import Sequence, Optional
import re
import os

def getFileName(file_path):
    file_name = os.path.basename(file_path)
    file_name_without_ext, ext = os.path.splitext(file_name)
    return file_name_without_ext + ext

# テキストの整形と改行処理を行う関数
def format_text(text):
    # Network Domainを削除
    start_index = text.index('\n')
    end_index = text.index('\n', start_index + 1)
    text = text[:start_index + 1] + text[end_index + 1:]

    text = re.sub(r'担当：\s*.*\n', '', text)
    text = re.sub(r'日時：\s*\d{4}/\d{2}/\d{2} \d{1,2}:\d{1,2}:\d{1,2}\n', '', text)
    text = re.sub(r'ＨＰアドレス：\s*http(s)?://.+\n', '', text)
    text = re.sub(r'\s', '', text)
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
                    if 'aqga' not in row['URL']:
                        continue
                    future = executor.submit(process_row, row)
                    futures.append(future)

                for future in futures:
                    row = future.result()
                    if 'aqga' not in row['URL']:
                        continue
                    writer.writerow(row)

    print(f"Formatted output saved to '{output_file}'")



input_file = 'data/output_20230514_080351.csv'  # 入力ファイル名
output_file = f'data/transformed_{getFileName(input_file)}'  # 出力ファイル名
# ファイルの並列処理を実行
process_file(input_file, output_file)
