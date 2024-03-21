
f= open("file.txt", "w")
f.write("#This is the first line\n")
f.write("#This is the second line\n")


with open("file.txt", "a") as f:
    f.write("first line\n")
    f.write("second line")

try:
    with open("file1.txt", "a") as f:
        f.readline
    f.close

except Exception as e:
    print("Please check the file name")


#print(dir(f))