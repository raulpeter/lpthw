#与print部分相结合，通过argv传递参数
from sys import argv

script, user_name = argv
prompt = '> '

print(f"hi, {user_name},I'm the {script} script")
print("I will ask u some questions")
print(f"do u like me {user_name}?")
likes = input(prompt)

print(f"where do u live {user_name}?")
lives = input(prompt)

print("what kind of computer do u have?")
computer = input(prompt)

print("""alright, so u said {likes} about liking me .
u live in {lives}.
and u have {computer} computer
""")