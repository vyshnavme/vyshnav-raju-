low=1
high=1000
print("Please, Think of a number btw {} and {} ".format(low,high))
input("Please, Press Enter to Start")
guesses=1
while True:
    print("The number is Between {} and {}".format(low,high))
    guess=low+(high-low)//2
    high_low=input("My guess is {}. Should i guess Higher or lower? Enter h,l or c if my guess is correct ".format(guess).casefold())
    if high_low == "h":
        low=guess+1
    elif high_low == "l":
        high=guess-1
    elif high_low == "c":
        print("You have got it in {} guesses".format(guesses))
        break
    else:
        print("Please, enter h,l or c")
    guesses=guesses+1
