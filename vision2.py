import io
import os
import re

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
credentials = service_account.Credentials. from_service_account_file('key.json')
client = vision.ImageAnnotatorClient(credentials=credentials)    # [END vision_python_migration_client]

for i in range(1, 11):
# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
    file_name = os.path.join(
        os.path.dirname(__file__),
        str(i)+'.jpg') # Your image path from current directory


    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    for text in texts:
#         print('\n"{}"'.format(text.description))
        with open('file'+str(i)+'.txt', 'a') as f:
             print('\n"{}"'.format(text.description), file=f)

    lines = [] #Declare an empty list named "lines"


for i in range(1, 11):
    pattern_occur = []                         # The list where we will store results.
    pattern = re.compile(r"(\+\d{3})?[\s.-]?\d{3}[\s.-]?\d{4}[\s.-]?\d{4}")  # Compile a case-insensitive regex pattern.
    try:                              # Try to:
        with open ('file'+str(i)+'.txt', 'rt') as in_file:        # open file for reading text.

            for linenum, line in enumerate(in_file):        # Keep track of line numbers.
                if pattern.search(line) != None:          # If substring search finds a match,
                    pattern_occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
            for linenum, line in pattern_occur:              # Iterate over the list of tuples, and
                a=line
            print('MASTER-AIRWAYBILL NO of image '+ str(i)+ ' is \t'+a)   # prints MAWB number of every  file

    except FileNotFoundError:                   # If log file not found.

        print("Log file not found.")                # print an error message.
