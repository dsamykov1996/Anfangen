# for | while 

# 1

# n = int(input("Enter number: "))
# for i in range(n):
#     print("Hello, Python!")

# 2

# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     a, b = b, a

# for i in range(a, b + 1)
#     print(1)


# # 3

# n = int(input("Emter sec: "))

# # for i in range(n, 0 , -1):
# #     print(i)

# while n > 0:
#     print(n)
#     n -= 1 # n = n - 1


# print("Start")    

# 8

# n = int(input("Count: "))

# for i in range(1, n+1):
#     print("#" * i)

# # while n > 0:
# #     print("#" * n)
# #     n -= 1 # n = n - 1

# 9

# n = int(input("Count: "))

# # 5! = 1 * 2 * 3 * 4 * 5 -> range(1,n+1)
# # 5! = 5 * 4 * 3 * 2 * 1 -> while n > 0: n -= 1

# f = 1

# for i in range(1, n+1):
#     print(i)
#     f *= i

# print(f)    

# print("-------------")   

# f = 1
# while n > 0:
#     print(n)
#     f *= n
#     n -= 1
    
# print(f)
    

# def copy_string(text, n):
#     return (" " + text + " ") * n 

# text = input("Enter text: ")
# n = int(input("Enter n: "))
# print(copy_string(text, n))

# 3
# def sum_a_b(a, b):
#     return a + b

# num_1 = int(input("Num_1: "))
# num_2 = int(input("Num_2: "))

# print(sum_a_b(num_1, num_2))

# 4

# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     else:
#         return word[:n]
    
# string = "Letter"
# n = 30    
# print(n_letter(string, n)) 

# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     return word[:n]
#     print(1)
    
# string = "Letter"
# n = 3    
# print(n_letter(string, n)) 