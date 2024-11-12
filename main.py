import csv
from convert_braces import convert_braces
from construct_json_payload import construct_json_payload_with_artist

with (open('prompts/artist_strings.csv', 'r', encoding='utf-8-sig') as artist_strings_csv,
      open('prompts/prompt_string.csv', 'r', encoding='utf-8-sig') as prompt_string_csv):
    artist_string_reader = csv.reader(artist_strings_csv)
    prompt_string_reader = csv.reader(prompt_string_csv)
    artist_strings = []
    prompt_strings = []
    for row in artist_string_reader:
        artist_strings.append(convert_braces(row[0]))
    for row in prompt_string_reader:
        prompt_strings.append(row[0])
    for artist_string in artist_strings:
        for prompt_string in prompt_strings:
            json_payload = construct_json_payload_with_artist(artist_string, prompt_string)
            print(json_payload)
            # print(construct_json_payload_with_artist(artist_string, "||||just a test||||"))
