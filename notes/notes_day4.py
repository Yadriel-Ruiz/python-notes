class EquilateralShape:
    # A class with no state or behavior
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def calculate_perimeter(self):
        return self.num_sides * self.side_length

triangle1 = EquilateralShape(3, 1)
triangle2 = EquilateralShape(3, 100)
square = EquilateralShape(4, 1)

print(triangle1.num_sides)    # Prints 3
print(triangle1.side_length)  # Prints 1

print(triangle2.num_sides)    # Prints 3
print(triangle2.side_length)  # Prints 100

print(square.num_sides)       # Prints 4
print(square.side_length)     # Prints 1

print(triangle1.calculate_perimeter())  # Prints 3
print(triangle2.calculate_perimeter())  # Prints 300
print(square.calculate_perimeter())     # Prints 4