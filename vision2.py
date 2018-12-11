import io
import os
import re

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
credentials = service_account.Credentials. from_service_account_file('key.json')
client = vision.ImageAnnotatorClient(credentials=credentials)    # [END vision_python_migration_client]

for i in range(1,10):
# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
    file_name = os.path.join(
        os.path.dirname(__file__),
        str(i)+'.jpg') # Your image path from current directory

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:

        with open('file'+str(i)+'.txt', 'a') as f:
                print('\n"{}"'.format(text.description), file=f)



for j in range(1,10):
    with open('file'+str(j)+'.txt') as in_file:
        for linenum, line in enumerate(in_file):
            if not re.search(r'".*"', line):
                #in_file.write(line)
                print(line)
                with open('file_new'+str(j)+'.txt', "a") as f1:
                    f1.writelines(line)




#*****************************************************
#               Regex
#*****************************************************

for i in range(1, 10):
    pattern_occur = []                         # The list where we will store results.
    pattern = re.compile(r"(\+\d{3})?[\s.-]?\d{3}[\s.-]?\d{4}[\s.-]?\d{4}")  # Compile a case-insensitive regex pattern.
    try:                              # Try to:
        with open ('file_new'+str(i)+'.txt', 'rt') as in_file:        # open file for reading text.

            for linenum, line in enumerate(in_file):        # Keep track of line numbers.
                if pattern.search(line) != None:          # If substring search finds a match,
                    pattern_occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
            for linenum, line in pattern_occur:              # Iterate over the list of tuples, and
                a=line
            print(a)   # prints MAWB number of every  file

    except FileNotFoundError:                   # If log file not found.

        print("Log file not found.")                # print an error message.





    linesCo = [] #Declare an empty list named "lines"
    with open ('file_new'+str(i)+'.txt', 'rt') as in_file:  #Open file fire4.txt for reading of text data.

        for line in in_file: #For each line of text store in a string variable named "line", and
            index = 0  # index represents where in the string we begin looking.

            linesCo.append(line.rstrip('\n'))  #add that line to our list of lines.
            str1 = linesCo[0]
            substr = "CONSIGNE"         # Substring to search for, in this case a single character
            #print(str)

        for linenum, line in enumerate(linesCo):  # For every line in lines, enumerated by linenum,
            index = 0                   # Set the search index to the first character,
            str1 = linesCo[linenum]	    # and store the line in a string variable, str.
            #print(line)

            while index < len(str1):     # While search index is less than the length of the string:
                index = str1.find(substr, index)# If substring is located, set search index to that location.

                if index == -1:         # If nothing is found,
                    break               # break out of the while loop. Otherwise

                print("Line: ", linenum, str1) # Print the linenum and index of the located substr.
                li = linesCo[linenum:linenum + 5]

                index += len(substr)    # Before repeating search, increment index by length of substr." " "
                a=li
                print(a)
