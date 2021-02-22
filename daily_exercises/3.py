## Problem 1
phrase = "Hello World"
char = phrase[8]
print(char)

## Problem 2
word = "thinker"
sub_string = word[2:5]
print(sub_string)

## Problem 3
s = "Sammy"
print(s[2:])

## Problem 4
print(''.join(set("Mississippi")))

## Problem 5
def is_palindrome(phrase):
    lower_phrase = phrase.lower()
    clean_phrase = ''.join(char for char in lower_phrase if char.isalnum())
    reverse_phrase = ''.join(reversed(clean_phrase))
    result = "Y" if clean_phrase == reverse_phrase else "N"
    return result

print(is_palindrome("Stars"))
print(is_palindrome("O, a kak Uwakov lil vo kawu kakao!"))
print(is_palindrome("Some men interpret nine memos"))
