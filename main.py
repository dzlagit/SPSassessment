import random  # importing the random module
from dict import ( # importing the dictionaries from dict.py
    greetings_dict, jokes_dict, inputJoke_dict,
    howAreYou_dict, inputHowAreYou_dict,
    created_dict, validation_dict, name_dict  # importing the dictionaries from dict.py
)

def get_random_greeting(user_language): # function to get a random greeting
    language_greetings = greetings_dict.get(user_language.lower()) # getting the language from the dictionary

    if language_greetings: # if the language is found in the dictionary
        return random.choice(language_greetings) # return a random greeting from the dictionary
    else:
        raise ValueError("Language not found in the greetings dictionary.") # else raise an error

try: # try and except block to catch errors 
    while True: # while loop to keep the program running
        try: 
            user_language = input("Enter the language for your greeting: ") # getting the language from the user
            greeting = get_random_greeting(user_language) # calling the function to get a random greeting
            print(greeting)
            while True: # while loop to keep the program running
                user_input = input(">>> ").lower() # getting the input from the user
                if user_input in inputJoke_dict: # checking if the input is in the dictionary
                    print(random.choice(list(jokes_dict.values()))) # printing a random joke from the dictionary
                elif user_input in created_dict: # checking if the input is in the dictionary
                    validationInput = input("What is your name: ").lower() # getting the input from the user
                    if validationInput in validation_dict: # checking if the input is in the dictionary
                        print("You created me!")
                    else:
                        print("My creator is Arthur!")
                elif user_input in inputHowAreYou_dict: # checking if the input is in the dictionary
                    print(random.choice(list(howAreYou_dict.values()))) # printing a random response from the dictionary
                elif user_input in name_dict:
                    print(name_dict[user_input]) # printing the name from the dictionary
                elif user_input == "goodbye": # checking if the input is in the dictionary
                    print("Goodbye! Have a great day.")
                    break # breaking out of the loop
                else: # if the input is not in the dictionary
                    print("I'm sorry, I don't understand that command.")

        except ValueError as ve: # catching the error if the value is not found in the dictionary
            print(f"Error: {ve}") # printing the error and exiting the program
        except KeyError: # catching the error if the key is not found in the dictionary
            print("Unexpected input. Please try again.") # printing the error and exiting the program
        except Exception as e: # catching the error if the key is not found
            print(f"An unexpected error occurred: {e}") # printing the error and exiting the program
except KeyboardInterrupt: # catching the error if the user presses ctrl + c
    print("\nExiting the program. Goodbye!") # printing the error and exiting the program
