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
# #  Create an empty dictionary called student_grades.
# student_grades = {}
#
# # : Write your code below to add the grades to student_grades.👇
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
#  Write the function that will allow new countries
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
# --------------------------------------------blackjack --------------------------------------------------------------
# import random
# def deal_cards():
#     '''Zwraca karte z talii'''
#     cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card= random.choice(cards)
#     return card
#
# user_cards=[]
# computer_cards=[]
# game_over=False
#
#
# for _ in range(2):
#     user_cards.append(deal_cards())
#     computer_cards.append(deal_cards())
#
# def calculate_score(cards):
#     if sum(cards)==21  and len(cards)==2:
#         return 0
#     if 11 in cards and sum(cards)>21:
#         cards.remove(11)
#         cards.append(1)
#     score=0
#     for card in cards:
#         score+=card
#     return score
#
# def compare(user,computer):
#     if user==computer:
#         return "draw"
#     elif user == 0 :
#         return "You have a black jack"
#     elif computer == 0:
#         return "computer has blackjack"
#     elif user > 21:
#         return "you lose"
#     elif computer > 21:
#         return "computer lose"
#     elif user > computer:
#         return "You  win"
#     else:
#         return "you lose"
#
#
# while not game_over:
#
#     user_total_score=calculate_score(user_cards)
#     computer_total_score=calculate_score(computer_cards)
#     print(f'User cards: {user_cards}, Player score: {user_total_score}')
#     print(f'Computer first card is : {computer_cards[0]}')
#
#     if user_total_score == 0 or computer_total_score == 0 or user_total_score >21:
#         game_over=True
#
#     else:
#         response=input("another card ? type 'y' or type 'n' to pass : ")
#         if response == "y":
#             user_cards.append(deal_cards())
#         else:
#             game_over = True
#
# while computer_total_score !=0 and computer_total_score <17 :
#     computer_cards.append(deal_cards())
#     computer_total_score = calculate_score(computer_cards)
# print(f'computer cards{computer_cards} score: {computer_total_score}')
# print(compare(user_total_score, computer_total_score))

# --------------------------------Zgadnij liczbe------------------------------------------------------------------------
# import random
# EASY=10
# HARD=5
#
#
# def porownaj(sekretna_liczba, liczba_gracz,zycia):
#     if sekretna_liczba == liczba_gracz:
#         print(f"Zgadłeś brawo to jest liczba {sekretna_liczba}!!")
#     elif sekretna_liczba > liczba_gracz:
#         print("Twoja liczba jest zbyt niska")
#         return zycia - 1
#     else:
#         print("Twoja liczba jest zbyt wysoka")
#         return zycia - 1
#
# def ustal_poziom_trudnosci():
#
#     poziom_trudnosci = input("wybierz poziom trudnosci wpisz latwy lub trudny\n")
#     if poziom_trudnosci == "latwy":
#         return EASY
#     else:
#         return HARD
#
#
# def game():
#     print("Witaj w grze zgadnij moja liczbe :)\nMysle o liczbie pomiedzy 1-100")
#     secret_number=random.randrange(1,100)
#     # print(f"Podpowiedz liczba to {secret_number} ")
#
#     liczba_zyc = ustal_poziom_trudnosci()
#     liczba_gracza=0
#     while liczba_gracza != secret_number :
#         print(f"Masz obecnie {liczba_zyc} prób na trafienie")
#
#         liczba_gracza= int(input("zgadnij liczbe\n"))
#
#         liczba_zyc=porownaj(secret_number,liczba_gracza,liczba_zyc)
#
#         if liczba_zyc == 0:
#             print(f"Koniec gry nie masz juz zyc moja liczba to {secret_number}")
#             return
#         elif liczba_gracza !=secret_number:
#             print("zgadnij jeszcze raz")
# game()
# -------------------------------------------higher/lower game--------------------------------------------------------
#
# import random
# from art import logo , vs
# from  game_data import data
# import os
#
# def formatuj_dane(postac):
#     imie_postaci= postac["name"]
#     description = postac["description"]
#     country = postac["country"]
#     followers= postac['follower_count']
#     return (f" {imie_postaci}, a {description} from {country} {followers}")
#
# def sprawdz_odpowiedz(guess,postac_A,postac_B):
#     """uzywa if aby sprawdzic czy grac odpowiedział prawidłowo i zwraca true albo false"""
#     if postac_A>postac_B:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
#
# print(logo)
# score=0
# kontynuowac_gre = True
# losowa_postacB = random.choice(data)
#
# while kontynuowac_gre:
#     losowa_postacA = losowa_postacB
#     losowa_postacB = random.choice(data)
#
#     while losowa_postacA == losowa_postacB:
#         losowa_postacB = random.choice((data))
#
#     print(f"Compare A {formatuj_dane(losowa_postacA)}")
#     print(vs)
#     print(f"Againts B {formatuj_dane(losowa_postacB)}")
#
#     #zapytaj gracza kto ma wiecej followersów
#     guess = input("Who has more followers 'A' or 'B' ? : ").lower()
#
#
#     #sprawdz followersów dla kazdej postaci
#     postac_A_followers= losowa_postacA['follower_count']
#     postac_B_followers= losowa_postacB['follower_count']
#
#     #sprawdz czy gracz odpowiedzial dobrze
#     odpowiedz_dobra= sprawdz_odpowiedz(guess,postac_A_followers,postac_B_followers)
#     #daj odpowiedz graczowi czy odpowiedział dobrze
#
#     if odpowiedz_dobra:
#         score +=1
#         print(f"Masz racje zgadłes obecnie masz {score} punktów")
#     else:
#         print(f"NIestety nie zgadłeś finalny wynik to {score} punktów")
#         kontynuowac_gre =False

