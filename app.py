
print("Welcome to my Python program!")
points = input("How many points did you earn today? ")
try:
    points = float(points)
except ValueError:
    print("Please enter a valid number.")
    exit()  # stops the program if input is invalid


weekly_points = points * 7
print(f"You have gotten {weekly_points} points this week.")
