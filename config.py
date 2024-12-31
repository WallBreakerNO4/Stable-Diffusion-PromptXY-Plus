# API URL
# STABLE_DIFFUSION_URL = "https://u518045-a316-f1fcb2d2.westc.gpuhub.com:8443"
# STABLE_DIFFUSION_URL = "http://192.168.20.100:7860"
STABLE_DIFFUSION_URL = "http://127.0.0.1:6006"
# STABLE_DIFFUSION_URL = "http://100.71.15.9:7860"

# CSV 文件路径
ARTIST_CSV_FILE = "prompts/artist_strings_unique.csv"
# ARTIST_CSV_FILE = "prompts/artist_test.csv"
PROMPT_CSV_FILE = "prompts/prompt_string.csv"

# 生成图片所用参数
IMAGE_QUALITY_PROMPT = (
    r"very awa,masterpiece,best quality,year 2024,newest,highres,absurdres,"
)
IMAGE_NEGATIVE_PROMPT = r"text,watermark,bad anatomy,bad proportions,extra limbs,extra digit,extra legs,extra legs and arms,disfigured,missing arms,too many fingers,fused fingers,missing fingers,unclear eyes,watermark,username,"
IMAGE_SEED = -1
IMAGE_SAMPLER_NAME = "Euler"
IMAGE_SCHEDULER = "Automatic"
IMAGE_BATCH_SIZE = 1
IMAGE_STEPS = 28
IMAGE_CFG_SCALE = 4.5
IMAGE_WIDTH = 832
IMAGE_HEIGHT = 1216
