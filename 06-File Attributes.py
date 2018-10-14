files=open('writefile.txt','r+')


print(files.mode)
print(files.name)
print(files.closed)
files.close()
