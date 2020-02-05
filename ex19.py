#函数括号内的变量和外部的变量没有必然联系
def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"u have {cheese_count} cheeses")
    print(f"u have {box_of_crackers} box of crackers")
    print("it's enough for a party")

print("we can just give the function number directly:")
cheese_and_crackers(20,30)

print("we can also use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can even do math inside")

cheese_and_crackers(10+20,5+6)
print("we can combine the two,variables and math")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+60)