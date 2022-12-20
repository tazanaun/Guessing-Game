def main():
    print("Inside main()")
    number = number_input()

def guess_number(number):
    isGuess = False
    while not isGuess:
        guess = 50
        print("Is your number", guess, "?")
        response = input()

        if response == "yes":
            isGuess = True
        elif response == "lower":
            guess = guess/2
        elif response == "higher":
            guess = guess + 1
    return number
def number_input():
    print("Please input a number for the computer to guess between 1 and 100")
    number = int(input())
    return number
if __name__ == "__main__":
    print("Welcome to the number guessing game! You will be asked to insert a number for the computer to guess")

    main()