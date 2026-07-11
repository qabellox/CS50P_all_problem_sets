# Get arithmetic expression from user
exp = input("Expression: ")
# Remove leading/trailing whitespace
exp = exp.strip()
# Split the expression into three parts (x, operator, z)
exp = exp.split()

# Convert first and third parts to floats
num1 = float(exp[0])
num2 = float(exp[2])

# Perform the operation based on the operator
if exp[1] == "+":
    print(num1 + num2)
elif exp[1] == "-":
    print(num1 - num2)
if exp[1] == "*":
    print(num1 * num2)
if exp[1] == "/":
    print(num1 / num2)
