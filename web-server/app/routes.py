from flask import Blueprint, render_template
import pandas as pd
import os
import ast

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # 读取CSV文件
    csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'compressed_image_paths.csv')
    df = pd.read_csv(csv_path, header=None)
    
    # 准备图片数据矩阵
    image_matrix = []
    
    # 获取第一行的prompts作为列标题
    first_row = df.iloc[0]
    first_cell = str(first_row[0]) if pd.notna(first_row[0]) else ""
    prompts = [p.strip() for p in first_cell.split(',') if p.strip()]
    prompt_list = prompts[:5] if prompts else ["风格1", "风格2", "风格3", "风格4", "风格5"]
    
    # 处理每一行
    for _, row in df.iterrows():
        # 获取完整的画师风格信息
        artist_cell = str(row[0]) if pd.notna(row[0]) else ""
        artist_styles = [style.strip() for style in artist_cell.split(',') if style.strip()]
        artist_info = {
            'name': artist_styles[0] if artist_styles else '未知画师',
            'full_style': artist_cell
        }
        
        # 获取这一行的所有图片
        image_row = []
        for i, path in enumerate(row[1:6]):  # 取前5列图片
            if pd.notna(path) and isinstance(path, str) and path.startswith('['):
                try:
                    img_path = ast.literal_eval(path)[0]
                    image_row.append({
                        'path': img_path.replace('compressed_images/', 'static/images/compressed_images/'),
                        'artist': artist_info['name'],
                        'artist_full_style': artist_info['full_style'],
                        'prompt': prompts[i] if i < len(prompts) else f"风格{i+1}"
                    })
                except (ValueError, SyntaxError, IndexError):
                    image_row.append(None)
            else:
                image_row.append(None)
        
        if any(image_row):  # 只添加至少有一张图片的行
            image_matrix.append({
                'artist': artist_info['name'],
                'artist_full_style': artist_info['full_style'],
                'images': image_row
            })
    
    return render_template('index.html', image_matrix=image_matrix, prompts=prompt_list) 