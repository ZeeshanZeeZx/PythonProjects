from string import ascii_letters


def run(my_lst: list):
    lst = []
    locations = []
    for index, i in enumerate(my_lst):
        i = i.split(" ")
        if i[0].lower() == "mov":
            dict[i[1]] = int(i[2])
        elif i[0].lower() == 'print':
            # print(dict[i[1]])
            lst.append(dict[i[1]])
        elif i[0].lower() == "add":
            if i[2] in ascii_letters:
                sum = dict[i[1]] + dict[i[2]]
                dict[i[1]] = sum
            else:
                dict[i[1]] += int(i[2])
            lst.append(dict[i[1]])
        elif i[0].lower() == "sub":
            if i[2] in ascii_letters:
                sub = dict[i[1]] - dict[i[2]]
                dict[i[1]] = sub
            else:
                dict[i[1]] -= int(i[2])
            lst.append(dict[i[1]])
        elif i[0].lower() == "mul":
            if i[2] in ascii_letters:
                mul = dict[i[1]] * dict[i[2]]
                dict[i[1]] = mul
            else:
                dict[i[1]] *= int(i[2])
            lst.append(dict[i[1]])
        elif i[0].lower() == "div":
            if i[2] in ascii_letters:
                div = dict[i[1]] / dict[i[2]]
                dict[i[1]] = div
            else:
                dict[i[1]] /= int(i[2])
            lst.append(dict[i[1]])

        elif i[0].lower() == 'end':
            return lst


if __name__ == "__main__":
    dict = {}
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("MUL A B")
    program1.append("PRINT A")
    program1.append("DIV A 1")
    program1.append("PRINT A")
    program1.append("SUB A 1")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
