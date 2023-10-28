from random import *
from string import ascii_lowercase

def generate_strong_password(n:int, num_true:int, special_char:str):
    letters = ascii_lowercase  # All lowercase letters
    nums = [str(i) for i in range(10)]  # All numbers
    s_char = "!?=+-()#"  # special characters
    password = []  
    if special_char:
        password += sample(s_char, 2)
    if num_true:
        password += sample(nums, 2)
    l = n - len(password)   #checking the len after adding numbers and special if no number or special char are added then len will be same as provided
    password += sample(letters, l)  # Adding remaining letters 
    shuffle(password)
    # print("".join(password))   # Converting list into string
    return "".join(password)


if __name__ =="__main__":
    while True:
        length = int(input("Enter how long you want your Password: "))
        num = input("Enter Y or y if you want number in your Password else N: ").lower() 
        special = input("Enter Y or y if you want some Special Character else N: ").lower()
        if num == 'y' and special == "y":
            num = special = True
        elif num == "y" and special != 'y':
            num = True
            special = False
        elif num != 'y' and special == "y":
            num = False
            special = True
        else:
            num = False
            special = False
        print(generate_strong_password(length, num, special))
        quit = input("Enter q to Exit or any other key to continue: ")
        if quit:
            break
        
