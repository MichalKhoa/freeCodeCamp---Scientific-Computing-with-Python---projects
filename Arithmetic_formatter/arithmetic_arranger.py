def arithmetic_arranger(problems, result=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for item in problems:
        item = item.split(" ")
        if "*" in item[1] or "/" in item[1]:
            return "Error: Operator must be '+' or '-'."
        if len((max(item))) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if item[0].isdigit() is False or item[2].isdigit() is False:
            return 'Error: Numbers must only contain digits.'
    arranged_numbers = ""
    for k, item in enumerate(problems):
        item = item.split(" ")
        numbers_from_item = []
        for i in range(len(item)):
            if item[i].isdigit() is True:
                numbers_from_item.append(int(item[i]))
        arrange_size = len(str(max(numbers_from_item))) + 2
        arranged_numbers += (item[0].rjust(arrange_size))
        if k != len(problems) - 1:
            arranged_numbers += "    "
        numbers_from_item.clear()
    arranged_numbers += "\n"
    for k, item in enumerate(problems):
        item = item.split(" ")
        for i in range(len(item)):
            if item[i].isdigit() is True:
                numbers_from_item.append(int(item[i]))
        arrange_size = len(str(max(numbers_from_item))) + 2
        arranged_numbers += (item[1].ljust(1))
        arranged_numbers += (item[2].rjust(arrange_size-1))
        if k != len(problems) - 1:
            arranged_numbers += "    "
        numbers_from_item.clear()
    arranged_numbers += "\n"
    for k, item in enumerate(problems):
        item = item.split(" ")
        for i in range(len(item)):
            if item[i].isdigit() is True:
                numbers_from_item.append(int(item[i]))
        arrange_size = len(str(max(numbers_from_item))) + 2
        arranged_numbers += "-"*arrange_size
        if k != len(problems) - 1:
            arranged_numbers += "    "
        numbers_from_item.clear()
    if result is True:
        arranged_numbers += "\n"
        for k, item in enumerate(problems):
            item = item.split(" ")
            for i in range(len(item)):
                if item[i].isdigit() is True:
                    numbers_from_item.append(int(item[i]))
            arrange_size = len(str(max(numbers_from_item))) + 2
            if item[1] == "+":

                soucet = int(item[0]) + int(item[2])
                arranged_numbers += str(soucet).rjust(arrange_size)
                if k != len(problems) - 1:
                    arranged_numbers += "    "
            if item[1] == "-":
                rozdil = int(item[0]) - int(item[2])
                arranged_numbers += str(rozdil).rjust(arrange_size)
                if k != len(problems) - 1:
                    arranged_numbers += "    "
            numbers_from_item.clear()
    return arranged_numbers