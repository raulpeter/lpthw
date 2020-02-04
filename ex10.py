#\的相关用法
tabby_cat = "\tI'm tabbed in"
perisa_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"#当需要输入\时\\可以避免python混淆\后的转义符

fat_cat = """
I'll do a list
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""
print(tabby_cat)
print(perisa_cat)
print(backslash_cat)
print(fat_cat)