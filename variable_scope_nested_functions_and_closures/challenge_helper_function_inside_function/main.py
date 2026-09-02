def process_numbers(numbers):
    def square_and_add_five(x):
        return (x**2) + 5
    
    new_list = []
    for n in numbers:
        new_list.append(square_and_add_five(n))
    return new_list        

output = process_numbers([1, 2, 3])
print(output)
