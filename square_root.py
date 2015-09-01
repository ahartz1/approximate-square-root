def newton_sq_rt(root_of):
    '''Finds square root to minimum precision of 0.01 using Newton's method
        of successive approximations'''

    # Start with initial guess of half the input value
    apxroot = root_of/2
    n = 0
    while abs(root_of - apxroot**2) > 0.01:
        if n == 0: # I like to be grammatically correct :smiley:
            print("{} iteration,  guess is {}".format(n+1, apxroot))
        else:
            print("{} iterations, guess is {}".format(n+1, apxroot))
        apxroot  = (apxroot + root_of/apxroot)/2
        n += 1
    return apxroot

def get_input():
    root_of = input("Enter a positive number: ")
    try:
        float(root_of)
    except:
        print("Non-numeric input.".format(end=''))
        return get_input()
    if float(root_of) < 0:
        print("Negative numbers not allowed. ".format(end=''))
        return get_input()
    return float(root_of)

root_of = get_input()
print("The square root of {} is {}".format(root_of, newton_sq_rt(root_of)))
