import sys

print(sys.argv)
if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
    if sys.argv[1].isnumeric() == False:
        print("AssertionError: argument is not integer")
        exit()
    s = int(sys.argv[1])
    if s == 0:
        print("I'm Zero.")
    elif s % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")