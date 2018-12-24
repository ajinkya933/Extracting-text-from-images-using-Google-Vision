import io
import os
import re

# *****************************************************
#               Match MAWB
# *****************************************************


for i in range(1, 10):
    pattern_occur = []  # The list where we will store results.
    pattern = re.compile(r"(\+\d{3})?[\s.-]?\d{3}[\s.-]?\d{4}[\s.-]?\d{4}")  # Compile a case-insensitive regex pattern.
    try:  # Try to:
        with open('file_new' + str(i) + '.txt', 'rt') as in_file:  # open file for reading text.

            for linenum, line in enumerate(in_file):  # Keep track of line numbers.
                if pattern.search(line) != None:  # If substring search finds a match,
                    pattern_occur.append(
                        (linenum, line.rstrip('\n')))  # strip linebreaks, store line and line number in list as tuple.
            for linenum, line in pattern_occur:  # Iterate over the list of tuples, and
                a = line
            print('\n\n')
            print('###########################################')
            print('MAWB : ' + a)  # prints MAWB number of every  file

    except FileNotFoundError:  # If log file not found.

        print("Log file not found.")  # print an error message.

    # *****************************************************
    #               Match Port of Destination
    # *****************************************************

    with open('file_new' + str(i) + '.txt', 'rt') as in_file:  # Open file fire4.txt for reading of text data.
        searchstrings = ('BOM', 'BLR', 'HYD', 'CCU', 'MAA', 'DEL')
        for line in in_file:
            if any(word in line for word in searchstrings):
                # print(line)
                c = line

    print('Port of Destination ' + c[12:])


    # *****************************************************
    #               Match Weight
    # *****************************************************

    def get_weight(fp):
        next(line for line in fp if 'WEIGHT' in line or 'K' in line)
        for line in fp:
            try:
                return float(line)
            except ValueError:
                continue
        # raise ValueError("No numeric line after 'KILO'")


    with open('file_new' + str(i) + '.txt', 'rt') as fd:
        print('Weight : ', get_weight(fd))


    # *****************************************************
    #               Match Cosignee
    # *****************************************************

    def get_address_line1(fp):
        next(line for line in fp if 'Jeena' in line)
        for line in fp:
            return line


    with open('file_new' + str(i) + '.txt', 'rt') as fd:
        print('Cosignee : JEENA & COMPANY, ', get_address_line1(fd))

