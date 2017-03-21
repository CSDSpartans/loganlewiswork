name_of_mydocument = 'poe'
file_input = open(name_of_mydocument, 'r')     

line = file_input.readline()
print(line, end = '')

line = file_input.readline()
print(line, end = '')

line = file_input.readline()
print(line, end = '')

line_counter = 0
stanza_counter = 1

line = file_input.readline()
while line != '':                                     
    if line == '\n':
      stanza_counter += 1
      print(" ")
    else:
      line_counter += 1 
      print(line_counter,")   ", line, end = '')              
    
    line = file_input.readline()
total_lines_in_file = 32    
print("--End of Poem---")    
print(" ")
print(" ")
print("The number of stanzas is: ",stanza_counter)
print("The number of lines is: ",line_counter)
print("The total lines in this file: ",total_lines_in_file)
print("The members were Ray Thomas, John Lodge, Justin Hayward, Graeme Edge,and Mike Pinder")
print("The song \"Tuesday Afternoon\" first appeared on the album \x1B[3mDays of Future Passed\x1b[23m in 1967.")

file_input.close()
