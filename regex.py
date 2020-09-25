import sys
sys.setrecursionlimit(10000)


def compare(regex, i, string, j):
    if i == len(regex):
        return True
    if j == len(string):
        return False

    if regex[i] == string[j] or (regex[i] == ".") or (regex[i] == ""):
        return compare(regex, i + 1, string, j + 1)
    else:
        return compare(regex, i, string, j + 1)


def compare_forward(regex, string):
    if regex == '':
        return True
    elif (regex[0] == string[0]) or (regex[0] == ".") or (regex[0] == ""):
        return True
    elif (regex[0] != string[0]) or (regex[0] != ".") or (regex[0] != ""):
        return False

    return compare(regex[1:], string[1:])


def compare_backward(regex, i, string, j):
    r = (len(regex) * -1) - 1
    if i == r:
        return True
    if regex[i] == string[j] or (regex[i] == ".") or (regex[i] == ""):
        return compare_backward(regex, i - 1, string, j - 1)
    else:
        return False


inp_reg, inp_string = input().split("|")
if inp_reg == "":
    print(True)
elif inp_reg[-1] == "$" and inp_reg[0] == '^':
    the_regex = inp_reg[1:-1]
    if (compare_backward(the_regex, -1, inp_string, -1) is True) and (compare_forward(the_regex, inp_string) is True):
        print(True)
    else:
        print(False)
elif inp_reg[0] == "^":
    the_regex = inp_reg[1:]
    print(compare_forward(the_regex, inp_string))
elif inp_reg[-1] == "$":
    the_regex = inp_reg
    print(compare_backward(the_regex, -2, inp_string, -1))
else:
    print(compare(inp_reg, 0, inp_string, 0))
