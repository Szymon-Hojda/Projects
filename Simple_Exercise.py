def space():
    print('\n')
    print(50 * '*','\n')


# 1.  Display even elemtents of set from 1 to 100.

for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=",")
space()

# 2. Display 30 elements of fibo

f_element = 1
s_element = 1
fibo = 0
print(f_element,end='-')
print(s_element,end='-')
for i in range(1, 29):
    fibo = f_element + s_element
    print(fibo,end='-')
    f_element = s_element
    s_element = fibo
space()

#3. Draw a square from random small letter for random n>4. Square must be filled and without infill.
import string
import random

small_letters = string.ascii_lowercase
random_letter = small_letters[random.randint(0,len(small_letters))]
random_n = random.randint(5,20)

# Square with infill
for i in range(0,random_n):
    print(random_letter * random_n)
space()

# Square without infill

for i in range(0,random_n):
    if i in (0,random_n - 1):
        print(random_letter * random_n)
    else:
        print(random_letter + ' ' * (random_n - 2) + random_letter)
space()

#4. Create a function which get a dictionary and return only part of it which key is not a number.

d = {'key1' : 100, 'key2' : 200, 3 : 300, 4 : 400}
new_dict = {}
print(d)
print(d.items())
for k,v in d.items():
    if k != int:
        new_dict[k] = v
print(new_dict)
# Problem with delete key which is int propably im not understand how its work with dict.

space()

#5. Create a function which is find a prime number and give new list with that numbers.
a_list = [1,2,3,4,56,73,111,'s','whatever',23.22]
def isPrime(list):
    for x in list:
        for z in range(1,x):
            if x % z == 0:
                print('its prime')

isPrime(a_list)