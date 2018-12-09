import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
credentials = service_account.Credentials. from_service_account_file('key.json')
client = vision.ImageAnnotatorClient(credentials=credentials)    # [END vision_python_migration_client]


# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
file_name = os.path.join(
    os.path.dirname(__file__),
    '3.jpg') # Your image path from current directory


with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
#print('Texts:')

for text in texts:
#     print('\n"{}"'.format(text.description))
     with open('file.txt', 'a') as f:
         print('\n"{}"'.format(text.description), file=f)

lines = [] #Declare an empty list named "lines"
"""
with open ('file.txt', 'rt') as in_file:  # Open file file.txt for reading of text data.
    for line in in_file: # Store each line in a string variable "line"
        lines.append(line)
    #print(lines[4]) # prints that line
    for element in lines:  # For each element in our list,
        print(element)  # print it.
"""

import re
pattern_occur = []                         # The list where we will store results.
pattern = re.compile(r"(\+\d{3})?[\s.-]?\d{3}[\s.-]?\d{4}[\s.-]?\d{4}")  # Compile a case-insensitive regex pattern.
try:                              # Try to:
    with open ('file.txt', 'rt') as in_file:        # open file for reading text.

        for linenum, line in enumerate(in_file):        # Keep track of line numbers.
          if pattern.search(line) != None:          # If substring search finds a match,
                pattern_occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
        for linenum, line in pattern_occur:              # Iterate over the list of tuples, and
            a=line
        print(a)

except FileNotFoundError:                   # If log file not found.

    print("file not found.")                # print an error message.
