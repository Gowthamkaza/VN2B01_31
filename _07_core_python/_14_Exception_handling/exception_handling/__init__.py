try:
    k = 5//0  # raises divide by zero exception.
    print(k)



# handles zerodivision exception
except exception as err1:
    print("Can't divide by zero", err1)
else:
    print("no catching done")
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')