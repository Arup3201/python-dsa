d = 17
    
def nextHash(hin: int, new: str, prev: str, m: int):
    hout = d*(hin - ord(prev) * d**(m-1)) + ord(new)
    return hout

def search(pat, txt):
    result = []
    
    pLen = len(pat)
    tLen = len(txt)
    
    d = 17
    q = 10**6 + 7
    h = 1
    for _ in range(pLen-1):
        h = (h*d) % q
    
    p = 0
    t = 0
    for i in range(pLen):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    i = 0
    while i<=tLen-pLen:
        if t==p:
            if txt[i:i+pLen]==pat:
                result.append(i)
        
        if i < tLen-pLen:
            t = (d*(t - ord(txt[i])*h) + ord(txt[i+pLen])) % q
            if t < 0:
                t = t+q
        
        i+=1
        
    return result