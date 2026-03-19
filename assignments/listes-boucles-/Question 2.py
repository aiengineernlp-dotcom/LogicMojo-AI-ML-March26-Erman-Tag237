ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
# Iterates through the dataset and removes all invalid age values
valid_ages = []
for a in ages:
    if type(a) is int and a >= 0:
        if a not in valid_ages:
            valid_ages.append(a)
    else:
        pass
    print(valid_ages)
