def counter(file_in):

    ''' (file) -> dictionary

    Return a dictionary that holds the line number as keys and the
    position of the file as its value'''

    global input_file
    global file_dict

    input_file = open(file_in, 'r')
    file_dict = {0:0}   # Set dict at the beginning of file
    line_number = 1 # Keep count of line numbers
    s = 'not blank'

    #Read every line and store its position in a dict.

    while s != '':
        s = input_file.readline()
        location = input_file.tell()
        file_dict[line_number] = location
        line_number += 1

    return file_dict

import random

def scramble(in_filename, out_filename):

    ''' (file1, file2) -> None

    Take in file1 in read mode, assign line number, scramble
    the order of the lines and then write scrambled lines into file2'''

    counter(in_filename)
    file_output = open(out_filename, 'w')
    length = len(file_dict) - 2    # Deletes 2 lines since they are overcounted

    # creates a list of unique random numbers
    line_list = random.sample(range(length), length)    
    

    # iterate over random list; finds number on the dict;
    # read line of file1 from that position 

    for i in line_list:
        position = input_file.seek(file_dict[i], 0)
        line_string = input_file.readline()

        # adds a new line char. to last line of file 1
        if i == length - 1:
            line_string = line_string + '\n'

        # remove the trailing new line char from last line in file2
        if i == line_list[-1]:
            line_string = line_string.strip()

        file_output.write(str(i + 1) + ':' + line_string)

    file_output.close()



