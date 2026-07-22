print("=== Implicit Type Conversion ===")

num1 = 10
num2 = 5.5
result = num1 + num2
print(f"Result: {result} (Type: {type(result)})")

print("\n=== Explicit Type Conversion ===")
age = "18"
print(type(age))
age = int(age)
print(type(age))

price = float("99.99")
marks = str(95)
number = complex(5)

print(price)
print(marks)
print(number)

print("\n=== Boolean Conversion ===")

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))
print(bool([]))
print(bool([1]))
