try:
    with open("log.txt" "r") as reader:
        reader.readline()

except Exception as e:
    print(e)

finally:
    print("not matter what try and except will do i will execute all ways when you write finally")