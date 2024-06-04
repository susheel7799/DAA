def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def check_armstrong(n, count):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** count) + check_armstrong(n // 10, count)

def is_armstrong(n):
    count = count_digits(n)
    return n == check_armstrong(n, count)
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
