'''
This program is a simple chatty bot which help you study programming.
First stage: a bot the display a greeting, its name and the date of its creation
Second stage: Implement input from the user, a small dialogue with greetings
Third stage: adding a guessing game that will predict the user age.
'''
'''
First stage: 
bot_name = "Alfred"
birth_year = 2020

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")
'''
# Second stage
bot_name = "Aid"
bot_age = 2020

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {bot_age}.")

print("Please, remind your name.")
user_name = input()
print(f"What a great name you have, {user_name}!")

# Third stage
print("Let me quess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

num1 = int(input())
num2 = int(input())
num3 = int(input())

remainder3 = num1 % 3
remainder5 = num2 % 5
remainder7 = num3 % 7
# Only works if the user types in a number between 0 and 104.
quessing_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {quessing_age}; that's a good time to start programming")