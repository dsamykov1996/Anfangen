# 1. Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення `Password accepted.`. У іншому випадку повідомлення буде `Sorry, that is the wrong password.`.



# password_accept = input("Please enter your password:")
# password = "qwerty"

# if password_accept == password:
#     print("Correct")
# else:
#     print("You wrong")

# 2. Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.

# name_1 = input("Enter first name:")
# name_2 = input("Enter second name:")

# if name_1 > name_2:
#     print("First name is", name_1)
# elif name_2 > name_1:
#     print("First name is:", name_2)
# else:
#     print("Two names started with the same letter:", name_1, name_2)    

# 3. Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або `1` або `2` або `3`, то виводиться повідомлення - назва числа, відповідно, `One`, `Two`, `Three`. В усіх інших випадках виводиться слово `Unknown`.

# num_1 = "1"
# num_2 = "2"
# num_3 = "3"

# num = input("Write your number:")

# if num == num_1:
#     print("One")
# elif num == num_2:
#     print("Two")
# elif num == num_3:
#     print("Three")
# else: 
#     print("Unknown")            

# 4. Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.

# letter_1 = input("Letter 1:")
# letter_2 = input("Letter 2:")

# if letter_1 < letter_2:
#     print(letter_1)
# else:
#     print(letter_2)    °

# Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення `A cold, isn’t it?`. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде `Cool.`, у інших випадках `Nice weather we’re having.`.

# temperature_1 = int(input("Enter tempuature:"))
# tempuature_0 = 0
# tempuature_10 = 10

# if temperature_1 < tempuature_0:
#     print("A cold, isn’t it")
# elif temperature_1 < tempuature_10:
#     print("Cool")
# elif temperature_1 == tempuature_0:
#     print("Cool")    
# else:    
#     print("Nice weather we’re having")




# 6. Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.

# figure = input("Write the number of sides and get the name of figure:")
# figure_1 = "Triangle" #3
# figure_2 = "Quadrilateral" #4
# figure_3 = "Pentagon" #5
# figure_4 = "Hexagon" #6

# if figure == "3":
#     print(figure_1)
# elif figure == "4":
#     print(figure_2)
# elif figure == "5":
#     print(figure_3)
# elif figure == "6":
#     print(figure_4) 
# else:       
#     print("Unknown")

# 7. Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.

# print ("input number from 0 to 36:")
# number = int(input())
# if number == 0:
#     print ("green")
# elif  1 <= number <= 10:
#     if number % 2 == 0:
#         print("black")
#     else:
#         print("red")

# elif 11 <= number <= 18:
#     if number % 2 == 0:
#         print("red")
#     else:
#         print("black")  
# elif 19 <= number <= 28:
#     if number % 2 == 0:
#         print("black")
#     else:
#         print("red")     
# elif 29 <= number <= 36:    
#     if number % 2 == 0:
#         print("red")  
#     else:
#         print("black")   
# else:
#     print("number is not exist")

# 8.Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат. 

# x1 = float(input("Write the distation(x1):"))                    
# x2 = float(input("Write the distation(x2):"))                    
# y1 = float(input("Write the distation(y1):"))                    
# y2 = float(input("Write the distation(y2):"))   

# a = (x1 ** 2 + y1 **2 ) ** 0.5
# b = (x2 ** 2 + y2 ** 2) ** 0.5

# if a > b:
#     print("Point A farer from the start")
# elif a < b:
#     print("Point B farer from start")
# else:
#     print("Points A and B is on the same distance from start") 

# # 10. Дано натуральное число. Визначити, чи закінчується число парною цифрою. Якщо так, то виведе True, інакше False.

# x = int(input("Input number:"))

# if (x % 10 % 2 == 0):
#     print("True")
# else:
#     print("False")     

# 12. Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем) парне або непарне. Якщо так, то виведе True, інакше False.

# y = int(input("Input number:"))

# if (y % 2 == 0):
#     print("True") 
# else:
#     print("False")    

# 13. Відомі рік і номер місяця народження людини, а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.

today_month = 10
today_year = 2025

birth_month = int(input("Input your birth month:"))
birth_year = int(input("Input your birth year:"))
age = today_year - birth_year

if today_month > birth_month:
    age = today_year - birth_year 
elif today_month == birth_month:
    age = today_year - birth_year           
else :
    age = today_year - birth_year - 1
    print("Your current age is:", age)

# я не могу придумать как сделать чтобы возраст показывало если месяц рождения меньше нынешнего месяца
