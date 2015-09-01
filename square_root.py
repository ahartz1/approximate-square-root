'''
1. Have your program ask the user for a positive number and
    store it in a variable
2. Have your program perform Newton's method of successive approximations to
    approximate the square root of the inputted number


Notes: You have to start somewhere, but where?
'''


def newton_sq_rt(root_of):
    apxroot = root_of/2
    n = 0
    while abs(root_of - apxroot**2) > 0.01:
        apxroot  = (apxroot + root_of/apxroot)/2
        n += 1
    return apxroot

root_of = float(input("Enter a positive number: "))
print("The square root of {} is {}".format(root_of, newton_sq_rt(root_of)))
