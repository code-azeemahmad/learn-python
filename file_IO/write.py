# f = open("file_name", "w")      # overwrites the entire file
# f = open("file_name", "a")      # adds at the end to the file

# f = open(r"F:\python learning\learn-python\file_IO\demo.txt", "a")

f = open(r"F:\python learning\learn-python\file_IO\demo.txt", "r+")     # stream is positioned at the beginning of the file
f = open(r"F:\python learning\learn-python\file_IO\demo.txt", "a+")     # stream is positioned at the end of the file
f.write("abc")
f.close()


# w mode creates a new file if it does not exist
# w+ mode truncates the data