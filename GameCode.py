answer = 5

print("Please guess the number between 1 and 10: ")
guess = int(input())

if guess < answer :
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it correctly!")
    else:
        print("Sorry,you have not guessed correctly")
elif guess > answer:
    print("Please guess low")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry,you have not guessed correctly")

else:
    print("You got it first time")
