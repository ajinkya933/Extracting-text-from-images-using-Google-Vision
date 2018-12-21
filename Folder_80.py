import io
import os
import re

#*****************************************************
#               Match MAWB
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
            print('\n\n')
            print('###########################################')
            print('MAWB : '+a+'\n')   # prints MAWB number of every  file

    except FileNotFoundError:                   # If log file not found.

        print("Log file not found.")                # print an error message.

# *****************************************************
#               Match Consignee
# *****************************************************

    linesCo = [] #Declare an empty list named "lines"
    with open ('file_new'+str(i)+'.txt', 'rt') as in_file:  #Open file fire4.txt for reading of text data.

        for line in in_file: #For each line of text store in a string variable named "line", and
            index = 0  # index represents where in the string we begin looking.

            linesCo.append(line.rstrip('\n'))  #add that line to our list of lines.
            #str = linesCo[0]
            substr = "Consigne"         # Substring to search for, in this case a single character
            substr2 = "CONSIGNE"

            #print(str)

        for linenum, line in enumerate(linesCo):  # For every line in lines, enumerated by linenum,
            index = 0
            index2 = 0  # Set the search index to the first character,
            str2 = linesCo[linenum]	    # and store the line in a string variable, str.
            #print(line)

            while index < len(str2):     # While search index is less than the length of the string:
                index = str2.find(substr, index) # If substring is located, set search index to that location.
                if index == -1:         # If nothing is found,
                    #print('index = -1')
                    break               # break out of the while loop. Otherwise

                print(str2) # Print the linenum and index of the located substr.
                li = linesCo[linenum:linenum + 5]

                index += len(substr)    # Before repeating search, increment index by length of substr." " "
                a=li
                print(a)

            while index2 < len(str2):     # While search index is less than the length of the string:
                index2 = str2.find(substr2, index2)# If substring is located, set search index to that location.
                if index2 == -1:         # If nothing is found,
                    #print('index = -1')
                    break               # break out of the while loop. Otherwise

                print(str2) # Print the linenum and index of the located substr.
                li2 = linesCo[linenum:linenum + 5]

                index2 += len(substr2)    # Before repeating search, increment index by length of substr." " "
                b=li2
                print(b)


# *****************************************************
#               Match Port of Destination
# *****************************************************

        with open('file_new'+str(i)+'.txt', 'rt') as in_file:  # Open file fire4.txt for reading of text data.
            searchstrings = ('DEL', 'MAA', 'BLR', 'BOM', 'HYD', 'CCU')
            for line in in_file:
                if any(word in line for word in searchstrings):
                    #print(line)
                    c = line


        print(' \n Port of Destination '+ c )

        
# *****************************************************
#               Match Weight
# *****************************************************
    
    def get_weight(fp):
        next(line for line in fp if 'KILO' in line or 'KG' in line)
        for line in fp:
            try:
                return float(line)
            except ValueError:
                continue
        #raise ValueError("No numeric line after 'KILO'")


    with open ('file_new'+str(i)+'.txt', 'rt') as fd:            
        print('Weight : ',get_weight(fd))
            
            
            