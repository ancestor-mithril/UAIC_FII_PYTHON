"""
6. Write a script that writes the day of the week for the New Year Day, for the last x years (x is given as argument).

"""
import datetime
import sys
import calendar


def run():
    if len(sys.argv) < 2:
        print("Run the project as following:")
        print("python.exe ex_6.py x")
        print("where x is an integer")
        exit()
    try:
        years = int(sys.argv[1])
    except ValueError:
        print("x is not integer")
        exit()
    current_year = int(datetime.date.today().year)
    new_years = []
    for i in range(years):
        new_years.append((current_year - i, calendar.day_name[datetime.datetime(current_year - i, 1, 1).weekday()]))
    print(new_years)


if __name__ == "__main__":
    run()
