# place the variables inside the function
# they do not need to be global variables

# def count_vowels(word):
#     vowels = 'aeiou'
#     num_vowels = 0
#     for char in word:
#         if char in vowels:
#             num_vowels += 1
#     return print(num_vowels)
#
# print(count_vowels('Happy Anniversary!'))

# def minimum_value(value1, value2):
#     if value1 < value2:
#         return print(value1)
#     else:
#         return print(value2)
#
# minimum_value(5, 10)

# Complete the can_skydive function so that determines if someone can go skydiving based on these criteria.
#
# The person must be greater than or equal to 18 years old, or
# The person must have a signed consent form

# def can_skydive(age, signed_consent):
#     if age >= 18 or signed_consent == True:
#         return print("True")
#     else:
#         return print("False")

def sum_of_the_first_n_even_numbers(n):
    sum = 0
    for num in range(n):
        sum += (num + 1) * 2
    return print(sum)
sum_of_the_first_n_even_numbers(10)