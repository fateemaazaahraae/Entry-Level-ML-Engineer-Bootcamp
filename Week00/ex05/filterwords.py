import sys
import re

if len(sys.argv) != 3:
    print("ERROR")
    sys.exit(1)

S, N = sys.argv[1], sys.argv[2]
if not N.isdigit():
    print("ERROR")
    sys.exit(1)

N = int(N)

words = re.findall(r'\b\w+\b', S)

filtered_words = [word for word in words if len(word) > N]

print(filtered_words)
