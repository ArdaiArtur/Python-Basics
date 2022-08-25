with open('filename', 'a') as f: # able to append data to file
	f.write(var1) # Were var1 is some variable you have set previously
	f.write('data') 
	f.close() # You can add this but it is not mandatory 

with open('filename', 'r') as f: # able to read data from file ( also is the default mode when opening a file in python)

with open('filename', 'x') as f: # Creates new file, if it already exists it will cause it to fail

with open('filename', 't') as f: # opens the file in text mode (also is defualt)

with open('filename', 'b') as f: # Use if your file will contain binary data
  
with open('filename', 'w') as f: # Open file with ability to write, will also create the file if it does not exist (if it exists will cause it to fail)
  
with open('filename', '+') as f: # Opens file with reading and writing

# You can combine these as you like with the + for reading and writing



# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)
