def validAnagram(s,t):
    if(len(s) != len(t)):
        return False
    dictS={}
    dictT={}
    for i in s:
        if i in dictS:
            dictS[i] +=1
        else:
            dictS[i] = 1
    
    for j in t:
        if j in dictT:
            dictT[j] +=1
        else:
            dictT[j] = 1
    print(dictT)
    print(dictS)
    return dictS == dictT

s = "anagtam"
t = "nbgbram"
res=validAnagram(s,t)
print(res)