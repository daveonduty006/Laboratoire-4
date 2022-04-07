f = open("bd_original.txt", "r", encoding="utf8")

line = str(f.readlines()[2][1:5])

f.close()

print(line)

