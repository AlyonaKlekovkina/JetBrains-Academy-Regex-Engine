import sys
sys.setrecursionlimit(10000)

reg, string = input().split("|")


def compare(regex, i, string, j):

    if i == len(regex):
        return True
    if j == len(string):
        return False

    if regex[i] == string[j] or (regex[i] == ".") or (regex[i] == ""):
        return compare(regex, i + 1, string, j + 1)
    else:
        return compare(regex, i, string, j + 1)


print(compare(reg, 0, string, 0))
