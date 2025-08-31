# loops.py
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "numbers is:", total)


num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number is:", reverse)

