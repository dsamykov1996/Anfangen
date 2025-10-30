# Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.

ex = input("Enter ex:\n") # 5-3+1
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
# # print(my_list)    

# new_list = list(map(int, my_list))
# print(new_list)

#-------------------

# # # 4 var


# ex = ex.replace("-", "+-")
# parts = ex.split("+")

# # map()
# sum_ex = sum(map(int, parts))
# print(sum_ex)

