def generate_fibonacci(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series


num = int(input("Enter how many Fibonacci numbers to generate: "))
result = generate_fibonacci(num)
print(f"First {num} numbers of the Fibonacci series:")
print(result)