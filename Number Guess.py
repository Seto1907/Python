import random
file = open("C:/Users/Seto/Desktop/numbers.txt","a")
print('''Note:
You have 5 healths. If your healths end, you lose. So be careful.''')
while True:
    try:
        lowerRange = int(input("Enter lower range:"))
        upperRange = int(input("Enter upper range:"))
        health = 5
        number = random.randint(lowerRange,upperRange)
        file.write('{}\n'.format(number))
    except:
        print("The values you entered have to be integers!")
    else:
        break
while True:
    guess = int(input("Guess:"))
    if guess == number:
        print('''Right Guess. Congratulations...
        Choose process:
        1- New Game.
        2- Finish.''')
        choose = int(input("Choose:"))
        if choose==1:
            number = random.randint(lowerRange,upperRange)
            file.write('{}\n'.format(number))
            health = 5
        elif choose==2:
            print("Process is terminated.")
            break
        else:
            print('''Wrong process!
Process is terminated.''')
            break
    elif guess!=number:
        print("Wrong guess. Try again.")
        health-=1
        if health == 0:
            again= int(input(('''Your healths finished, you lost.
The number I choose: {}
Would you like to play again?
1-Yes
2-No:'''.format(number))))
            if again == 2:
                print("Process is terminated...")
                break
            else:
                health = 5
                number = random.randint(lowerRange, upperRange)
file.close()
