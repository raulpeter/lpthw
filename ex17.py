from os.path import exists

from_file = input('form_file')
to_file = input('to_file')

print(f"copying from {from_file} to {to_file}")
indata = open(from_file).read()#这种方式读取文件后无需close
print(f"the input file is {len(indata)} bytes long")

print(f"does the output file exist? {exists(to_file)}")
print("return to continue, CTRL-C to abort")
input('?')

open(to_file,'w').write(indata)#无需close

print("done!")

