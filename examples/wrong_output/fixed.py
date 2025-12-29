# Fixed version: correct average calculation

numbers = [10, 20, 30, 40]

if len(numbers) == 0:
    print("No numbers provided")
else:
    total = sum(numbers)
    average = total / len(numbers)  # FIX: correct divisor
    print("Average:", average)
