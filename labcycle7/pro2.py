file = open("File1.txt","r")
file2 = open("File2.txt","w")
line = file.readlines()
for i in range(len(line)):
        if(i%2!=1):
                file2.write(line[i])
file.close()
file2.close()
