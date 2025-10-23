
print("--"*20)


# 1. Напишіть програму, яка приймає від користувача рядок, і відображає цей рядок у верхньому і нижньому регістрах.

# x = input("Please text a upper text:")
# y = input("Text low text:")


# print(x.lower())
# print(y.upper())

print("--"*20)

# 2. Скласти програму, яка запитує назву баскетбольної команди і повторює її на екрані зі словами: This is a champion!.

# team = input("Write your favorite team:")

# print(team + " This is a champion!")

print("--"*20)

# 3. Дано натуральне число. Знайти число, що отримується при прочитанні його цифр справа наліво.

# num = input("Text the bit number and get it reversed:")
# reversed_num = num[::-1]

# print(reversed_num)

print("--"*20)

# 4. Дано рядок. Змініть регістр символів в цьому рядку так, щоб перша буква кожного слова була великою, а інші літери - малими. (метод 's.title()')

# title = input("Write few words:")

# print(title.title())

print("--"*20)

# # 5. Дано рядок. Визначити порядковий номер першої вказаної букви. Якщо такої літери немає, вивести нуль.

# t = input("Any text:")
# f = input("Write letter, if letter is there, so you will see the digit of this letter:")

print("--"*20)

# 6. Напишіть програму, яка по введеному числу `n` від 1 до 9 виводить на екран `n` пінгвінів з відповідним номером - число від 1 до `n`. Зображення одного пінгвіна має розмір `5 x 9` символів, між двома сусідніми пінгвінами також є порожній (з пропусків) стовпець. Дозволяється вивести порожній стовпець після останнього пінгвіна. Для спрощення малювання скопіюйте пінгвіна із вихідних даних. Врахуйте, що виведення на екран виконується порядково, а не «попінгвінно».

#          _~_        _~_        _~_        _~_
# #       (o o)      (o o)      (o o)      (o o)
# #      /  V  \    /  V  \    /  V  \    /  V  \
# #     /(  1  )\  /(  2  )\  /(  3  )\  /(  4  )\
# #       ^^ ^^      ^^ ^^      ^^ ^^      ^^ ^^
# #     ```

# n = int(input("number"))

# p1 = "    _~_    "
# p2 = "   (o o)   "
# p3 = "  /  V  \\  "
# p5 = "   ^^ ^^   "

# print(p1 * n)
# print(p2 * n)
# print(p3 * n)

# nums = "1 2 3 4 5 6 7 8 9"[:2*n]
# p4 = " /(  " + "  )\\  /(  ".join(nums.split()) + "  )\\"
# print(p4)
# # p4 = " /(  "+ str(n) +r"  )\ "


# print(p5 * n)

print("--"*20)

# 7. У рядку є кілька слів, розділених одним або декількома пропусками. Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, а також всі пропуски на початку і в кінці рядка. На вхід програмі подається рядок, що складається не більше ніж з 255 символів. Надрукувати новий рядок.

#     Вхідні дані:
#     <pre>
#        Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves</pre>
#     Вихідні дані:
#     ```
#     Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves
#     ```

# text = input("Text any text with many spases:")

# text_no_space = " ".join(text.split())

# print(text_no_space)




