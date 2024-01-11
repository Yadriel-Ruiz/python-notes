# place the variables inside the function
# they do not need to be global variables

def count_vowels(word):
    vowels = 'aeiou'
    num_vowels = 0
    for char in word:
        if char in vowels:
            num_vowels += 1
    return print(num_vowels)

print(count_vowels('Happy Anniversary!'))