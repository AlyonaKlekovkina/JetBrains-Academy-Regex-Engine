# write your code here
user_input = input()
reg, string = user_input.split("|")


def compare(reg, string):
    if reg == '':
        return True
    elif len(reg) != len(string):
        return False
    elif (reg[0] == string[0]) or (reg[0] == ".") or (reg[0] == ""):
        return True
    elif (reg[0] != string[0]) or (reg[0] != ".") or (reg[0] != ""):
        return False

    return compare(reg[1:], string[1:])


print(compare(reg, string))
