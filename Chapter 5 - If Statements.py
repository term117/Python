# Chapter 5 - If Statements
motorcycle = "zx6r"
print("Is motorcycle == 'zx6r'? Yes")
print(motorcycle == 'zx6r')

print("\nIs motorcycle == 'zx6r'? No")
print(motorcycle == 'bmws1000')

game = 'Valhiem'
print(game.lower() == 'valhiem')

num = 26
if num <=11 or num >=13:
    print('\nThe number is not 12')

age = 32
if age > 18 and age >= 21:
    print('\nThey are old enough to drink and vote!')

print('')

coding_langs = ['python','C#','Java']
lang = 'python'
if lang in coding_langs:
    print(lang,"is a conding language")
lang = 'MSI'
if lang not in coding_langs:
    print(lang,'is not a coding language')

print('')

alien_color = 'yellow'
if alien_color == 'green':
    print('+5 points')
elif alien_color == 'yellow':
    print('+10 points')
elif alien_color == 'red':
    print('+15 points')

print('')

age = 32
if age < 2:
    print('This person is a baby')
elif age == 2 or age < 4:
    print('This person is a toddler')
elif age == 4 or age < 13:
    print('This person is a kid')
elif age == 13 or age < 20:
    print('This person is a teenager')
elif age == 20 or age < 65:
    print('This person is an adult')
elif age >= 65:
    print('This person is an elder')

print('')

fruits = ['black berry','mango','strawberry','watermelon']
if 'mango' in fruits:
    print('You really like mangoes')
if 'black berry' in fruits:
    print('You really like black berries')

print('')

user_name = ['king','term','cosmic','ribread','admin']
if 'king' in user_name:
    print('Hello king')
if 'term' in user_name:
    print('Hello term')
if 'cosmic' in user_name:
    print('Hello cosmic')
if 'ribread' in user_name:
    print('Hello ribread')
if 'admin' in user_name:
    print('Hello admin, would you like to see a status report?')
else: print('We need to find some user!')

print('')

current_users = ['king','term','cosmic','ribread']
new_users = ['term','ribread','kitty','anna']
if 'term' in current_users:
    print('You will need to enter a new user name')
else: print('This username is available')

if 'ribread' in current_users:
    print('You will need to enter a new user name')
else: print('This username is available')

if 'kitty' in current_users:
    print('You will need to enter a new user name')
else: print('This username is available')

if 'anna' in current_users:
    print('You will need to enter a new user name')
else: print('This username is available')

print('')

nums = list(range(1,10))
for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else: print(f'{num}th')