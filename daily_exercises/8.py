# 1
def func():
    print("Hello World")
func()

# 2
def func1(x):
    print(f"Hi My name is {x}")
func1('Tom')

# 3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)
def func3(x,y,z):
    if z == True:
        return x
    else:
        return y
print(func3('hello','goodbye',False))

# 4.define a function func4(x,y) which returns the product of both the values.
def func4(x,y):
    return x*y
print(func4(2,4))

# 5.define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(is_even(2))

# 6.define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.
def func6(x,y):
    if x > y:
        return True
    else:
        return False
print(func6(2,3))

# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
def func7(*args):
    return sum(args)
print(func7(2,3,10))

# 8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.
def func8(*args):
    return [i for i in args if i % 2 == 0]
print(func8(2,3,10))

# 9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letteris lowercase
def func9(word):
    lst = []
    for count, val in enumerate(word.upper()):
        if count % 2 != 0:
            lst.append(val.lower())
        else:
            lst.append(val)
    return ''.join(lst)
print(func9('birthday'))


# 10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.
def func10(x,y):
    lesser = x if x < y else y
    greater = x if x > y else y
    if x % 2 == 0 and y % 2 == 0:
        return lesser
    if x % 2 != 0 or y % 2 != 0:
        return greater
print(func10(2,3))

# 11.Write a function which takes two-strings and returns true if both the strings start with the same letter.
def func11(x,y):
    str1 = x[0]
    str2 = y[0]
    if str1 == str2:
        return True
    else:
        return False
print(func11("bob", "matt"))

# 12. Create a function which takes input as a list of numbers,computes twice (or) squares the number and outputs on the terminal try using range function for this program.
def func12(lst):
    new_lst = [i*2 for i in lst]
    return new_lst
print(func12([2,3,4,5]))

# 13.A function that capitalizes first and fourth character of a word in a string.
def func13(word):
    new_word = list(word)
    new_word[0] = new_word[0].upper()
    new_word[3] = new_word[3].upper()
    return ''.join(new_word)
print(func13('birthday'))
