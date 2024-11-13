def convert_braces(input_string):
    # 将 { 替换为 (，并将 } 替换为 )
    output_string = input_string.replace('{', '(').replace('}', ')')
    return output_string
