import json
import requests
from PIL import Image
from io import BytesIO
import base64


def fetch_and_return_images(api_url, json_payload):
    # 发送POST请求到API
    response = requests.post(api_url, json=json_payload)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析返回的JSON数据
        response_data = response.json()

        # 提取和解码图像数据
        images_base64 = response_data.get('images', [])
        images = []
        if images_base64:
            for idx, image_data_base64 in enumerate(images_base64):
                # 解码每一张图片
                image_data = base64.b64decode(image_data_base64)
                image = Image.open(BytesIO(image_data))

                # 显示图像
                print(f"Displaying image {idx + 1}")
                images.append(image)
        else:
            raise Exception("No images returned from API")
        return images
    else:
        raise Exception(f"Failed to fetch images from API. Status code: {response.status_code}")
