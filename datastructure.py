# list datastructure
# ordered
# indexed
# changeable/mutable


names=["Hanzo","Bi-Han","Liu","Johnny","Jax"]
names.append("Sonya")
names.insert(5,"Kano")
print(names)
names[0]="Hasashi"
print(f"My name is {names[0]}")

# tuples datastructure
# ordered
# indexed
# unchangeable/immutable

country=("Germany","Poland","France","England","Japan")
print(country)
print(f"I was born in {country[0]}")

# set datastructure
# unordered
# no index

cars={"BMW","Mercedes-Benz","Porsche","Audi","Volkswagen"}
print(cars)

# dictionary datastructure
# key value pair
# mutable

staff={"name":"George","Age":21,"Salary":"Ksh. 250,000/="}
print(f"Employee name is {staff['name']}")
print(f"Employee's age is {staff['Age']}")
print(f"Employee's salary is {staff['Salary']}")