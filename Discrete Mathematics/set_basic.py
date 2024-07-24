a = {1, 3, 5, 7}
b = {1, 2, 4, 6, 8}

union = a.union(b)
intersection = a.intersection(b)
diffrence = a.difference(b)
symmetric_diffrence = a.symmetric_difference(b)

print("------------- Basic -------------")
print(union)
print(intersection)
print(diffrence)
print(symmetric_diffrence)

print("\n--------- A - B = A ^ B' ---------")
a_diff_b = diffrence
b_bar = union.difference(b)
a_intr_b_bar = a.intersection(b_bar)

if a_diff_b == a_intr_b_bar:
    print(True)
else:
    print(False)
