def clean_prompt(prompt):
    # 使用逗号分隔关键词
    keywords = prompt.split(',')
    # 去除空关键词并保持顺序
    seen = set()
    cleaned_keywords = []
    for keyword in keywords:
        if keyword and keyword not in seen:
            seen.add(keyword)
            cleaned_keywords.append(keyword)
    # 重新组合成字符串
    cleaned_prompt = ','.join(cleaned_keywords)
    return cleaned_prompt

# 示例使用
if __name__ == '__main__':
    prompt = "very awa,masterpiece,best quality,year 2024,newest,highres,absurdres,,very awa,,best quality"
    cleaned_prompt = clean_prompt(prompt)
    print(cleaned_prompt)