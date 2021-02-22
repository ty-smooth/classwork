# 1
lst = [i for i in range(1500, 2701) if i % 5 == 0 and i % 7 == 0]
print(lst)

# 2
fahrenheit = 140
convert_to_celcius = 5*((fahrenheit-32)/9)
print(convert_to_celcius)

celcius = 60
convert_to_fahrenheit = (9*(celcius/5))+32
print(convert_to_fahrenheit)

# 3
from random import choice

looping = True
ints = [*range(1,10)]
val = choice(ints)

while looping:
    guess = input("I've selected a random number between 1 to 9. Guess what it is?")
    if int(guess) == val:
        print("Well guessed!")
        looping = False

# 4
for i in range(1,6):
    print('*' * i)
    if i == 5:
        for i in reversed(range(1,5)):
            print('*' * i)

# 5
word = input("Type in a word: ")
print(''.join(reversed(word)))

# 6
series = [1,2,3,4,5,6,7,8,9]
even_count = len([i for i in series if i % 2 == 0])
odd_count = len(series) - even_count
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

# 7
datalist = [1452, 11.23, 1+2j, True, 'w3resource',
            (0, -1), [5, 12], {"class":"V", "section":"A"}]
for i in datalist:
    print(i, type(i))


# 8
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    print(i)
