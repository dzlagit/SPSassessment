import random
from dict import (
    greetings_dict, jokes_dict, inputJoke_dict,
    howAreYou_dict, inputHowAreYou_dict,
    created_dict, validation_dict, name_dict  # importing the dictionaries from dict.py
)

def get_random_greeting(user_language):
    language_greetings = greetings_dict.get(user_language.lower())

    if language_greetings:
        return random.choice(language_greetings)
    else:
        raise ValueError("Language not found in the greetings dictionary.")

try:
    while True:
        try:
            user_language = input("Enter the language for your greeting: ")
            greeting = get_random_greeting(user_language)
            print(greeting)
            while True:
                user_input = input(">>> ").lower()
                if user_input in inputJoke_dict:
                    print(random.choice(list(jokes_dict.values())))
                elif user_input in created_dict:
                    validationInput = input("What is your name: ").lower()
                    if validationInput in validation_dict:
                        print("You created me!")
                    else:
                        print("My creator is Arthur!")
                elif user_input in inputHowAreYou_dict:
                    print(random.choice(list(howAreYou_dict.values())))
                elif user_input in name_dict:
                    print(name_dict[user_input])
                elif user_input == "goodbye":
                    print("Goodbye! Have a great day.")
                    break
                else:
                    print("I'm sorry, I don't understand that command.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError:
            print("Unexpected input. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
except KeyboardInterrupt:
    print("\nExiting the program. Goodbye!")
