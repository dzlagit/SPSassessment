import random
from dict import (
    greetings_dict, jokes_dict, inputJoke_dict,
    howAreYou_dict, inputHowAreYou_dict,
    created_dict, validation_dict, name_dict  #importing the dictionaries from dict.py
)

def get_random_greeting(user_language): #function to get random greeting
    language_greetings = greetings_dict.get(user_language.lower()) #get the language from the dictionary

    if language_greetings: #if the language exists
        return random.choice(language_greetings) #return a random greeting
    else:
        return "I'm sorry, I don't have greetings in that language." #if the language doesn't exist, return this

while True: #loop for the language
    user_language = input("Enter the language for your greeting: ") #ask for the language

    if user_language.lower() in greetings_dict: #check if the specified language exists

        greeting = get_random_greeting(user_language)  #get a random greeting
        print(greeting) #print the greeting

       
        while True:  #loop that ends with "goodbye"
            user_input = input(">>> ").lower() #ask for the input and always make it lowercase
            if user_input in inputJoke_dict: #if the input is in the joke dictionary
                print(random.choice(list(jokes_dict.values()))) #print a random joke
            elif user_input in created_dict:  #if the input is in the created dictionary
                validationInput = input("What is your name: ").lower() #ask for the name and make it lowercase
                if validationInput in validation_dict: #if the name is in the validation dictionary
                    print("You created me!") 
                else: #if the name is not in the validation dictionary
                    print("My creator is Arthur!") 
            elif user_input in inputHowAreYou_dict: #if the input is in the how are you dictionary
                print(random.choice(list(howAreYou_dict.values()))) #print a random response
            elif user_input in name_dict: #if the input is in the name dictionary
                print(name_dict[user_input]) #print the response
            elif user_input == "goodbye": #if the input is goodbye
                print("Goodbye! Have a great day.") 
                break #break out of the inner loop
            else: #if the input is not in any of the dictionaries 
                print("I'm sorry, I don't understand that command.") 
        break  #break out of the outer loop when the language is found
    else:
        print("Language not found in the greetings dictionary. Please try again.") #if the language is not found, print this
