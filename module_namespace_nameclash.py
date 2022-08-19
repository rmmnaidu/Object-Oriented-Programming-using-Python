# Program to demonstrate name clashes in different namespaces
def max(numbers): # global namespace
    print("USER DEFINED FUNCTION MAX...")
    large = -1 # local namespace
    for i in numbers:
        if i>large:
            large = i
    return large
numbers = [9, -1, 4, 2, 7]
print("Max of numbers = ",max(numbers))
print("Sum of these numbers = ",sum(numbers)) # built-in namespace
'''
USER DEFINED FUNCTION MAX...
Max of numbers =  9
Sum of these numbers =  21
'''
