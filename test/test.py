from lib.fetch_and_return_images import fetch_and_return_images
from lib.construct_json_payload import *

if __name__ == "__main__":
    # 示例API调用地址和JSON内容，你需要根据实际情况进行调整
    api_url = "http://192.168.20.100:7860/sdapi/v1/txt2img"
    json_payload = construct_json_payload_with_artist(
        r"{artist:kousaki ruri},[artist:wlop],artist:ciloranko,year 2023,",
        r"1girl,texas \(arknights\),arknights,solider,tactic helmet,(military uniform,armored,ballistic,jacket,"
        r"latex bodysuit underwear,skirt,black gloves),knee pads,elbow pads,boots,realistic pantyhose,")
    print(json_payload)
    # 调用函数
    images = fetch_and_return_images(api_url, json_payload)
    for idx, image in enumerate(images):
        image.show()
        print(f"Displaying image {idx + 1}")
