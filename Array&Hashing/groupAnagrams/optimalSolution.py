from collections import defaultdict

def groupAnagram(strs):
    hashMap= defaultdict(list)
    res=[]
    n = len(strs)
    for i in range(n):
        sortedS = "".join(sorted(strs[i]))
        hashMap[sortedS].append(strs[i])
    for key in hashMap:
        res.append(hashMap[key])
    return res


strs = ["eat","tea","tan","ate","nat","bat"]
res=groupAnagram(strs)
print(res)