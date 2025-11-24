#Welcome
print("Welcome to my Python program!")
#input taken
points = input("How many points did you earn today? ")
#input to number if wrong
try:
    points = float(points)
except ValueError:
    print("Please enter a valid number.")#inform user
    exit()  # stop program if wrong

#calualte weekly
weekly_points = points * 7
#display
print(f"You have gotten {weekly_points} points this week.")
