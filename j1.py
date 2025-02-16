# Arithmetic Operators
print("Arithmetic Operators:")
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(f"Addition (x + y): {x + y}")      # Addition
print(f"Subtraction (x - y): {x - y}")   # Subtraction
print(f"Multiplication (x * y): {x * y}") # Multiplication
print(f"Division (x / y): {x / y}")       # Division (float result)
print(f"Floor Division (x // y): {x // y}") # Floor Division (integer result)
print(f"Modulus (x % y): {x % y}")        # Modulus (remainder of division)
print(f"Exponentiation (x ** y): {x ** y}") # Exponentiation (x raised to the power of y)

print("\nBitwise Operators:")
# Bitwise Operators
a = 12  # 1100 in binary
b = 10  # 1010 in binary

print(f"Bitwise AND (a & b): {a & b}")   # AND (binary 1100 & 1010 = 1000)
print(f"Bitwise OR (a | b): {a | b}")    # OR (binary 1100 | 1010 = 1110)
print(f"Bitwise XOR (a ^ b): {a ^ b}")   # XOR (binary 1100 ^ 1010 = 0110)
print(f"Bitwise NOT (~a): {~a}")         # NOT (inverts all bits)
print(f"Left Shift (a << 2): {a << 2}")  # Left Shift (shifts bits left, multiplying by 2^2)
print(f"Right Shift (a >> 2): {a >> 2}") # Right Shift (shifts bits right, dividing by 2^2)

print("\nLogical Operators:")
# Logical Operators
x = True
y = False

print(f"x and y: {x and y}")  # AND (both need to be True for the result to be True)
print(f"x or y: {x or y}")    # OR (either needs to be True for the result to be True)
print(f"not x: {not x}")      # NOT (inverts the boolean value)