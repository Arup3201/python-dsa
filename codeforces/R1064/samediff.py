def same_diference(n: int, s: str) -> int:
    n = len(s)
    cnt = 0
    lst = s[-1]
    for ch in s[:-1]:
        if ch!=lst:
            cnt+=1

    return cnt

if __name__=="__main__":
    t = int(input())
    while t>0:
        n = int(input())
        s = input()
        out = same_diference(n, s)
        print(out)
        t-=1