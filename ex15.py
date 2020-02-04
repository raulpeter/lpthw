#读文件
from sys import argv

script, filename = argv

txt = open(filename)

print(f"here is your file {filename}")
print(txt.read())#不加read无法读取内容，只是相当于打开了一个文件object
txt.close()

print("type the filename again:")
file_again = input()

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()