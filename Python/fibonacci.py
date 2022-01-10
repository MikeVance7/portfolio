# Simple program to find desired Fibonacci Sequence value.

# Get the desired sequence number. Make sure it is a valid Int
userN = input('Which Fibboanci number would you like to see? ')
try:
    userN = int(userN)
except:
    print('That is not a valid integer.')
    exit()
assert(userN), "User input is a null value!"
assert(userN > 0), "User input must be positive!"




# Fibonacci numbers 1 or 2 are 1.
if userN == 1 or userN == 2:
    fib = 1

# Otherwise, loop through the range, adding
# the numbers together to get the result.
else:
    fb1 = 1
    fb2 = 1

    for x in range(2, userN):
        fib = fb1 + fb2
        print(fib)
        # Update fb1 and fb2 to reflect their
        # new position in the sequence.
        fb1 = fb2
        fb2 = fib
    assert(fib >= userN), "Sequence calculation failed."

print(f'Fibonacci number {userN} is {fib}.')
