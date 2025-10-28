def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(6))  
print(fibonacci(1))  

# ----------------------------------------------

fibonacci = lambda n: 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  
print(fibonacci(1))