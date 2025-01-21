def is_prime(n):
    f = 0
    if n < 2:
        return "Not prime"
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            f = 1
            break
    if f == 1:
        return "not prime"
    else:
        return "prime"

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
    print(is_prime(num))
elif num < 0:
    print(f"{num} is a negative number.")
    num = int(input("Please enter a positive number: "))
    print(f"{num} is a positive number.")
    print(is_prime(num))
else:
    print(f"{num} is zero.")