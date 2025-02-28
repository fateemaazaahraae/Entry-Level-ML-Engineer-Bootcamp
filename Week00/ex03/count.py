import sys

def text_analyzer(string):
    ''' This function counts the number of upper characters, lower characters, punctuation and space in a given text.'''
    if string == '':
        print("What is the text to analyze?")
        return
    if isinstance(string, int):
        string = str(string)
    if string.isnumeric() == True:
        print("AssertionError: argument is not a string")
        return
    printableChar = len(string)
    upper = lower = punctuation  = space = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char == ' ':
            space += 1
        else:
            punctuation += 1
    print("The text contains ", printableChar, " printable character(s):")
    print("- ", upper, " upper letter(s)")
    print("- ", lower, " lower letter(s)")
    print("- ", punctuation, " punctuation mark(s)")
    print("- ", space, " space(s)")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("No argument provided OR YOU entered more than one argument")