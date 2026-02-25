while True:
    try:
        input_string = input("input\n").split('/')# splits the string into two numbers (denominator and numirator)
        numerator = int(input_string[0])
        denominator = int(input_string[1])
        persentage_f = (numerator * 100) / denominator# calculates persentage

        if numerator <= 0 or numerator > denominator:# fail condition
            continue


        if persentage_f <= 1:
            print('E')
        elif persentage_f >= 99:
            print('F')
        else:
            print(f"{int(round(persentage_f))}%")#  prints the rounded persentage with a '%'
        
        break
        
    except (ValueError, ZeroDivisionError):
        continue