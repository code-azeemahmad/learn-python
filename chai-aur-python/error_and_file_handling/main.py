file = open("youtube.txt", "a")
try:
    file.write("my name is azeem\n")
finally:
    file.close()

# The with statement automatically closes the file, even if an exception occurs.
with open("youtube.txt", "a") as file:
    file.write("my name is azeem\n")


'''
"w" means write mode.
Every time you open a file in "w" mode:
1) If the file doesn't exist → Python creates it.
2) If the file already exists → Python erases all existing content before writing the new content.
'''