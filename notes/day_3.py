# talking about classes and objects

# class Superhero:
#     # You want to always start with __init__ in order to initialize the class
#     # self is the first parameter of __init__
#     base_rate = 1000
#     def __init__(self, name, superpowers, villians_beaten):
#         self.name = name
#         self.superpower = superpowers
#         self.villains_beaten = villians_beaten
#
#     # You can create functions inside of classes
#     def get_rate(self):
#         superpower_bonus = len(self.superpower) * 1000
#         # get the bonus for villians beaten
#         villain_bonus = self.villains_beaten * 250
#         calculated_rate = self.base_rate + superpower_bonus + villain_bonus
#         # return the final rate
#         return calculated_rate
#
#     def describe(self):
#         print("My name is " + self.name + " and I have " + str(len(self.superpower)) + " superpowers.")
#         print(f"I have beaten {self.villains_beaten} villains.")#here is another way to type in the information by using f strings
#         print(f"My rate is {self.get_rate}.")
#
#
#
# hero1 = Superhero("Superman", ["flight", "super strength", "heat vision"], 100)
# hero2 = Superhero("Batman", ["money", "cool"], 1)
#
# print(hero1.get_rate)
#
# print(hero2.describe())

# ******************************************************
# In programming, we also want to find a specific value in a list. In this problem, we want to find the maximum value in a list of numbers.

# Quite often, the way that you solve a problem in programming is the same way that you would solve it in the real world.

# Imagine you had a printed list of 10,000 numbers. Your job is to find the biggest one. How would you go about doing it?

# Think about that for a moment and come up with the series of steps that you would use. Be really specific about what you would do.

# What's the first step in finding the biggest number?
# Do you have to remember anything? If so, you have a variable!
# What do you do after the first step?
# Can you repeat that action over and over? If so, you have a for loop!
# When you're done, what do you report (or, in the language of Python, return)?
# Once you've thought about that, please write the maximum function.

# Function name: maximum
# Parameter
# numbers - a list of numbers
# Returns - the largest value in the list of numbers
# Here are some sample inputs and outputs for the function.
#
# Input	Output
# [1]	1
# [1, 2, 3]	3
# [3, 2, 1]	3
# [1, 1, 1]	1

# def maximum(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest
# print(maximum([1, 2, 3, 24, 5, 6, 7, 8, 9]))

# def count_greater_than_100(numbers):
#     count = 0
#     for number in numbers:
#         if number > 100:
#             count += 1
#     return count

# ******************************************************
# Earlier, you found the longest string when given two strings. Now, write a function that finds the longest string in a list of strings.

# What's the first step in finding the longest string?
# Do you have to remember anything? If so, you have a variable!
# What do you do after the first step?
# Can you repeat that action over and over? If so, you have a for loop!
# When you're done, what do you report (or, in the language of Python, return)?
# Once you've thought about that, please write the longest function.

# Function name: longest
# Parameter
# strings - a list of strings
# Returns - the longest string in a list of strings
# Here are some sample inputs and outputs for the function.

# Input	Output
# ["a"]	"a"
# ["a", "bb"]	"bb"
# ["bb", "a"]	"bb"
# ["a", "bb", "ccc", "bb"]	"ccc"

def longest(strings):
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string
print(longest(["a", "bb", "ccc", "bb"]))

def yas(num_a):
    #takes the number given and adds that many a's to the string
    return "a" * num_a

