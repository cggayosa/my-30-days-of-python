# EXERCISE:
# Day 1, Exercise Level 1

# 1. Check the python version you are using
print('Python version: 3.14.4')

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
# Addition (+)
print('Addition: ', 3+4)
# Subtraction (-)
print('Subtraction: ', 3-4)
# Multiplication (*)
print('Multiplication: ', 3*4)
# Division (/)
print('Division: ', 3/4)
# Exponential (**)
print('Exponential: ', 3**4)

# 3. Write strings on the python interactive shell. The strings are the following
# Your name
print('Caitlin')
# Your family name
print('Gayosa')
# Your country
print('Philippines')
# I am enjoying 30 days of python
print('I am enjoying 30 days of python ')

# 4. Check the data types of the following data: 
# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4 - 4j
print(type(4-4j))
# ['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))
# Your name
print(type('Caitlin'))
# Your family name
print(type('Gayosa'))
# Your country
print(type('Philippines'))


# Day 1, Exercise Level 2 
# Create a folder named day_1 inside 30DaysOfPython folder.
# Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. 
# Remember to use print() when you are working on a python file. 
# Navigate to the directory where you have saved your file, and run it.
# ALREADY DONE

# Day 1, Exercise Level 3
# Write an example for different Python data types such as:
# Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
my_int = 3
my_float = 0.96
my_complex = 5-10j

my_string = 'day1string'
my_boolean = True

my_list = ['apple','oranges',1611,'banana']
my_tuple = ('UCB','UCLA',1919,'USC')
my_set = {'green','yellow','blue'}
my_dict = {'quote1':'Hello there!','quote 2':'Hello, indeed.'}

print(my_int)
print(my_float)
print(my_complex)

print(my_string)
print(my_boolean)
print(my_list)
# Find an Euclidean distance between (2, 3) and (10, 8)
x1,y1 = 2,3
x2,y2 = 10,8
euclidean_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('Euclidean Distance between (2, 3) and (10, 8):', f'{euclidean_distance:.2f}') 