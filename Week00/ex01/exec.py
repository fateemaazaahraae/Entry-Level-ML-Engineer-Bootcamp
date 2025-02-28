import sys

if len(sys.argv) > 1:
    input_string = ' '.join(sys.argv[1:])
    
    result = ''.join([char.lower() if char.isupper() else char.upper() for char in input_string[::-1]])
    
    print(result)