#if you don't know what Exception it is going through
try:
    with open("log.txt" "r") as reader:
        reader.readline()

except Exception as e:
    print(e)

#if you know what Exception it is going through
try:
    with open("log.txt" "r") as reader:
        reader.readline()

except FileNotFoundError:
    print("File is not found in the project directory")