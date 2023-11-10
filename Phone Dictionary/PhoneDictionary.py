def command(inp, p_dict):
    if inp == 2:
        name = input("name: ")
        if name in p_dict.keys():
            p_dict[name] += "\n"+ input("number:")
        else:
            p_dict[name] = input("number:")
        print("ok!")
    elif inp == 1:
        name = input("name: ")
        if name in p_dict.keys():
            print(p_dict[name])
        else:
            print("no number")
        
inp = int(input("command (1 search, 2 add, 3 quit): "))
p_dict = {}
while inp != 3:
    command(inp, p_dict)
    inp = int(input("command (1 search, 2 add, 3 quit): "))
print("quitting...")

# ℤ𝕏
