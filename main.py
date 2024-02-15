text = ["3 love",
        "6 computers",
        "2 dogs",
        "4 cats",
        "1 I",
        "5 you"]
numbers = []
levels_array = []
id_numbers = []
text = sorted(text, key=lambda x: int(x.split()[0]))

for elem in text:
    for symbol in elem:
        if symbol.isdigit():
            numbers.append(int(symbol))

levels = len(numbers) // 2
for i in range(1, levels + 1):
    line = " " * (levels - i)
    for _ in range(i):
        line += str(numbers.pop(0)) + " "
    line += " " * (levels - i - 1)
    if not numbers:
        line = line[:-1]
    levels_array.append(line)

for i in levels_array:
    for j in reversed(i):
        if j.isdigit():
            id_numbers.append(j)
            break

for i in text:
    for j in i:
        if j in id_numbers:
            print(i)
