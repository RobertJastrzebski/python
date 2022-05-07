import random
# imie=input("what is your name")
# length = len(imie)
# print(length)
#
# print("hello"[-2])

# print(2**6)

# wynik w intach
# print(type(4//2))


#f-string------------------------------------------------------------------------------
# wynik =1
# print(f'wynik wynosi {wynik}')

# # cwiczenie1
# print('Welcome to the tip calculator!')
# do_zaplaty= float(input('What was the total bill?'))
# tip= int(input('How much tip would you like to give? 10, 12, or 15?'))
# ile_osob = int(input("How many people to split the bill?"))
#
# do_zaplaty_na_osobe=(do_zaplaty/ile_osob)*(1+(tip/100))
# finalna="{:.2f}".format(do_zaplaty_na_osobe)
# print(finalna)

# # --------if else----------------------------------
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#     print("welcome")
# else:
#     print("not welcome")
# ---------modulo %-----------------------------------
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# if number % 2 == 0:
#   print("this is even number")
# else:
#   print("this is odd number")
#
# # -------------------- if else  elif --------------------------------
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bmi = weight/height**2
# if bmi <18.5:
#   print(f"your bmi is {bmi} underweight")
# elif bmi <25:
#   print(f"your bmi is {bmi} normal weight")
# elif bmi <30:
#   print(f"your bmi is {bmi} slightly overweight")
# elif bmi <35:
#   print(f"your bmi is {bmi} slightly obese")
# else:
#   print(f"your bmi is {bmi} clinically obese.")
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#
# ------------------czy rok przystepny------------------------------
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("rok przestepny")
#         else:
#             print("nie jest rokiem przestepnym")
#     else:
#         print("rok przestepny")
# else:
#     print("nie jest rokiem przestepnym")
# ---------------------------Zadanie pizza-------------------------------
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# pizza_price = 0
# pizza_size = ""
# if size == "S":
#     pizza_price = 15
#     pizza_size = "S"
# elif size == "M":
#     pizza_price = 20
#     pizza_size = "M"
# else:
#     pizza_price = 25
#     pizza_size = "L"
#
# if add_pepperoni == "Y":
#     if pizza_size == "S":
#         pizza_price += 2
#     else:
#         pizza_price += 3
#
# if extra_cheese == "Y":
#     pizza_price += 1
#
# print(pizza_price)
# ----------------------love calculator---------------------------------------------
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# lacznie = name1 + name2
# lacznie_lower = lacznie.lower()
#
# t = lacznie_lower.count("t")
# r = lacznie_lower.count("r")
# u = lacznie_lower.count("u")
# e = lacznie_lower.count("e")
# true=t+r+u+e
# print(f'true wynosi {true}')
#
#
# l = lacznie_lower.count("l")
# o = lacznie_lower.count("o")
# v = lacznie_lower.count("v")
# e = lacznie_lower.count("e")
#
# love=l+o+v+e
# print(f'love wynosi {love}')
#
# total_love = str(true)+ str(love)
# total_love_int = int(total_love)
#
# if total_love_int <10 and total_love_int >90:
#     print(f"Your score is {total_love_int}, you go together like coke and mentos")
# elif total_love_int > 40 and total_love_int < 50:
#     print(f"Your score is {total_love_int}, you are alright together.")
# else:
#     print(f"Your score is {total_love_int}")
# ----------------random function----------------------------------------------
# random_int=random.random()*5
#
# print(random_int)
#
#
# #Write your code below this line 👇
# #Hint: Remember to import the random module first. 🎲
# import random
# random_number = random.randint(0,1)
#
#
# if random_number == 1:
#     print("orzeł")
# else:
#     print("reszka")
# ------------------------ list append function dodaje na koncu listy.--------------------------------------------------

# owoce = ["jakłko","pomarancza","banan"]
# owoce.append("truskawka")
# owoce.extend(["sliwka","jablko"])
# print(owoce)

# ----------------exercise who will pay---------------------------------------------------------------------------------
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# length_names = len(names)-1
# random_person = random.randint(0,length_names)
# imie = names[random_person]
# print(f'{imie} is going to buy the meal today!')
# -------------------------------nested list----------------------------------------------------------------------------
# warzywa= ['ziemniaki','marcheswki','buraki']
# owoce= ['czeresnie','wisnie','jablka']
# warzywa_owoce=[warzywa,owoce]
# print(warzywa_owoce)

# ------------------------------------------exercise treasure map-------------------------------------------------------
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# position_column = int(position[0])
# position_row = int(position[1])
# map[position_row-1][position_column-1]=" X   "
#
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
# ----------------------------------------rock paper scisor-------------------------------------------------------------
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# #Write your code below this line 👇
# rock_paper_scissors=["rock", "paper", "scissors"]
# computer_choice_int=random.randint(0,2)
# game_images=[rock,paper,scissors]
#
# computer_pick= rock_paper_scissors[computer_choice_int]
#
#
#
# player_choice = input("What do you choose? Rock, Paper or Scissors.\n")
# print(f'computer pick is {computer_pick}')
# print(game_images[computer_choice_int])
# print(f'Player pick is {player_choice}')
#
#
# if player_choice == computer_pick:
#     print("draw")
# elif player_choice == "rock" and computer_pick == "scissors":
#     print("player wins")
# elif player_choice == "rock" and computer_pick == "paper":
#     print("computer wins")
# elif player_choice == "paper" and computer_pick == "scissors":
#     print("computer wins")
# elif player_choice == "paper" and computer_pick == "rock":
#     print("player wins")
# elif player_choice == "scissors" and computer_pick == "rock":
#     print("computer wins")
# elif player_choice == "scissors" and computer_pick == "paper":
#     print("player wins")
# else:
#     print("incorrect answer You lose !!!")
# ----------------------------------------------------------------------------------------------------------------------