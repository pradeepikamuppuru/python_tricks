import math

N = int(input("Enter a number: "))
square = int(math.sqrt(N))
divisors = []
for i in range(1, square + 1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            # Add the counterpart divisor to the list
            divisors.append(N // i)

# Sort the divisors list for better readability (optional)
divisors.sort()

print(divisors)
