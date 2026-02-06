# It works perfectly because the encoded message sent like this: "11,1,#"

def encoding(strArray):
  if (not strArray):
    return ""
  
  res = ""
  strLengths = []
  for s in strArray:
    strLengths.append(len(s))
  
  for length in strLengths:
    res = res+str(length)+","
  res = res +"#"

  for s in strArray:
    res += s
  print(res)
  return res

def decoding(string):
  if(not string):
    return []
  res =[]
  i = 0
  while(string[i] != "#"):
    i+=1
  subString = string[0 : i-1]
  lengths = subString.split(",")
  
  start = i+1
  end = i+1
  for j in lengths:
    n= int(j)
    end += n
    if(n == 0):
      res.append("")
    else: 
      res.append(string[start: end])
    start = end
  return res

strArray =["#"]
encodedString = encoding(strArray)

result = decoding(encodedString)
print(result)