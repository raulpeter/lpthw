#dictionary
states = {'oregon':'OR','florida':'FL','california':'CA','new york':'NY','michigan':'MI'}
cities = {'CA':'san francisco','MI':'detroit','FL':'jacksonville'}
cities['NY']='new york'
cities['OR']='portland'

print("NY state has: ",cities['NY'])
print("OR state has: ",cities['OR'])

print('michigan abbreviation is : ',states['michigan'])
print('florida abbreviation is : ', states['florida'])

print('michigan has :',cities[states['michigan']])
print('florida has : ',cities[states['florida']])

for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has city {city}")

for state,abbrev in list(states.items()):
    print(f"{state} has city {cities[abbrev]}")

state = states.get('texas')
if not state:
    print('there is no texas')

city = cities.get('TX','Does not exist')#get可以为不存在的key设定一个默认value
print(f"city for state 'TX' is {city}")