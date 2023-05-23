# Chapter 4 - Working With Lists
pizzas = ['mushroom pizza','ham pizza','sausage pizza']
for pizza in pizzas:
    print(pizza,'is my favorite kind of pizza!')
print('I really love pizza!')

pets = ['cat','dog','hamster']
for pet in pets:
    print('A',pet,'would make a great pet!')
print('You can find all these animals at petsmart!')

for value in range (1,21):
    print(value)
numbers = list(range(1,1000001))
print(numbers)
print(min(numbers))
print(max(numbers))

odd_numbers = (list(range(1,20,2)))
print(odd_numbers)

multi_3 = (list(range(3,31,3)))
print(multi_3)

cubed = [value**2 for value in range(1,11)]
print(cubed)

buddies = ["riley", "zach", "andrew", "ben", "micheal", "jake"]
print("The first three names are:",buddies[:3])
print("Three names from the middle of the list are:",buddies[1:4])
print("The the three names from the list are:",buddies[3:6])

friend_pizzas = pizzas[:]
pizzas.append("pepperoni pizza")
friend_pizzas.append("pineapple pizza")
print("My favorite pizzas are:",pizzas)
print("My friends favorites pizzas are:",friend_pizzas)