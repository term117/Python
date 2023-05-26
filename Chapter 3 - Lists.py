# Chapter 3 - Lists

# 3-1, 3-2 Names and Greetings
names = ['zach', 'riley', 'andrew']
print(names[0])
print(names[1])
print(names[2])
message = 'Get online'
print(message, names[0])
print(message, names[1])
print(message, names[2])

# 3-3 Your Own Lists
bikes = ['Kawasaki', 'Suzuki', 'Honda']
print('\nI use to own a', bikes[1])
print('I have a', bikes[0])
print('I want to get a', bikes[2])

print('')

# 3-4, 3-5 Guest List and Changing Guest List
guestList = ['Neil Armstrong,', 'Neil Degrasse Tyson,', 'Galileo Galilei,']
message = 'I would like to formal invite you for dinner tonight.'
print(guestList[0], message)
print(guestList[1], message)
print(guestList[2], message)
print(guestList[1], 'will not be attending tonight.')
del guestList[1]
guestList.append('Kitboga,')
print(guestList[0], message)
print(guestList[1], message)
print(guestList[2], message)
print(len(guestList))

print('')

# 3-8 Seeing the World
places = ['tokyo', 'hawaii', 'jamaica', 'germany', 'greece']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(len(places))
