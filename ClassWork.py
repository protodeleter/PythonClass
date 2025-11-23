from re import findall


def print_hi(name):
    print(f'Hi, {name}')

def guessWord():
    print("Guess a word")
    print("You are allowed to make 6 mistakes")

    errors = 6
    secretWord = ["l","e", "t", "t", "e" , "r"]

    guessedWord = ["_","_","_","_","_","_"]

    for i in range(0,6):
        print(i)
        inpt = input("Enter letter")

        if inpt not in secretWord:
            print("Invalid Letter")
            errors -= 1

            if errors == 0:
                print("You are out of letters!")
                return
        else:
            for i in secretWord:



guessWord()