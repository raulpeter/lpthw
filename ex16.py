#读写文件
from sys import argv

#
filename = input('filename is:')
print(f"we're going to erase {filename}")
print("if u don't want that, hit CTRL-C ")
print("if u do want that, hit return")
input('?')

print("opening the file...")
target = open(filename,'w')
print("truncating the file")
target.truncate()
print("now I'll ask u for 3 lines")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to wirte these to the file")
target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("finally we close it")
target.close()
