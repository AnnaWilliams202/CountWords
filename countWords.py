import glob
import os

# '/Users/annawilliams/Desktop/processingTextFiles/processingTextFiles.py'

filepaths = sorted(glob.glob("/Users/annawilliams/Desktop/processingTextFiles/*.txt"))
counter = {}

for filepath in filepaths:
    with open(filepath, 'r') as f:
        content = f.read()
        words = content.split()
        for word in words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1

with open('countWords.txt', 'w') as f:
    for word, count in counter.items():
        f.write(word + "\t" + str(count) + "\n")
