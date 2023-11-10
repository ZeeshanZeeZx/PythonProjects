import string


def change_case(orig_string: str):  # upper -> Lower :: Lower -> Upper
    word = ""
    for i in orig_string:
        if i in string.ascii_lowercase:
            word += i.upper()
        elif i in string.ascii_uppercase:
            word += i.lower()
        else:
            word += i
    return word


# splits the parameter string in half, and returns the results in a tuple (word1, word2)
def split_in_half(orig_string: str):
    length = len(orig_string)
    half = int(length/2)
    return (orig_string[:half], orig_string[half:])


# Only lowercase and uppercase letters, numbers and spaces are allowed in the returned string
def remove_special_characters(orig_string: str):
    word = ""
    for i in orig_string:
        if i.isalnum() or i == " ":
            word += i
    return word


if __name__ == "__main__":
    # my_string = "Well hello there!"
    my_string = input("Enter sentence to revese case: ")
    print("================================")
    print(change_case(my_string))
    inp = input(
        "Enter Y or y to Split the sentence in half and remove special characters: ")
    if inp.lower() == 'y':
        p1, p2 = split_in_half(my_string)
        print("================================")
        print(f"word: {my_string}")
        print(f"Part 1: {p1}")
        print(f"Part 2: {p2}")
        print("================================")
        m2 = remove_special_characters(my_string)
        print("Without any Special characters: ")
        print(m2)

# ℤ𝕏
