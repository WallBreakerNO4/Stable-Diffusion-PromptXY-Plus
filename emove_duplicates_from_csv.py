import csv
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove_duplicates(input_file, output_file):
    # 使用集合来存储唯一的行
    unique_lines = set()

    # 读取输入文件并去重
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            # 将每一行转换为元组并添加到集合中
            unique_lines.add(tuple(row))

    logging.info(f'从文件 {input_file} 中读取了 {len(unique_lines)} 行唯一数据')

    # 将去重后的内容写入输出文件
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for line in unique_lines:
            writer.writerow(line)

    logging.info(f'去重后的数据已写入文件 {output_file}')

# 指定输入和输出文件名
input_file = 'prompts/artist_strings.csv'
output_file = 'prompts/artist_strings_unique.csv'

# 调用函数去重
remove_duplicates(input_file, output_file)