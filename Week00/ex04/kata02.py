kata = (2019, 9, 25, 3, 30)

year = kata[0]
month = kata[1]
day = kata[2]
hour = kata[3]
minute = kata[4]

output = f"{month:02d}/{day:02d}/{year} {hour:02d}:{minute:02d}"
print(output)