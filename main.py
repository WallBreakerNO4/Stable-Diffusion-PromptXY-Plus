import csv
from convert_braces import convert_braces
from construct_json_payload import construct_json_payload_with_artist

with open('artist_strings.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    artist_strings = []
    for row in reader:
        artist_strings.append(convert_braces(row[0]))
    for artist_string in artist_strings:
        print(construct_json_payload_with_artist(artist_string, ""))
