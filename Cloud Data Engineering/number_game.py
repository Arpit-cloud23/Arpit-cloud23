# i am going to make a simple game of guessing a simple number
n = 6
i = 1
while i<=5:
    guessed = int(input("enter the guess"))
    if guessed > n:
        print("go back and guesses left are ",5-i)
        if i==5:
            print("GAME OVER")
            break
            print("go back and guesses left are ", 5-i)
    elif guessed < n:
        if i==5:
            print("GAME OVER")
            break
        print("go forward and guesses left are ", 5 - i)
    elif guessed == n:
        print("you won with chances left ",5-i)
        break
    i = i + 1

# #next method
import random
win = random.randint(1,100)
c = 1
while(c<=5):
    guess = int(input("enter guess"))
    if guess<win:
        if guess<win and c==5:
            print("GAME OVER")
            break
        print(f"go forward and remaining chances are {5-c}")
    elif guess>win:
        print(f"go back and remaining chances are {5-c}")
        if guess>win and c==5:
            print("GAME OVER")
    elif guess==win:
        print(f"you win with {5-c} chances remaining")
    c = c + 1

#another mthd
#my first game
number = 83
current = 0
while (1):
    current=current+1
    if current == 6:
        print("sorry you lost the game")
        break
    elif current<=5:
        guess = int(input("enter the guess\n"))
        if guess==number:
            print("congratulations you won the game with ",5-current, "chances left")
            break
        elif guess<number:
            print("please go forward and chances remaining are ",5-current)
        elif guess >number:
            print("please go backward and chances remaining are ",5-current)



