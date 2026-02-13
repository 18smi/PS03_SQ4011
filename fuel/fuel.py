input_string = input("input\n") + '\0'
numerator = 0
denominator = 0

invalid_input = True
while invalid_input:
    pos = 0
    while input_string[pos] != '/':
        numerator = numerator*10 + int(input_string[pos])
        pos += 1
    pos += 1
    while input_string[pos] != '\0':
        denominator = denominator*10 + int(input_string[pos])
        pos += 1

    if denominator != 0 and numerator <= denominator:
        invalid_input = False

persentage_f = (numerator * 100) / denominator


if persentage_f <= 1:
    print('E')
elif persentage_f >= 99:
    print('F')
elif persentage_f % 1 < 0.5:
    print(int(persentage_f), '%', sep='')
else:
    print(int(persentage_f) + 1, '%', sep='')
