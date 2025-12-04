def getLPS(s):
    n = len(s)
    lps = [0]*n
    
    l = 0
    for i in range(1, n):
        if s[i]==s[l]:
            l+=1
            lps[i] = l
        else:
            while l>0 and s[i]!=s[l]:
                l = lps[l-1]
                
            if s[i]==s[l]:
                l+=1
                lps[i] = l
                
    return lps

def search(pat, txt):
    pl = len(pat)
    tl = len(txt)
    
    lps = getLPS(pat)
    
    i = 0
    j = 0
    result = []
    while i<tl:
        if txt[i]==pat[j]:
            i+=1
            j+=1
        
        if j==pl:
            result.append(i-pl)
            j = lps[j-1]
        elif i<tl and txt[i]!=pat[j]:
            if j==0:
                i+=1
            else:
                j = lps[j-1]
                
    return result