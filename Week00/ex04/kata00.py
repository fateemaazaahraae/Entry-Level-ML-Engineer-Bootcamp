kata = (19, 42, 21, 99, 00)

output = "The " + str(len(kata)) + " numbers are: "

output += ", ".join(map(str, kata))

print(output)
