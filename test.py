from fetch_and_return_images import fetch_and_return_images

if (__name__ == "__main__"):
    # 示例API调用地址和JSON内容，你需要根据实际情况进行调整
    api_url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    json_payload = {
        "prompt": r"high definition,amazing quality,masterpiece,best quality,very aesthetic,highres,absurdres,sensitive,{artist:kousaki ruri},[artist:wlop],artist:ciloranko,year 2023,1girl,texas \(arknights\),arknights,solider,tactic helmet,(military uniform,armored,ballistic,jacket,latex bodysuit underwear,skirt,black gloves),knee pads,elbow pads,boots,realistic pantyhose,",
        "negative_prompt": r"text,watermark,bad anatomy,bad proportions,extra limbs,extra digit,extra legs,extra legs and arms,disfigured,missing arms,too many fingers,fused fingers,missing fingers,unclear eyes,watermark,username,eyeshadow,",
        "seed": -1,
        "sampler_name": "Euler a",
        "scheduler": "Automatic",
        "batch_size": 2,
        "steps": 30,
        "cfg_scale": 4.5,
        "width": 1024,
        "height": 1536
    }

    # 调用函数
    images = fetch_and_return_images(api_url, json_payload)
    for idx, image in enumerate(images):
        image.show()
        print(f"Displaying image {idx + 1}")
