# Buggy version: calculates average incorrectly

numbers = [10, 20, 30, 40]

total = 0
for n in numbers:
    total += n

average = total / (len(numbers) - 1)  # BUG: wrong divisor

print("Average:", average)
