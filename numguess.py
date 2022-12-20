def main():
    print("Inside main()")
    number = number_input()
    print(guess_number(number))
def guess_number(number):
    isGuess = False
    max = 100
    min = 0
    mid = max/2
    while not isGuess:
        
        print("Is your number", mid, "?")
        response = input()
        

        if response == "yes":
            isGuess = True
            print("The computer guessed your number!")
        elif response == "lower":
            max = mid
            mid = (max+min)/2
        elif response == "higher":
            #wont work rn
            min = mid
            mid = (max+min)/2
    return mid
    
def number_input():
    print("Please input a number for the computer to guess between 1 and 100")
    number = int(input())
    return number
if __name__ == "__main__":
    print("Welcome to the number guessing game! You will be asked to insert a number for the computer to guess")

    main()