from tkinter import *
import random
import string
import pyperclip
import pyttsx3

engine = pyttsx3.init()  # Assign varible to module
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)


def runme():
    engine.say("Welcome To Random Password Generator")
    engine.runAndWait()
    # Initialize window
    root = Tk()
    root.geometry("450x250")
    root.resizable(0, 0)
    root.title("EDU - PASSWORD GENERATOR")

    # Heading
    heading = Label(root,
                    text=' RANDOM PASSWORD GENERATOR',
                    font='arial 17 bold').pack()
    Label(root, text='--SAA--', font="arial 12 bold").pack(side=BOTTOM)

    # Select password length
    pass_label = Label(root, text='Password Length', font='arial 15').pack()
    pass_len = IntVar()
    length = Spinbox(root,
                     from_=8,
                     to_=20,
                     textvariable=pass_len,
                     width=10,
                     font='arial 9').pack()

    # Define function
    pass_str = StringVar()

    def Generator():
        password = ''
        for x in range(0, 4):
            password = random.choice(string.ascii_uppercase) + random.choice(
                string.ascii_lowercase) + random.choice(
                    string.digits) + random.choice(string.punctuation)
        for y in range(pass_len.get() - 4):
            password = password + random.choice(string.ascii_uppercase +
                                                string.ascii_lowercase +
                                                string.digits +
                                                string.punctuation)
        engine.say("Your encoded password is shown in screen")
        engine.runAndWait()
        pass_str.set(password)

    # Button for generating password
    Button(root, text="GENERATE PASSWORD", command=Generator,
           font='arial 10').pack(pady=5)
    Entry(root, textvariable=pass_str, width=20, font='arial 9').pack()

    # Function to copy
    def Copy_password():
        pyperclip.copy(pass_str.get())
        engine.say("Your encoded password is Copied")
        engine.runAndWait()

    # Button for copying password
    Button(root,
           text='COPY TO CLIPBOARD',
           command=Copy_password,
           font='arial 10').pack(pady=5)

    # Loop to run program
    root.mainloop()
