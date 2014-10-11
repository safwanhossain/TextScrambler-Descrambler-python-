def file_lines():

    '''(None) -> list

    Return a nested list holding the line number and the
    corresponding position associated with it'''

    file_messed = open('output_file.txt', 'r')
    global last_line_scrambled
    global line_list
    global only_lines
    line_list = []  #stores line number and corresponding position
    only_lines = [] #stores onlt line_number
    i = 0
    line = 'not blank'
    
    while line != '':

        line = file_messed.readline()
        
        colon_location = line.find(':') # find colon location in line

        if colon_location == -1:
            break

        line_list.append([])

        # create a list with the line number and position
        
        if i != 0:
            line_list[i].append(int(line[:colon_location]))
            line_list[i].append(byte_position)
            only_lines.append(int(line[:colon_location]))
            i = i + 1

        else:
            line_list[i].append(int(line[:colon_location]))
            line_list[i].append(0)
            only_lines.append(int(line[:colon_location]))
            i = i + 1

        byte_position = file_messed.tell()  #position of line in file_messed

    last_line_scrambled = line_list[-1][0]  # last line in original file
    line_list.sort()
    
    return line_list


def line_index(line_num):

    '''(int) -> int

    Return the index of a line number in line_list''' 

    for column in range(len(line_list[0])):
        for row in range(len(line_list)):
            if line_list[row][0] == line_num:
                line_num = row

                return line_num
            

def descramble(in_filename, out_filename):

    '''(file1, file2) -> None

    Take in file1, descramble it, remove line numbers and write
    to it to file2.'''

    file_messed = open(in_filename, 'r')
    file_lines()    
    file_correct = open(out_filename, 'w')
    file_messed.seek(0,0)
    
    for i in range(line_list[-1][0]):
        
        if i + 1 not in only_lines:
            line = '\n'
            
        else:

            file_messed.seek(0,0)   # resets position to 0
            i = line_index(i + 1)   # finds the index of line number
            line_position = line_list[i][1] #find the line number
            file_messed.seek(line_position, 0)
            line = file_messed.readline()
            line = line[line.find(':') + 1:] #strip the line numbers
        
        
            # Add newline char. to last line is scrambled file
            if i + 1 == last_line_scrambled:
                line = line + '\n'

            # Remove trailing newline char in
            # the last line of descrambled file
            if i + 1 == len(line_list):
                line = line.rstrip('\n')

        file_correct.write(line)
            
    file_correct.close()
        
