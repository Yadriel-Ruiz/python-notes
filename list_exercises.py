list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

numbers = [1, 2, 3, 4, 5, 6, 7]
list2 = []
for num in numbers:
    num = num ** 2
    list2.append(num)
print(list2)


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)