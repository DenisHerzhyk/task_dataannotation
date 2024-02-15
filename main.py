with open('text.txt', 'r') as file:
    text = file.readlines()
numbers_array = []
result_array = []
id_numbers = []
step = 2
index = 0
text = sorted(text, key=lambda x: int(x.split()[0]))

for line in text:
    numbers_array.append(int(elem.split()[0]))

for number in numbers_array:
    id_numbers.append(numbers_array[index])
    index += step
    step += 1
    if index >= len(numbers_array):
        index = len(numbers_array) - 1
        id_numbers.append(numbers_array[index])
        break

for line in text:
    if (int(line.split()[0]) in id_numbers):
        result_array.append(line)
        
print(result_array)
