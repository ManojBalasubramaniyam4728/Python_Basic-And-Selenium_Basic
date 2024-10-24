with open("C:/Users/manoj.b/PycharmProjects/Python Basic/text.txt","r") as reader:
    list=reader.readlines()
    with open("C:/Users/manoj.b/PycharmProjects/Python Basic/revers.txt","w") as write:
        for line in reversed(list):
            write.write(line)