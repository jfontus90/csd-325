import csv
from datetime import datetime
import matplotlib

from matplotlib import pyplot as plt

print("\nWelcome to Sitka Highs Program!!!\nHere's How To Use it:")
print("\nSelect a Number for the Option you Want:\n1. Highs\n2. Lows\n3.Exit\n")

user_choice = input("Enter your choice here: ")

while (user_choice == "1" or user_choice == "2"):
    if user_choice == "1":
        print("\nYou have chosen to print the Highs!")
        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and high temperatures from this file.
            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)

        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

        user_choice = input("\n type here: ")
        if (user_choice == 3):
            break
    elif user_choice == "2":
        print("\nYou have chose to print the Lows!")
        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and low temperatures from this file.
            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)

        # Plot the low temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

        user_choice = input("\ntype here: ")
        if (user_choice == "3"):
            break
else:
    print("\nExit: You have chosen to exit the program.")