
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
#               Match Port of Destination
# *****************************************************

    
    with open('file_new'+str(i)+'.txt', 'rt') as file_iterator:
        for line in file_iterator:
            if "Consignee" in line:
                
               next(file_iterator)
               print (next(file_iterator))



     

            