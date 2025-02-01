file = open("8.filehandling/practice/mehedi/01/r1.txt", "r")

#print(file.writable())
text =  file.read()
print(text)
size = len(text)
print(size)
file.close()