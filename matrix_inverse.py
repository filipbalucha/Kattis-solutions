import sys

if __name__ == "__main__":
    case = 1
    while(True):
        try:
            (a, b) = tuple(map(int, input().split()))
            (c, d) = tuple(map(int, input().split()))
            det = a*d-b*c
            print("Case {}:".format(case))
            print("{} {}".format(int(d/det), int(-b/det)))
            print("{} {}".format(int(-c/det), int(a/det)))
            input()
            case += 1
        except EOFError:
            break
