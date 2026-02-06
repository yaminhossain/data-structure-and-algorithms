def nums(s):
  res=[]
  i=0
  while(s[i] !="#"):
    cur = ""
    while(s[i] !=","):
      cur += s[i]
      i +=1
    res.append(int(cur))
    cur=""
    i+=1
  return res
res = nums("11,1,#")
print(res)