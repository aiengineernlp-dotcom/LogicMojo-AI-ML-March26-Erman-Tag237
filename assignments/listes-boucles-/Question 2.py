ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
# Iterates through the dataset and removes all invalid age values
for a in ages:
    if type(a) != int:
        ages.remove(a)
        print(ages)
