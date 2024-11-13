import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
import ast

# Load the DataFrame from the transposed CSV file
df = pd.read_csv('image_paths.csv', index_col=0)

# Create a new Excel workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Set the row height and column width to fit the images
row_height = (1536 // 1.3) + 10  # Increase the row height more significantly
col_width = (1024 // 7.5) + 10  # Column width remains the same

# Write the DataFrame to the Excel worksheet
for j, artist_string in enumerate(df.columns, start=2):
    ws.cell(row=1, column=j, value=artist_string)
    ws.column_dimensions[chr(64 + j)].width = col_width
for i, prompt_string in enumerate(df.index, start=2):
    ws.cell(row=i, column=1, value=prompt_string)
    ws.row_dimensions[i].height = row_height
    for j, artist_string in enumerate(df.columns, start=2):
        image_paths = df.at[prompt_string, artist_string]
        if pd.notna(image_paths):
            for image_path in ast.literal_eval(image_paths):  # Use ast.literal_eval to convert string back to list
                img = ExcelImage(image_path)
                img.anchor = ws.cell(row=i, column=j).coordinate
                ws.add_image(img)

# Save the workbook
wb.save('output_images.xlsx')
