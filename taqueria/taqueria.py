total = 0.0
menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

try:
    while True:
        input_item = input("item\n").lower()

        if not input_item in menu:# fail condition causing a re-prompt
            continue

        total += menu[input_item]# adds the cost of the item to the total
        print(f"total: $ {format(total, ".2f")}")

except EOFError:
    ...