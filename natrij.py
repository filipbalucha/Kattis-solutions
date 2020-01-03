if __name__ == "__main__":
    (h1, m1, s1) = tuple(map(int, input().split(':')))
    (h2, m2, s2) = tuple(map(int, input().split(':')))
    s = (h2-h1) * 3600 + (m2-m1) * 60 + (s2-s1)  # get difference in seconds
    s %= 24*3600
    h = int(s / 3600)
    s %= 3600
    m = int(s / 60)
    s = int(s % 60)
    if h == 0 and m == 0 and s == 0:
        print("24:00:00")
    else:
        print(f"{h:02}:{m:02}:{s:02}")
