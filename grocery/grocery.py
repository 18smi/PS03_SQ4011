
grocery_list = {}
try:
    while True:
        input_item = input()
        item = ""
        for i in input_item:
            item += i.upper()
        
        already_counted = False
        for i in range(0, len(grocery_list)):
            if item in grocery_list:
                grocery_list[item] += 1
                already_counted = True
                break
        if already_counted == False:
            grocery_list[item] = 1

except EOFError:
    for key in sorted(grocery_list):
        print(grocery_list[key], key)
    