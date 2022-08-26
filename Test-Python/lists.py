# First list example
# Indexes start with 0.

edutainers = ['Adam', 'Aubri', 'Daniel', 'Jo', 'Justin', 'Zach']

print('Edutainers: ', edutainers)
print('The third edutainer is: ', edutainers[3])
print('Edutainer 0: ', edutainers[0])

# How do I know how many elements there are programmatically? Use "len()"

print('The number of edutainers are: ', len(edutainers))
print(edutainers[3], ' has ', len(edutainers[3]), 'characters.')
edutainers.append('Lance')  # Add an element to the end of a list
print('Edutainers: ', edutainers)
del edutainers[2]  # Remove an element from a list
print('Edutainers: ', edutainers)
special = edutainers.pop(0)  # Remove an element from the end of a list.
print('Edutainers: ', edutainers)
print('Special: ', special)
edutainers[2] = 'Dan'  # Change an element in a list
print('Edutainers: ', edutainers)

# Sort a list
numbers = [31, 2, 43, 0, 9, 10, 45]
letters = ['b', 'c', 'e', 'd']
edutainers = ['Jo', 'Justin', 'Vonne', 'Cherokee']

# Sort in ascending order
#sorted_numbers=numbers.sort(key, None, reverse, False)
sorted_numbers = sorted(numbers)
print('Sorted Numbers: ', sorted_numbers)
print('Numbers: ', numbers)

sorted_letters = sorted(letters)
print('Sorted Letters: ', sorted_letters)
print('Letters: ', letters)

sorted_edutainers = sorted(edutainers)
print('Sorted Edutainers: ', sorted_edutainers)
print('Edutainers: ', edutainers)

# Descending order
sorted_letters = sorted(letters)
des_letters = sorted(letters, reverse=True)

print('Letters: ', letters)
print('Sorted Letters: ', sorted_letters)
print('Descending Letters: ', des_letters)

# Reversing a list
reversed_edutainers = list(reversed(edutainers))
print(edutainers)
print('Reversed Edutainers: ', reversed_edutainers)
