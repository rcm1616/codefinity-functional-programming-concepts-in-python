cube = lambda x: x*x*x

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube,numbers))

result = cubed_numbers
print(result)