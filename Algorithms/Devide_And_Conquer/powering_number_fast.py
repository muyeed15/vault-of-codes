def power(a, b):
    if b == 0:
        return 1
    
    elif b % 2 == 0:
        x = power(a, int(b/2))
        return x*x
    
    else:
        x = power(a, int(b/2))
        return x*x*a
    

print(power(3, 9))
