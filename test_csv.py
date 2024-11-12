import csv
from convert_braces import convert_braces

with open('prompts/artist_strings.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    artist_strings = []
    for row in reader:
        artist_strings.append(convert_braces(row[0]))
    print(artist_strings)
