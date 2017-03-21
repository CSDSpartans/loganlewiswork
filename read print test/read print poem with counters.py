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
      print(line_counter, line, end = '')              
    
    line = file_input.readline()
total_lines_in_file = 32    
print("--End of Poem---")    
print(" ")
print(" ")
print("The number of stanzas is: ",stanza_counter)
print("The number of lines is: ",line_counter)
print("The total lines in this file: ",total_lines_in_file)
print("First album was The Magnificent Moodies in 1965 and the members were Ray thomas, John lodge ,and mike pinder")

file_input.close()

 Tuesday Afternoon												            by The Moody Blues

 Tuesday afternoon
 I’m just beginning to see
 Now I'm on my way
 It doesn't matter to me
 Chasing the clouds away

 Something calls to me
 The trees are drawing me near
 I've got to find out why
 Those gentle voices I hear
 Explain it all with a sigh

I'm looking at myself reflections of my mind
It's just the kind of day to leave myself behind
So gently swaying through the fairyland of love
If you'll just come with me you'll see the beauty of
Tuesday afternoon
Tuesday afternoon

Tuesday afternoon
I'm just beginning to see
Now I'm on my way
It doesn't matter to me
Chasing the clouds away

Something calls to me
The trees are drawing me near
I've got to find out why
Those gentle voices I hear
Explain it all with a sigh
