# 1 Виведіть повідомлення Hello, Python! на екран n разів (n - ціле число, яке вводить користувач).

# n = int(input("Enter number: "))
# for i in range(n):
#     print("Hello, Python!") 

# 2 Дано два цілих числа a і b (a ≤ b). Виведіть всі числа від a до b включно.


# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     a, b = b, a

# for i in range(a, b + 1)
#     print(1)

# 3 Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n, з якої слід починати відлік.

# n = int(input("Enter sec: "))

# # for i in range(n, 0 , -1):
# #     print(i)

# while n > 0:
#     print(n)
#     n -= 1 # n = n - 1

# 4 Користувач вводить кількість навчальних предметів n, а потім, відповідно, оцінки учня з n навчальних предметів. Визначте середню оцінку.

# ex = int(input("Tasks count: "))

# sum = 0

# for i in range(ex):
#     grade = int(input(f"Text grade {i+1}: "))
#     sum += grade
#     middle_grade = sum / ex

# print("middle grade:", middle_grade)

# 5 Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у порядку n, m.

# num_1 = int(input("Your number: "))
# num_2 = int(input("Text how many times you want to see your NUMBER: "))

# for i in range(num_2):
#     print(num_1, end=" ")

# 6 Напишіть програму для друку цілих чисел від n до 0 із виведенням біля кожного числа кількості символів #, що дорівнює значенню числа.

# num_5 = int(input("Text number: "))

# while num_5 > 0:
#      print(1 * num_5, "#" * num_5)
#      num_5 -= 1    

# # 7 Напишіть програму для побудови шаблону як у вихідних даних за введеним значенням n. 


# num = 9

# for i in range(1, num + 1):
#     print(str(i) * i)

# 8

# n = int(input("Count: "))

# for i in range(1, n+1):
#     print("#" * i)

# # while n > 0:
# #     print("#" * n)
# #     n -= 1 # n = n - 1

# # 10

# d = 10 
# t = 200 

# total = 0 #start 
# day = 0 #start
# current = d #in current day

# while total <= t:
#     day += 1 #incresing days
#     total += current #adding per day
#     current *= 1.1 #10%

# print(f"total will be more {t} km after {day} days.")
# print(f"total will be {total:.2f} km")    







    






