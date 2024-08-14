def power(a, b):
    if b < 0:
        a = 1/a
        b = -b
    
    if b == 0:
        return 1
    
    elif b % 2 == 0:
        x = power(a, float(int(b/2)))
        return x*x
    
    else:
        x = power(a, float(int(b/2)))
        return x*x*a
    

print(power(3, 9))
