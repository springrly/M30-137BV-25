values = [3, 1, 3, 2, 1, 5, 2]

unique_values = set(values)
print(unique_values, len(unique_values), len(values) != len(set(values)))

other = {2, 4, 5}

v1 = unique_values & other
v2 = unique_values | other
v3 = unique_values - other
v4 = other - unique_values
print(v1, v2, v3, v4)