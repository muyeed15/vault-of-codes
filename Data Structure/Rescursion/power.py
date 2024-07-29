def power(base, value):
    if value == 1:
        return base
    
    return power(base, value - 1) * base


print(power(2, 3))
