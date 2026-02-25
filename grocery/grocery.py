grocery_list = {}# starts an empty grocery list

try:
    while True:
        input_item = input().upper()

        if input_item in grocery_list:
            grocery_list[input_item] += 1# if item is in the dict add one to the quantity
        else:
            grocery_list[input_item] = 1# else add the item to the dict

except EOFError:
    for key in sorted(grocery_list):# prints list in desired format
        print(grocery_list[key], key)
    