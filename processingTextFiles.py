import glob
import os

# '/Users/annawilliams/Desktop/processingTextFiles/processingTextFiles.py'

filepaths = sorted(glob.glob("/Users/annawilliams/Desktop/processingTextFiles/*.txt"))

text = []

for filepath in filepaths:
    with open(filepath, 'r') as f:
        content = f.read()
        # Add the content to the list
        text.append(content)

    # Open the new file in write mode
with open('merged_file.txt', 'w') as merged_file:
    # Write each file's content into the merged file
    for content in text:
        merged_file.write(content + "\n")  # Adding a newline for separation