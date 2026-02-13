input_string = input("m/d/y number or words\n") + '\0'
day = ""
month = ""
year= ""

if (input_string[0].isdigit()):
    pos = 0
    while input_string[pos] != '/':
        month += input_string[pos]
        pos += 1
    if len(month) == 1:
        month = '0' + month
    pos += 1
    while input_string[pos] != '/':
        day += input_string[pos]
        pos += 1
    if len(day) == 1:
        day = '0' + day
    pos += 1
    while input_string[pos] != '\0':
        year += input_string[pos]
        pos += 1
    print(year + '/' + month + '/' + day)

else:
    pos = 0
    while input_string[pos] != ' ':
        month += input_string[pos].lower()
        pos += 1
    pos += 1
    while input_string[pos] != ' ':
        day += input_string[pos]
        pos += 1
    if len(day) == 1:
        day = '0' + day
    pos += 1
    while input_string[pos] != '\0':
        year += input_string[pos]
        pos += 1

    if month == "january":
        month = "01"
    elif month == "febuary":
        month = "02"
    elif month == "march":
        month = "03"
    elif month == "april":
        month = "04"
    elif month == "may":
        month = "05"
    elif month == "june":
        month = "06"
    elif month == "july":
        month = "07"
    elif month == "august":
        month = "08"
    elif month == "september":
        month = "09"
    elif month == "october":
        month = "10"
    elif month == "november":
        month = "11"
    elif month == "december":
        month = "12"

    print(year + '/' + month + '/' + day)
    