"""
    Exercise : Create a quizzing game.
    Make an HTTP request to the Open Trivia API at each round of the game to get a new question
    and present it to the user to answer. At the end of each round ask the user if he wants to play again.
    Keep playing forever until the user types 'quit'.
"""
import random
import requests
import json
from colorama import Fore

url = "https://opentdb.com/api.php?amount=1"
total_questions: int = 0
score: int = 0

print("======================================================================================")
print("                           WELCOME TO THE TRIVIA GAME")
print("======================================================================================")
while True :
    try :
        r = requests.get("http://www.google.com")
    except:
        print(Fore.RED + "Something went wrong. Please check your Internet Connection.")
        exit(1)

    r = requests.get(url)

    if 200 != r.status_code :
        print(Fore.RED + "There was an unexpected Error retrieving the question.")
    else :
        total_questions += 1
        question = json.loads(r.text)
        print("\nQuestion", total_questions, ":", question["results"][0]["question"])
        print("Options")
        options = [question["results"][0]["incorrect_answers"][0], question["results"][0]["incorrect_answers"][1],
                   question["results"][0]["incorrect_answers"][2], question["results"][0]["correct_answer"]]
        random.shuffle(options)
        correct_index = options.index(question["results"][0]["correct_answer"])
        print("(A)", options[0])
        print("(B)", options[1])
        print("(C)", options[2])
        print("(D)", options[3])
        data_valid = False
        while not data_valid :
            choice = ord(input("Your Choice : ").upper()) - 65
            if choice < len(options) :
                data_valid = True
            else :
                print(Fore.RED + "Invalid Choice!")
        if choice == correct_index :
            print(Fore.GREEN + "Voila! You got it right!")
            score += 1
        else :
            print(Fore.RED + "Incorrect Answer!")
            print(Fore.YELLOW + "The Correct Answer is :", options[correct_index])
    print(Fore.RESET + "\nIf you wish to quit the game and see your score, type 'quit'. Otherwise press Enter.")
    reply = input().lower()
    if reply == "quit" :
        break

print("\n===============================================")
print("Total Number of Questions Answered :", total_questions)
print("Number of Correct Answers :", score)
print("===============================================")
