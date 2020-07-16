'''
This program is a simple chatty bot which help you study programming.
First stage: a bot the display a greeting, its name and the date of its creation
Second stage: Implement input from the user, a small dialogue with greetings
Third stage: adding a guessing game that will predict the user age.
Fourth stage: Learning the bot to count from 0 to any positive number the user enter.
Fifth stage: Give the user a multiple-choice test about programming, will repeat until the user answer correctly.
Lastly: refactoring each staged into function for easy readability.
'''
'''
First stage: 
bot_name = "Alfred"
birth_year = 2020

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")
'''
# Second stage
def greeting(bot_name, bot_age):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {bot_age}.")


def remind_name():
    print("Please, remind your name.")
    user_name = input()
    print(f"What a great name you have, {user_name}!")

# Third stage
def guesging_age():
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

def count():
#Fourth stage
    print("Now I will prove to you that I can count to any number you want.")

    user_number = int(input())

    for count in range(user_number + 1):
        print(f"{count} !")

def multiple_choice_test():
    print("Let's test your programming knowledge.")
    print("why do we use methods?")
    print('''1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.
    ''')

    while True:
        multiple_choice = int(input())
        if multiple_choice == 2:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again")

def end():
    print("Congratulations, have a nice day!")

greeting('Aid', '2020')  # change it as you need
remind_name()
guesging_age()
count()
multiple_choice_test()
end()