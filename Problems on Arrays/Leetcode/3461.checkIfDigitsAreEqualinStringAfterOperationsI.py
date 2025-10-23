
def getDigits(givenStr):
    temp = ""
    while(len(givenStr)>2):
        temp=""
        for i in range(len(givenStr) - 1):
            s = (int(givenStr[i]) + int(givenStr[i + 1])) % 10
            temp += str(s)
        givenStr = temp
    if(givenStr[0] == givenStr[1]):
        return True
    return False


s = "34789"
res = getDigits(s)
print("Result :",res)