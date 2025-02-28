kata = (19, 42, 21)

output = "The " + str(len(kata)) + " numbers are: "

output += ", ".join(map(str, kata))

print(output)
