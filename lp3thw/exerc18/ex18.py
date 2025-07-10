# Exercise 18 - Names, Variables, Code, Functions

# The first function is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg):
    print(f"arg1: {arg}")

# this one takes no arguments
def print_none():
    print("I got nothin' for ya, bud.")


print_two("Samkelwa", "G")
print_two_again("Samke", "G2")
print_one("First!")
print_none()
