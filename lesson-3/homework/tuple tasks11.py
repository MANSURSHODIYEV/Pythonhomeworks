
my_tuple = (1, 2, 3, 2, 4, 2)
element = 2


indices = [i for i, value in enumerate(my_tuple) if value == element]

print(indices)
