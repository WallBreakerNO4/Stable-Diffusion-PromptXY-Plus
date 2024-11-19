from lib.convert_braces import convert_braces
from config import *


def construct_json_payload_with_artist(artist_string, prompt_string):
    payload = {
        "prompt": IMAGE_QUALITY_PROMPT + convert_braces(artist_string) + prompt_string,
        "negative_prompt": IMAGE_NEGATIVE_PROMPT,
        "seed": IMAGE_SEED,
        "sampler_name": IMAGE_SAMPLER_NAME,
        "scheduler": IMAGE_SCHEDULER,
        "batch_size": IMAGE_BATCH_SIZE,
        "steps": IMAGE_STEPS,
        "cfg_scale": IMAGE_CFG_SCALE,
        "width": IMAGE_WIDTH,
        "height": IMAGE_HEIGHT,
    }
    return payload
