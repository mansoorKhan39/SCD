print("Cricket Score Calculator")

try:
    runs = int(input("Enter runs: "))
    balls = int(input("Enter balls: "))

    if runs < 0 or balls < 0:
        print("Runs and balls cannot be negative.")

    elif balls == 0:
        print("Balls cannot be zero.")

    else:
        strike_rate = (runs / balls) * 100

        print("Runs:", runs)
        print("Balls:", balls)
        print("Strike Rate:", round(strike_rate, 2))

        if strike_rate > 100:
            print("Good batting!")
        else:
            print("You need to improve.")

except ValueError:
    print("Please enter numbers only.")