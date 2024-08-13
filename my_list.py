my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting the value 15 at the second position in the list
my_list.insert(1, 15)

# Extending my_list with [50, 60, 70]

my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop() 

# Sort my_list in ascending order
my_list.sort()

print(my_list)

index_of_30 = my_list.index(30)
print(f"The index of the value 30 in my_list is: {index_of_30}")