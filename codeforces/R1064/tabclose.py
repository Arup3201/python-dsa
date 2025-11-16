def tab_closing(a: int, b: int, n: int) -> int:
    cnt = 0
    m = n
    
    if m*b>a:
        cnt += 1
    
    while m>0 and m*b>a:
        m-=1

    if m!=0 and m*b<=a:
        cnt += 1
    
    return cnt


if __name__=="__main__":
    t = int(input())
    while t>0:
        a, b, n = list(map(int, input().split()))
        out = tab_closing(a, b, n)
        print(out)
        t-=1