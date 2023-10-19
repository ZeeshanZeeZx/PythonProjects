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
    for i in range(10):
        # print(generate_strong_password(8, True, True))
        print(generate_strong_password(5, True, False))
        # print(generate_strong_password(5, False, True))
        # generate_strong_password(8, True, True)
        # password should also contain one or more numbers
        # password should also contain one or more of these special characters: "!?=+-()#"
