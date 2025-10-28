def triangular_number(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(triangular_number(5)) 
print(triangular_number(2)) 

# ----------------------------------------------

triangular = lambda n: 1 if n == 1 else n + triangular(n - 1)

print(triangular(5))  
print(triangular(2))
