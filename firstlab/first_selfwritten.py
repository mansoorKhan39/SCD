print("Cricket Score Calculator")

runs = int(input("Enter runs: "))
balls = int(input("Enter balls: "))

strike_rate = runs / balls * 100

print("Runs:", runs)
print("Balls:", balls)
print("Strike Rate:", strike_rate)

if strike_rate > 100:
    print("Good batting!")
else:
    print("You need to improve.")