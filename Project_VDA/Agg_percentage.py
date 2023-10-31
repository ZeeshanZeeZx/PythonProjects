import pyttsx3

engine = pyttsx3.init()  # Assign varible to module
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)


def cgpa():
    engine.say("Welcome to Aggrigate percentage calculator")
    engine.runAndWait()
    engine.say("Please enter your name")
    engine.runAndWait()
    name = input("Enter your name: ")
    engine.say(f"{name} please enter s g p a and total credits of each sem")
    engine.runAndWait()
    # spk("Welcome to Engineering Percentage calculator")
    lst_SGPA = [
        "sem1_SGPA", "sem2_SGPA", "sem3_SGPA", "sem4_SGPA", "sem5_SGPA",
        "sem6_SGPA", "sem7_SGPA", "sem8_SGPA"
    ]
    lst_TC = [
        "sem1_TC", "sem2_TC", "sem3_TC", "sem4_TC", "sem5_TC", "sem6_TC",
        "sem7_TC", "sem8_TC"
    ]
    SGPA_TC_mul = 0
    TC_add = 0
    for i in range(0, 8):
        try:
            lst_SGPA[i] = float(
                input(f"Enter {i + 1} sem SGPA or '0' Don't have: "))
        except:
            continue
            # print("Error input")
        if lst_SGPA[i] == 0:
            continue
        lst_TC[i] = int(input(f"Enter {i + 1} sem Total Credits: "))
        SGPA_TC_mul += lst_SGPA[i] * lst_TC[i]
        TC_add += lst_TC[i]
    CGPA = SGPA_TC_mul / TC_add
    print(f"{name} your Percentage is: {(CGPA - 0.75) * 10}")
    per = (CGPA - 0.75) * 10
    per = str(per)
    # engine.say(f"{name} your aggregate Percentage is: {round(per, 2)}")
    engine.say(f"{name} your aggregate Percentage is: {per[:6]}")
    engine.runAndWait()

# ℤ𝕏
