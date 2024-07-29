def wordLower(string):
    newWord = ""
    for x in string:
        if 65 <= ord(x) <= 97:
            newWord += (chr(ord(x) + 32))
        else:
            newWord += x

    return newWord


print(wordLower("MuYeED"))
