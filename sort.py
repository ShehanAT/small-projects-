my_list = [9, 3, 1, 5, 88, 22, 99]

# sort in decreasing order
my_list = sorted(my_list, reverse=True) 
print(my_list)

# sort in increasing order
my_list = sorted(my_list, reverse=False) 
print(my_list)

# another way to sort using built-in methods
my_list.sort(reverse=True)  
print(my_list)

# sort again using slice indexes
print(my_list[::-1])

