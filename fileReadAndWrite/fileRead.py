file=open('C:/Users/manoj.b/PycharmProjects/Python Basic/text.txt')

#read all the content in the file
#print(file.read())

#Read file in with charter
#print(file.read(5))

#read the file line by line
#print(file.readline())
#print(file.readline())

#read the file in list mode
#print(file.readlines())

#If user want to loop in while
# line=file.readline()
# while line!="":
#     print(line)
#     line=file.readline()

#if user want loop in for
for line in file.readlines():
    print(line)

#closeing the file
file.close()