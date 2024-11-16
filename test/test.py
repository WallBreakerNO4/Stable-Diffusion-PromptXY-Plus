import pandas as pd
import ast

df = pd.read_csv('image_paths.csv', index_col=0)
for prompt_string in df.index:
    for artist_string in df.columns:
        image_path = df.at[prompt_string, artist_string]
        print("-----------------------")
        print(f'Prompt: {prompt_string};\nArtist: {artist_string};\nImage Path: {image_path}')
        print(type(image_path))