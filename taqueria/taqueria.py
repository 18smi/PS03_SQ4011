total = 0.0
try:
    while True:
        input_item = input()
        item = ""
        for i in input_item:
            item += i.lower()

        if item == "baja taco":
            total += 4.25
        elif item == "burrito":
            total += 7.50
        elif item == "bowl":
            total += 8.50
        elif item == "nachos":
            total += 11.00
        elif item == "quesadilla":
            total += 8.50
        elif item == "super burrito":
            total += 8.50
        elif item == "super quesadilla":
            total += 9.50
        elif item == "taco":
            total += 3.00
        elif item == "tortilla salad":
            total += 8.00
        print("total: $", format(total, ".2f"), sep='')

except EOFError:
    print("")