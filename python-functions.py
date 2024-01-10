# # value = print("What does this print?")
# # print(value)
#
# # In python there is a value called None
# # None is a value that represents nothing
# # None is the default value for variables
# # None is the default return value for functions
# # None is the default value for parameters
# # None is the default value for optional parameters
# # None is the default value for optional arguments
#
# # example: print(None)
#
# # Print a greeting
# print("Hi, I'd like to ask you about your favorite colors.")
#
# # Ask for input
# num_colors_str = input("How many colors do you like? ")
#
# # Turn the str into an int
# num_colors = int(num_colors_str)
#
# # Print a thanks
# print("Thanks! I will now ask you for each of those.")
#
# # Create a list to store the colors
# favorite_colors = []
#
# # Loop the number of times equal to their number of favorite colors
# for color_number in range(num_colors):
#     # Remember that range creates a list starting
#     # at 0, so we add 1 to make it more readable for humans
#     num = str(color_number + 1)
#
#     # create the string prompt that will ask them for their favorite color
#     prompt = "What is your #" + num + " favorite color? "
#
#     # prompt the user for their favorite color
#     color = input(prompt)
#
#     # add the color to the list
#     favorite_colors.append(color)
#
# # sort the colors to the list
# sorted_colors = sorted(favorite_colors)
#
# # print a thank you message
# print("Thank you! I have your favorite colors as:")
#
# # print each of the colors in the sorted list
# for color in sorted_colors:
#     print(" ", color)
#
# for color_number in range(num_colors):
#     num = str(color_number + 1)
#     prompt = "What is your #" + num + " favorite color? "
#     color = input(prompt)
#
#     favorite_colors.append(color)


# def test_list(term, items):
#     for item in items:
#         if term == item:
#             return print(True)
#     return print(False)
#
#
# # Test if 3 is in [1, 2, 3, 4]
# test_list(3, [1, 2, 3, 4])  # Returns True
#
# # Test if 0 is in [1, 2, 3, 4]
# test_list(0, [1, 2, 3, 4])  # Returns False


