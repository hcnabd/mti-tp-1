def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))
print(factorial_iterative(2))

# ----------------------------------------------

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))
print(factorial(2))
