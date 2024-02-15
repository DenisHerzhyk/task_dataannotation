with open('text.txt', 'r') as file:
    text = file.readlines()
numbers = []
id_numbers = []
step = 2
index = 0
text = sorted(text, key=lambda x: int(x.split()[0]))

for line in text:
    numbers.append(int(elem.split()[0]))

for number in numbers:
    id_numbers.append(numbers[index])
    index += step
    step += 1
    if index >= len(numbers):
        index = len(numbers) - 1
        id_numbers.append(numbers[index])
        break

for line in text:
    if (int(line.split()[0]) in id_numbers):
        print(line)
