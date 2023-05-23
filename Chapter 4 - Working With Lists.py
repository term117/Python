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
for number in numbers:
    print(number)
print(min(numbers))
print(max(numbers))

odd_numbers = (list(range(1,20,2)))
for odd_number in odd_numbers:
    print(odd_number)

multi_3 = (list(range(3,31,3)))
for multi in multi_3:
    print(multi)

cubed = [value**2 for value in range(1,11)]
for cube in cubed:
    print(cube)

buddies = ["riley", "zach", "andrew", "ben", "michael", "jake"]
print("The first three names are:",buddies[:3])
print("Three names from the middle of the list are:",buddies[1:4])
print("The the three names from the list are:",buddies[3:6])

friend_pizzas = pizzas[:]
pizzas.append("pepperoni pizza")
friend_pizzas.append("pineapple pizza")
print("My favorite pizzas are:",pizzas)
print("My friends favorites pizzas are:",friend_pizzas)

buffet_foods = ("Chicken","Waffles","Eggs","Bacon","Sausage")
for buffet_food in buffet_foods:
    print(buffet_food)
buffet_foods_revised = ("Chicken","Waffles","Eggs","Yogurt","Pastry")
for buffet_foods_revise in buffet_foods_revised:
    print(buffet_foods_revise)