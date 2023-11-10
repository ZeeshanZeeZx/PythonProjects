# Below are the module which are needed 
from datetime import datetime, timedelta

filename = input("Filename: ") # example--> 'late_june.txt'
Starting_date = datetime.strptime(input("Starting_date: "), "%d.%m.%Y") # ex --> 24.6.2020
days = int(input("How many days: "))
screen_time = print("Please type in screen time in minutes on each day (TV computer mobile): ")
dic = {}
total_time = 0

for i in range(days):
    EndDate = Starting_date + timedelta(days=i)
    print_date = EndDate.strftime("%d.%m.%Y")
    # print(f"Screen time {EndDate.date()}:")
    inp = list(map(str, input(f"Screen time {print_date}:").split())) # enter how many minutes you spend on your screen in an day 60   
    for i in inp:
        total_time += int(i)
    dic[print_date] = '/'.join(inp)

open(filename, "w").close() #if file is already present then emptying it
with open(filename, "a") as file_handle:
    Starting_date = Starting_date.strftime("%d.%m.%Y")
    file_handle.write(f"Time period: {Starting_date}-{print_date}\n")
    file_handle.write(f"Total minutes: {total_time}\n")
    file_handle.write(f"Average minutes: {total_time/days}\n")
    for i in dic:
        file_handle.write(f"{i}: {dic[i]}\n")

# at the end of the program you  will get a file that contain the whole info like
"""
Input:
Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
Please type in screen time in minutes on each day (TV computer mobile):
Screen time 24.06.2020: 60 120 0
Screen time 25.06.2020: 0 0 0
Screen time 26.06.2020: 180 0 0
Screen time 27.06.2020: 25 240 15
Screen time 28.06.2020: 45 90 5
Data stored in file late_june.txt

Output:
Time period: 24.06.2020-28.06.2020
Total minutes: 780
Average minutes: 156.0
24.06.2020: 60/120/0
25.06.2020: 0/0/0
26.06.2020: 180/0/0
27.06.2020: 25/240/15
28.06.2020: 45/90/5
"""

# ℤ𝕏
   

