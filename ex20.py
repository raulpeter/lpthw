input_file = input("inputfile:")
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first print  the whole file:\n")

print_all(current_file)

print("let's rewind")

rewind(current_file)

print("print 3 lines")

for i in range(1,4):
    print_a_line(i, current_file)
