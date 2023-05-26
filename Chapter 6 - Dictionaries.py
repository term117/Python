# Chapter 6 - Dictionaries

# 6-1 Person
gabby = {'first_name': 'gabby', 'last_name': 'rogers', 'age': '24', 'city': 'essex'}
print(gabby['first_name'].title())
print(gabby['last_name'].title())
print(gabby['age'])
print(gabby['city'].title())

# 6-2 Favorite Numbers
fav_numbers = {'zach': '1', 'riley': '2', 'andrew': '3', 'chuck': '4', 'gabby': '5'}
print(f"Zachs favorite number is {fav_numbers['zach']}")
print(f"Rileys favorite number is {fav_numbers['riley']}")
print(f"Andrews favorite number is {fav_numbers['andrew']}")
print(f"Chucks favorite number is {fav_numbers['chuck']}")
print(f"Gabbys favorite number is {fav_numbers['gabby']}")

# 6-3 Glossary
glossary = {'variable': 'a value that can change, depending on conditions or information passed to the program.',
            'list': 'is a sequence of several variables, grouped together under a single name.',
            'unit test': 'are typically automated tests written and run by software developers to ensure that a section of an application meets its design and behaves as intended.'}
print(f"A variable is {glossary['variable']}")
print(f"a lists is {glossary['list']}")
print(f"A unit test is {glossary['unit test']}")
