def beverage_counter(n):
    if n == 0:
        return "no more bottles"
    if n == 1:
        return "1 bottle"
    return str(n) + " bottles"


def get_line(n, word):
    return "{} of {} on the wall, {} of {}.\nTake {} down, pass it around, {} of {}{}.".format(beverage_counter(n+1), word, beverage_counter(n+1), word, 'it' if n == 0 else 'one', beverage_counter(n), word, '' if n == 0 else ' on the wall')


if __name__ == "__main__":
    n = int(input())
    word = input()
    lines = [get_line(i, word) for i in reversed(range(n))]
    print('\n\n'.join(lines))
