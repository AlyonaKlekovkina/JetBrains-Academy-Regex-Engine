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

    return compare_forward(regex[1:], string[1:])


def compare_backward(regex, i, string, j):
    r = (len(regex) * -1) - 1
    if i == r:
        return True
    if regex[i] == string[j] or (regex[i] == ".") or (regex[i] == ""):
        return compare_backward(regex, i - 1, string, j - 1)
    else:
        return False


def question_sign(regex, string):
    beg, end = regex.split('?')
    if (len(regex) - 1) == len(string):
        the_reg = beg + end
    else:
        the_reg = beg[:-1] + end
    return the_reg


def asterisk_sign(regex, string):
    beg, end = regex.split('*')
    if (len(regex) - 1) == len(string):
        the_reg = beg + end
    elif (len(regex) - 1) < len(string):
        repeated = beg[-1]
        times = abs(len(string) - (len(regex) - 1))
        the_reg = beg + (repeated * times) + end
    elif (len(regex) - 1) > len(string):
        i = abs(len(string) - (len(regex) - 1))
        the_reg = beg[:-i] + end
    return the_reg


def plus_sign(regex, string):
    beg, end = regex.split('+')
    if '+' in inp_reg and '^' in inp_reg and '$' in inp_reg:
        times = abs(len(string) - (len(regex) - 3))
        repeated = beg[-1]
        the_reg = beg + (repeated * times) + end
    elif (len(regex) - 1) < len(string):
        repeated = beg[-1]
        times = abs(len(string) - (len(regex) - 1))
        the_reg = beg + (repeated * times) + end
    else:
        the_reg = beg + end
    return the_reg


inp_reg, inp_string = input().split("|")
if inp_reg == "":
    print(True)
elif '+' in inp_reg and '^' in inp_reg and '$' in inp_reg:
    the_regex = plus_sign(inp_reg, inp_string)
    chopped = the_regex[1:-1]
    print(compare_backward(chopped, -1, inp_string, -1))
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
elif "?" in inp_reg:
    the_regex = question_sign(inp_reg, inp_string)
    print(compare_backward(the_regex, -1, inp_string, -1))
elif "*" in inp_reg:
    the_regex = asterisk_sign(inp_reg, inp_string)
    print(compare_backward(the_regex, -1, inp_string, -1))
elif "+" in inp_reg:
    the_regex = plus_sign(inp_reg, inp_string)
    print(compare_backward(the_regex, -1, inp_string, -1))
else:
    print(compare(inp_reg, 0, inp_string, 0))
