
if __name__ == "__main__":
    n = int(input())
    xs = sorted([float(input().split()[1]) for _ in range(n)], reverse=True)
    ans = 0
    for (i, p) in zip(range(n), xs):
        ans += (i+1)*p
    print(ans)
