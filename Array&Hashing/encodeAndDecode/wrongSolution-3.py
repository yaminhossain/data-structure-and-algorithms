#This solution is wrong because special characters like # and * can be part of the string

def encode(strArr):
  return "#".join(strArr)

def decode(str):
  if(str == ""):
    return ""
  res = [""]
  tempString=""
  lenString = len(str)
  for i in range(lenString):
    if(str[i] == "#" or i== lenString-1):
      res.append(tempString)
      tempString = ""
    else:
      tempString += str[i]
    
  res[len(res)-1] += str[lenString-1]
  return res

joinedString = encode(["Hello", "World"])
print("Joined String", joinedString)
decodedArray = decode(joinedString)
print(decodedArray)