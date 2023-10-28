Python script that allows a user to input daily screen time data, store it in a dictionary, and then write this data to a file. Here's a small description of the code:

1) The script starts by importing the datetime and timedelta classes from the datetime module.
2) It prompts the user to input a filename, starting date, and the number of days for which they want to record screen time.
3) The script initializes an empty dictionary called dic to store the screen time data for each day and a variable total_time to keep track of the total screen time.
4) It enters a loop that iterates over the specified number of days. For each day:
  - It calculates the end date based on the starting date and the current day's offset.
  - It Prompts the user to input screen time data for that day (presumably for TV, computer, and mobile usage) and stores it in a list.
  - It updates the total_time with the sum of the screen time values for that day.
  - Stores the screen time data for that day in the dic dictionary with the date as the key.
5) It opens the specified file in write mode and clears its contents. Then, it opens the same file in append mode.
6) The script writes a header to the file, including the time period, the total minutes of screen time, and the average minutes per day.
7) It iterates through the dic dictionary and writes each date and its corresponding screen time data to the file.
8) The code concludes with a comment that provides an example of how to use the script and what data is stored in the "late_june.txt" file.

In summary, this code is a basic screen time tracker that takes user input for multiple days, calculates the total and average screen time, and stores the data in a file for future reference.
