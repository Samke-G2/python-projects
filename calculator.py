# Calculator Project                        13/02/2025                                 16:34

print("This is a simple calculator")
print("To use it, type the operation first and then the values like this:")

print("Add 1 to 9")             # 10
print("or")
print("Subtract 5 from 10")     # 5
print("or")
print("Divide 18 by 6")         # 3
print("or")
print("Multiply 4 by 9")        #36

print("The first word MUST be capitalised.")

user_input = input("What would you like to calculate? ")

# I will need a function for each operation
def add(a, b):
    x = float(a)
    y = float(b)
    result = x+y
    return result

def subtract(a, b):
    x = float(a)
    y = float(b)
    result = y-x
    return result

def divide(a, b):
    x = float(a)
    y = float(b)
    result = x/y
    return result

def multiply(a, b):
    x = float(a)
    y = float(b)
    result = x*y 
    return result

# First I need to split the input in order to access its different parts
calc_ls = user_input.split()

# Next, some if statements to see which operation to use in the calculation
def calculation(lis):
    final = 0
    if "Add" in lis:
        final = add(lis[1], lis[3])
    elif "Subtract" in lis:
        final = subtract(lis[1], lis[3])
    elif "Multiply" in lis:
        final = multiply(lis[1], lis[3])
    elif "Divide" in lis:
        final = divide(lis[1], lis[3])
        
    return final

# print the result of the calculation
answer = calculation(calc_ls)
print(f"The result of your calcualtion is: {answer}")
