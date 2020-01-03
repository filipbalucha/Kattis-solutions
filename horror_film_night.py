if __name__ == "__main__":
    NUM_OF_FILMS = 10 ** 6
    xs = [False] * NUM_OF_FILMS
    ys = [False] * NUM_OF_FILMS
    count = 0
    last = 0  # can be either = both liked the previous film or this is the first film
    for i in list(map(int, input().split()[1:])):
        xs[i] = True
    for i in list(map(int, input().split()[1:])):
        ys[i] = True
    for i in range(NUM_OF_FILMS):
        if xs[i] and ys[i]:
            count += 1
            last = 0
        elif xs[i] and not last == 1:
            count += 1
            last = 1
        elif ys[i] and not last == 2:
            count += 1
            last = 2
    print(count)
