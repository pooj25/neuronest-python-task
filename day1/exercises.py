
# 1. Check Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 2. Check Positive, Negative, or Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# 3. Print Numbers Using For Loop
for i in range(1, 11):
    print(i)

# 4. Multiplication Table
number = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 5. Sum of Numbers
total = 0
for i in range(1, 101):
    total += i
print("Sum from 1 to 100:", total)

# 6. Countdown Using While Loop
count = 5
while count >= 1:
    print(count)
    count -= 1
print("Go!")

# 7. Function to Add Two Numbers
def add(a, b):
    return a + b

print("Addition:", add(10, 20))

# 8. Function to Find Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))
