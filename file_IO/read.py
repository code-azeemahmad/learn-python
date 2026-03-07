# we have to open a file before reading or writing
# f = open("file_name", "mode")

# data = f.read()
# f.close()

f = open(r"F:\python learning\learn-python\file_IO\demo.txt", "r")
# data = f.read()
# data = f.read(6)    # reads first five char 
data = f.readline()    # reads one line at a time   
print(data)
data = f.readline()     # moves the cursor to the end of line in file
print(data)     # one extra blank line due to \n at the end of each line
f.close()