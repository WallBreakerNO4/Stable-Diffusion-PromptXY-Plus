from collections import OrderedDict
import csv
import logging

def remove_duplicates(input_file, output_file):
    unique_lines = OrderedDict()

    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            unique_lines[tuple(row)] = None

    logging.info(f'从文件 {input_file} 中读取了 {len(unique_lines)} 行唯一数据')

    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for line in unique_lines.keys():
            writer.writerow(line)

    logging.info(f'去重后的数据已写入文件 {output_file}')

# 指定输入和输出文件名
input_file = 'prompts/artist_strings.csv'
output_file = 'prompts/artist_strings_unique.csv'

# 调用函数去重
remove_duplicates(input_file, output_file)