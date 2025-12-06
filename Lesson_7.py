# lst1 = [23, 57, 13, 67, 75]
# new_lst1 = []

# for i in lst1:
#     new_lst1.append(i ** 2)

# result1 = sum(new_lst1)
# # print(result1)



# lst2 = [14, 49, 6, 64]
# new_lst2 = []

# for i in lst2:
#     new_lst2.append(i ** 2)

# result2 = sum(new_lst2)
# print(result2)



# lst3 = [8, 90, 55, 83, 1, 22]
# new_lst3 = []

# for i in lst3:
#     new_lst3.append(i ** 2)

# result2 = sum(new_lst3)
# print(result2)

# def sum_squares_nums(lst):
#     new_lst = []
#     for i in lst:
#         new_lst.append(i ** 2)

#     result = sum(new_lst)
#     return result

# lst1 = [23, 57, 13, 67, 75]

# result1 = sum_squares_nums(lst1)
# print(result1)

# lst2 = [14, 49, 6, 64]

# result2 = sum_squares_nums(lst2)
# print(result2)

# lst3 = [8, 90, 55, 83, 1, 22]

# result3 = sum_squares_nums(lst3)
# print(result3)

# def prevet():
#     print("Матвей лох")

# def add(a, b):
#     return a + b

# num = add(32, 14)
# print(num)

# import random
# import string
# def password_generatoin(lenPas, iSnums, isUpAlpha):
#     symbols = string.ascii_lowercase
#     password = ""

#     if isUpAlpha:
#         symbols += string.ascii_uppercase
#     if iSnums:
#         symbols += "1234567890"
#     for _ in range(lenPas):
#         password += random.choice(symbols)
#     return password
# print ("---Программа для удаления пароля---")
# lenPas = int(input("Введите длину сосиски: "))
# iSnums = input("Нужны ли голубцы в пароле? Y/n: ") 
# isUpAlpha = input("Нужны ли большие дома Мурино в пароле? Y/n: ")


# if iSnums.lower() == "y":
#     iSnums = True
# else:
#     iSnums = False

# if isUpAlpha.lower() == "y":
#     isUpAlpha = True
# else:
#     isUpAlpha = False

# password = password_generatoin(lenPas, isUpAlpha, iSnums)
# print(password)

# num = input("Введите число: ")
# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# if(isEven(10))


# def CountVowelsSymbols(text):
#     vowlesSymbols = "ёеыаоэяиюу"
#     count = 0
#     for i in text:
#          count += vowlesSymbols.count(i)
#     return count


def KrutoiBobik(number):
    strNumbers = str(number)
    summa = 0
    for i in strNumbers:
        summa += int(i)
    return summa
print (KrutoiBobik(123456789))
        