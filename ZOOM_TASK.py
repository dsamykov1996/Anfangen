# Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.

# ex = input("Enter ex:\n") # 5-3+1
# # len_ex = len(ex) #5

# n = (len(ex) + 1) // 2 #тоже самое что и int но вместо него //

# # ex[::2].split("")

# # print(int(ex[0]) + (1 if ex[1] == "+" else -1) * int(ex[2]) + (1 if ex[3] == "+" else -1) * int(ex[4]))

# # ex.replace("-", "+")


# # 2 var
# # sum = int(ex[0])
# # for i in range (1, len(ex), 2):
# #     sum += (1 if ex[i] == "+" else -1) * int(ex[i+1])

# # print(sum)

# # 3 var
# sum = int(ex[0])
# for i in range(1, len(ex)):
#     if ex[i] == "+":
#         sum += int(ex[i+1])
#     elif ex[i] == "-":
#         sum -= int(ex[i+1])
# print(sum)




# my_list = ["1", "2", 4, 7]
# # for el in range(len(my_list)):
# #     my_list[el] = (my_list[el])
# # # print(my_list)    

# # new_list = list(map(int, my_list))
# # print(new_list)

# #-------------------

# # # # 4 var


# # ex = ex.replace("-", "+-")
# # parts = ex.split("+")

# # # map()
# # sum_ex = sum(map(int, parts))
# # print(sum_ex)



# # 10. Напишіть програму, яка приймає послідовність рядків (порожній рядок для завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.

# # while True:
# #     line = input("Enter text: ")
# #     if line == ""
# #         break

# # while input() != "":
# #     print(1)    

# # a = "1"
# # while a != "":
# #     a = input()  

# # lines = []

# # while True:
# #     line = input("Enter text: ")
# #     if line == "":
# #         break
# #     lines.append(line.upper())

# # print(lines)    

# # lines = []

# # while True:
# #     line = input("Enter text: ")
# #     if line == "":
# #         break
# #     lines.append(line.upper())

# # for el in lines:
# #     print(el)

# #     lines = []

# def task10():
#     lines = []

# while True:
#     line = input("Enter text: ")
#     if line == "":
#         break
#     lines.append(line.upper())

# for el in lines:
#     print(el)

# task10()    


# numbers = [1, -2, -3, 5, 6, -3, 7, 8]

# for i in range(len(numbers) - 1):
#     if numbers[i] * numbers[i + 1] > 0:
#         print(numbers[i], numbers[i + 1])



# task 18
# 

# text = "horse, cat, parrot, goldfish, dog"
# text_list = text.split(", ")
# text_list.sort(reverse=True)

# print(" ".join(text_list))

# text = "horse, cat, parrot, goldfish, dog"
# text_list = text.split(", ")
# text_list.sort(key=str.lower, reverse=True)

# print(" ".join(text_list))

# text = "horse, cat, parrot, goldfish, dog"
# # text_list = text.split(", ")

# text_list = [w.strip() for w in text_list]

# text_list.sort(key=str.lower, reverse=True)

# print(" ".join(text_list))


# 13 

numbers = [3, 44, 6, 8, 9, 12, 7]

numbers_list = numbers.split(", ")
if numbers_list =


