import pyttsx3
import phonenumbers

engine = pyttsx3.init()  # Assign varible to module
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)


def track():
    engine.say("Please enter your number..")
    engine.runAndWait()
    num = input("Enter your number: ")
    number = "+91" + num

    # getting location
    from phonenumbers import geocoder
    location = phonenumbers.parse(number,
                                  "CH")  #To get country C-country H-histroy
    print(f"Country:{geocoder.description_for_number(location, 'en')}")

    # getting service provider
    from phonenumbers import carrier
    service_provider = phonenumbers.parse(number)
    engine.say(f"Country is {geocoder.description_for_number(location, 'en')}")
    engine.runAndWait()
    print(f"Network: {carrier.name_for_number(service_provider, 'en')}")

    from phonenumbers import timezone
    gb_number = phonenumbers.parse(number, "GB")
    time_zone = timezone.time_zones_for_number(gb_number)
    engine.say(
        f"Network provider {carrier.name_for_number(service_provider, 'en')}")
    engine.runAndWait()
    print(f"Timezone: {time_zone}")

    engine.say(f"and the Timezone is {time_zone}")
    engine.runAndWait()


# ℤ𝕏