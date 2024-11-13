from lib.convert_braces import convert_braces


def construct_json_payload_with_artist(artist_string, prompt_string):
    payload = {
        "prompt": r"high definition,amazing quality,masterpiece,best quality,very aesthetic,highres,absurdres,sensitive,"
                  + convert_braces(artist_string) + prompt_string,
        "negative_prompt": r"text,watermark,bad anatomy,bad proportions,extra limbs,extra digit,extra legs,extra legs "
                           r"and arms,disfigured,missing arms,too many fingers,fused fingers,missing fingers,"
                           r"unclear eyes,watermark,username,eyeshadow,",
        "seed": -1,
        "sampler_name": "Euler a",
        "scheduler": "Automatic",
        "batch_size": 1,
        "steps": 30,
        "cfg_scale": 4.5,
        "width": 1024,
        "height": 1536
    }
    return payload
