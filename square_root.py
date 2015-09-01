'''
1. Have your program ask the user for a positive number and
    store it in a variable
2. Have your program perform Newton's method of successive approximations to
    approximate the square root of the inputted number'''

'''
Notes: You have to start somewhere, but where?
'''

def newton_sq_rt(root_of):
    apxroot = []
    apxroot.append(root_of/2)
    n = 0
    while apxroot[n] - (root_of/apxroot[n]) > 0.01:
        apxroot.append(apxroot[n] - (root_of/apxroot[n]))
        n += 1
    return apxroot[len(apxroot)-1]

root_of = float(input("Enter a positive number: "))
print("The square root of {} is {}".format(root_of, newton_sq_rt(root_of)))
