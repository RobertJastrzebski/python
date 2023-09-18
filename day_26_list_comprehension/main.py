# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)
#
# ----------------------exer 1--------------------------------
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [num for num in numbers if num % 2 == 0]
#
# #Write your code 👆 above:
#
# print(result)

# ---------------------- files compare-----------------------------

with open("file1.txt") as file1:
    lista1= file1.readlines()
with open("file2.txt")as file2:
    lista2= file2.readlines()

    result=[int(num) for num in lista1 if num in lista2 ]

# Write your code above 👆

print(result)


