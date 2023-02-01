# input
# name = input('Name: ')
# age = input('Age: ')
# print('Hello', name, 'you are', age, 'years old')

#######
# arithmetic operators
# x = 9
# y = 3
# result = 9+3
# print(result)

######
# change data type
# num = input('Number: ')
# print(int(num) - 5)

######
# string methods

# hello = 'hello'.upper
# hello = 'hello'
# print(hello.upper())

# x = 'hello '
# y = 3
# print(x*y)
# returns hello hello hello

######
# List and tuples
# tupples are immutable list

##########
# loops
# for i in range(10):
#     print('Hello ')

# x = [3, 5, 76, 23, 3]
# for i in x:
#   print(x)

# for i in range(len(x)):
#     print(x[i])

# for i, element in enumerate(x):
#     print(i, element)

#########
# slice operator
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# s = 'hello'


# sliced = x[start:stop:step]

# xsliced = x[0:4:2]
# results [0, 2]

# xsliced = x[:4]
# results [0, 1, 2, 3]

# xsliced = x[4:2:-1]
# results [4, 3]

# xsliced = x[::-1]
# results = reversed list

###########
# sets

# to create an empty set
# x = set()
# to create a set with elements
# s = {4, 32, 2, 2}
# s2 = {7, 12, 2, 11}

# s.add(5)
# s.remove(2)
# print(4 in s)
# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))


##########
# dictionary
# x = {'key': 4}
# print(x['key'])
# x['key2'] = 5
# print('key' in x)
# print(list(x.values()))
# print(list(x.keys()))
# del x['key']
# for key, value in x.items():
#   print(key, value)
# for key in x:
#     print(key, x[key])


##########
# comprehensions

# x = [x + 5 for x in range(5)]
# results [5, 6, 7, 8, 9]

# x = [[0 for x in range(7)] for x in range(5)]

# x = [i for i in range(25) if i % 5 == 0]
# result [0, 5, 10, 15, 20]

# x = {i: 0 for i in range(25) if i % 5 == 0}

# print(x)

##########
# functions

# def run():
#     print('Run')

#     def func():
#         print('hi')
#     func()
# run()

# def func(x, y):
#     print('func', x, y)
#     return x * y, x / y


# print(func(5, 7))
#returns (35, 0.7142857142857143)
# r1, r2 = func(5, 6)
# print(r1, r2)
# returns 30 0.8333333333333334


##########
# unpack operator & *args and **kwargs
# def func(x):
#     def func2():
#         print(x)
#     return func2


# x = func(3)
# x()

# def func(x,y):
#   print(x, y)

# pairs = [(1,2), (3,4)]

# for pair in pairs:
#   func(*pair)


# def func(*args, **kwargs):
#   print(args, kwargs)

#########
# throw/raise exception try

# raise Exception('Bad')

# try:
#     x = 7/0
# except Exception as e:
#     print(e)

##########
# lamba

# def x(x, y): return x+y


# print(x(2, 32))

##########
# map and filter

# x = [1, 2, 3, 4, 5, 6, 47, 365, 5262, 56, 145, 25, 2]

# mp = map(lambda i: i*2, x)
# print(list(mp))

# fl = filter(lambda i: i % 2 == 0, x)
# print(list(fl))

# fstrings
# tim = 87
# x = f'hello {6+8}, {tim}'
