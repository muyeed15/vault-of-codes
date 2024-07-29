def wordUpper(string):
    newWord = ""
    for x in string:
        if 97 <= ord(x) <= 122:
            newWord += (chr(ord(x) - 32))
        else:
            newWord += x

    return newWord


print(wordUpper("MuYeED"))
