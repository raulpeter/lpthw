#encode decode
input_encoding = input("input_encoding")
error = input("error")

def main(language_file,encoding,errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding,errors)
        return main(language_file,encoding,errors)#相当于创建了循环，用if来跳出循环

def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors=errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)
    print(raw_bytes,"<===>",cooked_string)

languages = open('languages.txt',encoding="utf-8")

main(languages,input_encoding,error)