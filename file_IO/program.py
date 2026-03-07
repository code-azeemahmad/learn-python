with open(r"F:\python learning\learn-python\file_IO\sample.txt", "r") as f:
    data = f.read()
    print(data)
    
# with does not need to close the file

with open(r"F:\python learning\learn-python\file_IO\sample.txt", "a") as f:
    f.write("\nnew data to be inserted")
