if __name__ == "__main__":
    n = int(input())
    steps = input()
    ans = list(range(1, n+1))
    i = 0
    while (i < len(steps)):
        if steps[i] == 'L':
            j = i
            while(j < len(steps) and steps[j] == 'L'):
                j += 1
            ans[i:j+1] = reversed(ans[i:j+1])
            i = j
        else:
            i += 1
    print(*ans, sep='\n')
