ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
# Iterates through the dataset and removes all invalid age values
valid_ages = []
for a in ages:
    if type(a) is int and a >= 0:
        if a not in valid_ages:
            valid_ages.append(a)
    else:
        pass
    '''Stores only valid ages in a new list.'''
print(valid_ages)
print('\n')
'''Calculates the average age of valid customers.'''
average = 0
for c in valid_ages:
    average =(sum(valid_ages)/len(valid_ages))
print (f"\n the average is : {average}")

print('\n')
"""Displays the list of customers whose age is greater than 30."""
is_greater_list = []
for a in valid_ages:
    if a>30:
        is_greater_list.append(a)
print(is_greater_list)



