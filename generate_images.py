import csv
import os
import pandas as pd
from tqdm import tqdm
from lib.convert_braces import convert_braces
from lib.construct_json_payload import construct_json_payload_with_artist
from lib.fetch_and_return_images import fetch_and_return_images
import hashlib
from config import STABLE_DIFFUSION_URL, ARTIST_CSV_FILE, PROMPT_CSV_FILE


# Function to generate a short hash for a given string
def generate_short_hash(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()[:10]


# Ensure the images directory exists
os.makedirs("images", exist_ok=True)

artist_csv_file = ARTIST_CSV_FILE
prompt_csv_file = PROMPT_CSV_FILE


# Read CSV files
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

    # Create a DataFrame to store the results
    df = pd.DataFrame(index=prompt_strings, columns=artist_strings)
    
    total_images = len(artist_strings) * len(prompt_strings)
    generated_images = 0

    # 创建总进度条
    progress_bar = tqdm(total=total_images, desc="生成图片进度")

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
                image_path = f"images/{artist_hash}_{prompt_hash}_{idx}.png"
                image.save(image_path)
                image_paths.append(image_path)
                print(
                    f'Saved image {idx + 1} for artist:"{artist_string}" and prompt:"{prompt_string}"'
                )
                # 更新进度条
                generated_images += 1
                progress_bar.update(1)
            # Store the image paths in the DataFrame
            df.at[prompt_string, artist_string] = str(
                image_paths
            )  # Convert list to string

    # 关闭进度条
    progress_bar.close()

# Transpose the DataFrame and save it to a CSV file
df.T.to_csv("image_paths.csv")
