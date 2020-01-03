def is_k_periodic(a, b):
    return b == (a[-1] + a[:-1])


if __name__ == "__main__":
    str = input()
    k_min = len(str)
    for k in range(len(str)-1, 0, -1):
        if len(str) % k == 0:
            l = [str[i:i+k] for i in range(0, len(str), k)]
            if all(is_k_periodic(a, b) for (a, b) in zip(l, l[1:])):
                k_min = k
    print(k_min)
