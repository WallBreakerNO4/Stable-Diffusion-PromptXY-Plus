import csv
import os
import pandas as pd
from tqdm import tqdm
from PIL import Image
from lib.convert_braces import convert_braces
from lib.construct_json_payload import construct_json_payload_with_artist
from lib.fetch_and_return_images import fetch_and_return_images
import hashlib
from config import STABLE_DIFFUSION_URL, ARTIST_CSV_FILE, PROMPT_CSV_FILE


def generate_short_hash(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()[:10]


# 确保压缩图片目录存在
os.makedirs("compressed_images", exist_ok=True)

artist_csv_file = ARTIST_CSV_FILE
prompt_csv_file = PROMPT_CSV_FILE


# 读取CSV文件
with (
    open(artist_csv_file, "r", encoding="utf-8-sig") as artist_strings_csv,
    open(prompt_csv_file, "r", encoding="utf-8-sig") as prompt_string_csv,
):
    artist_string_reader = csv.reader(artist_strings_csv)
    prompt_string_reader = csv.reader(prompt_string_csv)
    artist_strings = []
    prompt_strings = []
    api_url = STABLE_DIFFUSION_URL + "/sdapi/v1/txt2img"

    for row in artist_string_reader:
        artist_strings.append(convert_braces(row[0]))
    for row in prompt_string_reader:
        prompt_strings.append(row[0])

    # 创建DataFrame来存储结果
    df = pd.DataFrame(index=prompt_strings, columns=artist_strings)
    
    total_images = len(artist_strings) * len(prompt_strings)
    generated_images = 0

    # 创建总进度条
    progress_bar = tqdm(total=total_images, desc="生成压缩图片进度")

    for artist_string in artist_strings:
        for prompt_string in prompt_strings:
            json_payload = construct_json_payload_with_artist(
                artist_string, prompt_string
            )
            images = fetch_and_return_images(api_url, json_payload)
            image_paths = []
            for idx, image in enumerate(images):
                artist_hash = generate_short_hash(artist_string)
                prompt_hash = generate_short_hash(prompt_string)
                # 保存为webp格式
                image_path = f"compressed_images/{artist_hash}_{prompt_hash}_{idx}.webp"
                # 转换并保存为webp格式，quality=80提供良好的压缩率和质量平衡
                image.save(image_path, 'WEBP', quality=80, method=6)
                image_paths.append(image_path)
                print(
                    f'已保存压缩图片 {idx + 1}, 艺术家:"{artist_string}", 提示词:"{prompt_string}"'
                )
                # 更新进度条
                generated_images += 1
                progress_bar.update(1)
            # 将图片路径存储在DataFrame中
            df.at[prompt_string, artist_string] = str(image_paths)

    # 关闭进度条
    progress_bar.close()

# 转置DataFrame并保存为CSV文件
df.T.to_csv("compressed_image_paths.csv") 