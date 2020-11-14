import random

#cpu hand choices
handzero = 0
handfive = 5
handten = 10

#cpu guess
guesszero = 0
guessfive = 5
guessten = 10
guessfifteen = 15
guesstwenty = 20

#all the results
winCount = 0
loseCount = 0
wrongCount = 0
rightCount = 0

anotherRound = ""
username = input("Enter username: ")
replay = 1
game = 1


while winCount < 2 and loseCount < 2 or replay == 1:

    win = True
    userHands = input("\n\nEnter your fingers\n 0\n 5\n or\n 10: ")
    user = input("Enter your guess: ")
    user = int(user)
    userHands = int(userHands)
    cpuHand = ""
    cpuHands = random.randrange(1, 4)
    cpuguess = ""
    cpu = ""
    Y = 1

    #cpu hand choices
    if cpuHands == 1:
        cpuHand = handzero
        cpu = random.randrange(1, 4)
    elif cpuHands == 2:
        cpuHand = handfive
        cpu = random.randrange(2, 5)
    elif cpuHands == 3:
        cpuHand = handten
        cpu = random.randrange(3, 6)
    #cpu guesses
    if cpu == 1:
        cpuguess = guesszero
    elif cpu == 2:
        cpuguess = guessfive
    elif cpu == 3:
        cpuguess = guessten
    elif cpu == 4:
        cpuguess = guessfifteen
    elif cpu == 5:
        cpuguess = guesstwenty

    #The answer
    answer = cpuHand + userHands

    #tallying the results
    if user == answer:
        winCount += 1
    elif cpuguess == answer:
        loseCount += 1
    elif cpuguess != answer and user != answer:
        wrongCount += 1
    if cpuguess == answer and user == answer:
        rightCount += 1
        winCount -= 1

    print(f"\nCPU Hands: {cpuHand}")
    print(f"\nCPU GUESS: {cpuguess}")
    print(f"\nANSWER: {answer}")
    #printing the resultsN*
    print(f"\nLOSES: {loseCount}")
    print(f"\nWINS: {winCount}")
    print(f"\nBoth wrong: {wrongCount}")
    print(f"Both right: {rightCount}")
    ######Round repetitions are still having problems
    replay = 2
    game = 2
    if winCount == 2:
        print(f"\n{username} is the WINNER!")
        game = 1

    elif loseCount == 2:
        print("\nCPU is the WINNER!")
        game = 1

    while game == 1:
        anotherRound = input(f"Another round?: (Y/N)")
        if anotherRound == "Y":
            replay = 1
            game = 2
        elif anotherRound != "Y":
            replay = 2
            game = 2

print("\n\nGAME OVER!")



