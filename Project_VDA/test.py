# lst1 = ["this", "is", "good", 45, "is", "a"]
# # tup = ("this", "is", "tuple", 45)
# # string = " ".join(str(word) for word in tup)
# # print(string)
# # set_list = set(lst1)
# # print(set_list)
# print(lst1.count("is"))

import datetime
def wishme():
    print("Welcome back")
    hour = datetime.datetime.now().hour
    print(hour)
    if hour <= 12:
        print("Good Morning master")
    elif hour <= 17:
        print("Good afternoon master")
    elif hour > 17:
        print("Good evening master")
    # spk(f"This is {ai_name} at your service. How may i help u master....")
    # print(f"This is {ai_name} at your service. How may i help u master....")

wishme()