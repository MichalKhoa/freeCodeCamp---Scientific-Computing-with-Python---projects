from pytest import main

from arithmetic_arranger import arithmetic_arranger

# def arithmetic_arranger(*problems):
#     for item in problems:
#         item = item.split(" ")
#         arrange_size = len(max(item)) + 2
#         print(item[0].rjust(arrange_size),end="    ")
#     print("\n")
#     for item in problems:
#         item = item.split(" ")
#         arrange_size = len(max(item)) + 2
#         print(item[1].ljust(2), end="")
#         print(item[2].rjust(arrange_size-2),end="    ")
#     print("\n")
#     for item in problems:
#         item = item.split(" ")
#         arrange_size = len(max(item)) + 2
#         print("-"*arrange_size,end="    ")
#
#
# problem1 = "5860 + 14"
# problem2 = "4320 + 12"
# arithmetic_arranger(problem1, problem2)


# def arithmetic_arranger(problems, result=False):
#     if len(problems) > 5:
#         return print('Error: Too many problems.')
#     for item in problems:
#         item = item.split(" ")
#         if "*" in item[1] or "/" in item[1]:
#             return print("Error: Operator must be '+' or '-'.")
#         if len((max(item))) > 5:
#             return print('Error: Numbers cannot be more than four digits.')
#         if item[0].isdigit() is False or item[2].isdigit() is False:
#             return print('Error: Numbers must only contain digits.')
#
#     for item in problems:
#         item = item.split(" ")
#         numbers_from_item = []
#         for i in range(len(item)):
#             if item[i].isdigit() is True:
#                 numbers_from_item.append(int(item[i]))
#         arrange_size = len(str(max(numbers_from_item))) + 2
#         print(item[0].rjust(arrange_size), end="    ")
#         numbers_from_item.clear()
#     print("\n")
#     for item in problems:
#         item = item.split(" ")
#         for i in range(len(item)):
#             if item[i].isdigit() is True:
#                 numbers_from_item.append(int(item[i]))
#         arrange_size = len(str(max(numbers_from_item))) + 2
#         print(item[1].ljust(2), end="")
#         print(item[2].rjust(arrange_size-2), end="    ")
#         numbers_from_item.clear()
#     print("\n")
#     for item in problems:
#         item = item.split(" ")
#         for i in range(len(item)):
#             if item[i].isdigit() is True:
#                 numbers_from_item.append(int(item[i]))
#         arrange_size = len(str(max(numbers_from_item))) + 2
#         print("-"*arrange_size, end="    ")
#         numbers_from_item.clear()
#     print("\n")
#     if result is True:
#         for item in problems:
#             item = item.split(" ")
#             for i in range(len(item)):
#                 if item[i].isdigit() is True:
#                     numbers_from_item.append(int(item[i]))
#             arrange_size = len(str(max(numbers_from_item))) + 2
#             if item[1] == "+":
#
#                 soucet = int(item[0]) + int(item[2])
#                 print((str(soucet).rjust(arrange_size)), end="    ")
#             if item[1] == "-":
#                 print((str(int(item[0]) - int(item[2])).rjust(arrange_size)), end="    ")
#             numbers_from_item.clear()


# problem = 0
# problems = []
# print(('Zadej příklady, které chceš spočítat pod sebou.\n'
#        'Pokud už nechceš zadat žádné další, stiskni Enter.\n'
#        'Maximum příkladů, které můžeš zadat je 5.\n'
#        'Maximum cifer pro každé číslo je 5.\n'
#        'Program umí pouze sčítat a odčítat.'))
# while True:
#     problem = input()
#     if not problem:
#         break
#     problems.append(problem)
priklady = ['44 + 815', '909 - 2', '45 + 43', '123 + 49',
            '888 + 40', '653 + 87']
# problems = ["123 + 49", "1230 + 49"]
print(priklady)
print(arithmetic_arranger(priklady, result=True))
# zobrazit = [arithmetic_arranger(priklady)]
# print(zobrazit)

# Run unit tests automatically
main(['-vv'])
