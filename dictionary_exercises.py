# Problem 1
continents = {
    "Asia": ["China", "Mongolia", "India"],
    "South America": ["Brazil", "Argentina", "Chile"],
    "North America": ["United States", "Canada", "Mexico"],
    "Antarctica": [],
    "Africa": ["South Africa", "Algeria", "Kenya", "Ethiopia", "Egypt"],
    "Europe": ["France", "Germany", "England", "Spain", "Greece", "Italy"],
    "Australia": ["New Zealand", "Australia", "Fiji"]
}

print(continents["Asia"])

grab_fiji = continents["Australia"][2]
print(grab_fiji)

sorted_continents = sorted(continents)
print(sorted_continents)


# Problem 2

programmer = {"first_name": "Wally",
              "last_name": "McCrea",
              "years_experience": 4,
              "role": "graphic designer"
              }

print("The candidate, " + programmer["first_name"] + " " + programmer["last_name"] + " has \n" + str(
    programmer["years_experience"]) + " years of experience as a " + programmer["role"] + ".")


# Problem 3

my_dict = {'a': 1, 'b': 2, 'c': 3}
square_dict = {}
for key in my_dict:
    square_dict[key] = my_dict[key] ** 2
print(square_dict)

new_dict = {}
for key in my_dict:
    new_dict[my_dict[key]] = key
my_dict = new_dict
print("my_dict = " + str(my_dict))