# -----------------------------------------------Coffee machine project-------------------------------------------------
#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# profit = 0
#
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True if there is enough resources to process drink"""
#     for item in order_ingredients:
#         if order_ingredients[item] >=resources[item]:
#             print(f"Sorry there is not enough {item}")
#             return False
#     return True
#
# def process_coins():
#     """Returns the total calculated from coins inserted  """
#     print("Please insert coins")
#     total = int(input("how many quarters?(quarter is $0.25 )")) * 0.25
#     total += int(input("how many dimes?(dimes = $0.10)")) * 0.10
#     total += int(input("how many nickles?(nickles = $0.05)")) * 0.05
#     total += int(input("how many pennies ?(pennies = $0.01)")) * 0.01
#     return total
#
# def is_transaction_successful(money_received, drink_cost):
#     """return true when payment is accepted, or false if money is insufficient """
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost,2)
#         print(f"Here is ${change} in change")
#         global profit
#         profit+=drink_cost
#         return True
#     else:
#         print("Sorry that is not enough money.Money refunded")
#         return False
#
# def make_coffee(drink_name,order_ingredients):
#     """Deduct the required ingredients from the resources """
#     for item in order_ingredients:
#         resources[item]-= order_ingredients[item]
#     print(f"Here is your {drink_name}")
#
#
#
#
# is_on= True
# while is_on:
#     choice= input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on=False
#     elif choice == "report":
#         print(F"Water: {resources['water']}ml")
#         print(F"Milk: {resources['milk']}ml")
#         print(F"Coffee: {resources['coffee']}g")
#         print(F"Money: $ {profit}")
#     else:
#         drink= MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment,drink['cost']):
#                make_coffee(choice,drink["ingredients"])
#
#
# #TODO: 1 Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
#
# #TODO: 2 Turn off the Coffee Machine by entering “ off ” to the prompt.
#
# #TODO: 3  Wydrukuj raport dostepnych zasobów po wspisaniu "report"
#
# #TODO: 4 Check resources sufficient?
# # a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# # not continue to make the drink but print: “ Sorry there is not enough water. ”
# # c. The same should happen if another resource is depleted, e.g. milk or coffee.
#
# #TODO: 5 Process coins.
# # a. If there are sufficient resources to make the drink selected, then the program should
# # prompt the user to insert coins.
# # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#
# #TODO: 6 Check transaction successful?
#
# #TODO: 7 Make Coffee.

# ----------------------------------------oop class--------------------------------------------------------------------
#
# class User:
#     def __init__(self,user_id,user_name):
#         self.id = user_id
#         self.username=user_name
#         self.followers=0
#         self.following=0
#
#     def follow(self,user):
#         user.followers+=1
#         self.following+=1
#
#
# user_1 = User("001","Robert")
# user_2 = User("002","Asia")
#
# user_1.follow(user_2)
# print(user_2.followers)
# print(user_1.followers)




