import string
import csv
import random

secret_word_list = []

with open("D:\\programming\\PY\\Hangman\\movie_list.csv", mode='r') as movie_lists:
    csv_reader = csv.DictReader(movie_lists)
    for row in csv_reader:
        secret_word_list.append(row["title"])

# get available letters

def get_available_letters(letters_guess):
    ans = list(string.ascii_lowercase+"1234567890")
    for i in letters_guess:
        if i in ans:
            ans.remove(i)
    return '/'.join(ans)


# word creator and checker
def word_creator(secret_word, letters_guess):
    ans = ""
    for i in secret_word:
        if i.lower() in letters_guess:
            ans = ans + i
        else:
            ans = ans + "_"
    return ans


# checks if the word is completed by the user
def word_incomplete():
    if "_" in word_creator(secret_movie, letters_guessed):
        return True
    else:
        return False


def check_win():
    if point == 0 and word_incomplete:
        print("\nyou lost")    
    else:
        print("\nyou won")


if __name__ == "__main__":
    while True:
        point = 8
        letters_guessed = ["a", "e", "i", "o", "u", " ", "(", ")", ":", "","."]
        secret_movie = random.choice(secret_word_list)

        while word_incomplete() and point > 0:

            print(f"\n{word_creator(secret_movie, letters_guessed)}")

            print(f"\nAvailable = {get_available_letters(letters_guessed)}")

            user_guess = input("\nEnter your letter guess: ").lower()

            if user_guess in letters_guessed:
                print("\nyou have already guessed the letter")

            elif user_guess not in secret_movie.lower():
                print("\nwrong guess")
                point -= 1
                letters_guessed.append(user_guess)
                print(f"\nyou have {point} guess left")

            elif user_guess in secret_movie.lower():
                print("\nyou have guessed correct letter")
                letters_guessed.append(user_guess)

        check_win()
        print("The correct movie was:" + secret_movie)
        docontinue = input("Do you want to continue?:")
        if docontinue.lower() != "y":
            break
