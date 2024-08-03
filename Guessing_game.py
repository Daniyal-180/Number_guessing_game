import random     # import the ramdom library

def guessing_number():
  """ Define a function of number guessing game """
    start_num = 1
    end_num = 20
    secert_num = random.randint(start_num, end_num)    # Secert random num is guess by computer using random module.
    my_guesses = 0
    print(f"**___Welcome to a number guessing game___**")
    print(f"--->Guess a number between {start_num} and {end_num}<---")

    while True:
        try:
            guess_num = int(input("\tEnter a guess number: "))

            if guess_num < start_num or guess_num > end_num:
                print(f"Please guess the number between {start_num} and {end_num}")
                continue

            my_guesses += 1

            if guess_num == secert_num:
                print(f"'Congratulations!' You have successfully guess the sceret number in {my_guesses} rounds")
                break
                
            elif guess_num<secert_num:
                print(f"Your guess number is too low")

            elif guess_num > secert_num:
                print(f"Your guess number is too high")
                
        except ValueError:
            print(f"Invalid input. Please enter a valid input")

guessing_number()
