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
# indeks=owoce.index("jablko")
# print(indeks)
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
# ----------------------------------------rock paper scisor****--------------------------------------------------------
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
# ----------------------------------------loops------------------------------------------------------------------------
# warzywa= ['ziemniaki','marchewki','buraki']
# for warzywo in warzywa:
#     print(warzywo)
#

# ----------------------------------------exercise avarage count--------------------------------------------------------
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
#
# #Write your code below this row 👇
# total_height=0
# number_of_students=0
# for student in student_heights:
#   total_height+= student
#   number_of_students+= 1
# avarage = round(total_height/number_of_students)
# print(avarage)
#
# --------------------------------highest score-------------------------------------------------------------------------
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
# highest_score = 0
#
# for score in student_scores :
#   if score > highest_score:
#     highest_score= score
# print(highest_score)
# ---------------------------------------------------range()function----------------------------------------------------
# total=0
# for number in range(1,101):
#     total+=number
# print(total)

# ---------------------------------------------------excercise add even numbers-----------------------------------------
#
# total=0
# for number in range(1,101):
#     if number % 2 == 0:
#         total+=number
# print(total)

# ----------------------------------------------fizz buzz---------------------------------------------------------------
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 ==0:
#         print("Buzz")
#     else:
#         print(number)
#


# -------------------------------------password generator-------------------------------------------------------------

 # Password Generator Project
#
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# # Eazy Level - Order not randomised:
# # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#
# haslo = []
# for letter in range(1, nr_letters +1):
#     haslo+= random.choice(letters)
#
# for symbol in range(1,nr_symbols+1):
#     haslo+=random.choice(symbols)
#
# for number in range(1,nr_numbers+1):
#     haslo+=random.choice(numbers)
# print(haslo)
# random.shuffle(haslo)
# print(haslo)
#
# hasło_nowe=""
# for letter in haslo :
#     hasło_nowe+=letter
# print(hasło_nowe)

# -----------------------------------------------function def-----------------------------------------------------------
#
# def moja_funkcja():
#     print("hello!")
#     print("bye")
# moja_funkcja()

# -----------------------------------while ----------------------------------------------------------------------------
# b=1
# a=6
# while b<a:
#     print(b)
#     b+=1

# --------------------------------Hangman  exercise---------------------------------------------------------------------
#Step 5
#
# import random
# from hangman_words import word_list
# from hangman_art import logo,stages

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# end_of_game = False
# lives = 6
#
#
# print(logo)
# #Testing code
# # print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     if guess in display:
#       print(f"{guess} has been already guessed")
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     #Check if user is wrong.
#     if guess not in chosen_word:
#
#         print(f"You guessed {guess} and it is not in chosen word, You lose a life")
#         lives-= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#
#     print(stages[lives])
# ------------------------------------------------functions with inputs-------------------------------------------------
# # Review:
# # Create a function called greet().
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
#
#
# def greet(name):
#   for liczba in range(3):
#     print(f"hello {name}")
#
# greet(name="Rob")
# ----------------------------------------exercise -paint calculate number of cans--------------------------------------
# import math
# def paint_calc(height, width, cover):
#     result = (test_h * test_w) / cover
#     number_of_cans = math.ceil(result)
#     print(f'You will need {number_of_cans} can of paint ')
#
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
# ---------------------------------------exercise prime numbers--------------------------------------------------------
# # Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     for num in range(2, number):
#
#         if number % num == 0:
#             is_prime = False
#     if is_prime:
#         print("It is prime number")
#     else:
#         print("It is not a prime number")
#
#
# # Write your code above this line 👆
#
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# ----------------------------------------------Caesar Cipher----------------------------------------------------------
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# shift = shift % 26
#
# def cesar(plain_text,shift_amount,cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for letter in plain_text:
#         if letter in alphabet:
#             pozycja= alphabet.index(letter)
#             shift_litera=alphabet[pozycja+shift_amount]
#             end_text += shift_litera
#         else:
#             end_text+=letter
#     print(f"The encoded text is {end_text}")
# cesar(plain_text=text,shift_amount=shift,cipher_direction=direction)
# --------------------------------------------Dictionaries Nesting-----------------------------------------------------

moje= {"lubie":1 ,"nie_lubie":2}

# print(moje["lubie"])
#
# moje["nie_wiem"]="winogrona"
#

#
# for key in moje:
#     print(key)
#     print(moje[key])
# print(moje)
# ----------------------------------dictionary exercise----------------------------------------------------------------
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
#     # 🚨 Don't change the code below 👇
# print(student_grades)

# --------------------------------------exercise dictionary------------------------------------------------------------

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_name,visits_number,cities_visited):
#
#   new_country={
#     "country":country_name,
#     "visits":visits_number,
#     "cities":cities_visited
#   }
#   travel_log.append(new_country)
#
#
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# ----------------------------------functions with outputs  ----------------------------------------------------------
#
# def format_name(f_name,l_name):
#   formated_f_name= f_name.title()
#   formated_l_name=l_name.title()
#   return(f'{formated_f_name}  {formated_l_name}')
#
# print(format_name("roBert","jasTrzebski"))

# --------------------------------------calculator project-------------------------------------------------------------
# def calculator():
#     should_continue = True
#     while should_continue:
#         def add( liczba1, liczba2):
#             return liczba1+liczba2
#         def substract(liczba1,liczba2):
#             return liczba1 - liczba2
#         def multiply(liczba1,liczba2):
#             return liczba1 * liczba2
#         def devide(liczba1,liczba2):
#             return liczba1 / liczba2
#
#         operations = {
#             "+": add,
#             "-": substract,
#             "*": multiply,
#             "/": devide,
#         }
#
#
#         liczba_1 = float(input("Podaj pierwsza liczbe "))
#
#         for operator in operations:
#             print(operator)
#
#         operator_symbol= input("wybierz operator : ")
#
#         liczba_2 = float(input("Podaj druga liczbe "))
#
#         wybrany_operator = operations[operator_symbol]
#         result = wybrany_operator(liczba_1,liczba_2)
#         print(f"{liczba_1} {operator_symbol} {liczba_2} = {result}")
#         player_response= input("Type 'y' to continue calculating or type 'n' to exit")
#         if player_response == "n":
#             should_continue = False
#             calculator()
# calculator()