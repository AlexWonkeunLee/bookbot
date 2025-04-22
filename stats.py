def wordCount(words):
    total = words.split()
    return len(total)

def characterCount(words):
    counterList = {}
    for character in words:
        if(character.lower() in counterList):
            counterList[character.lower()] += 1
        else:
            counterList[character.lower()] = 1
    
    return counterList

def sort_on(dict):
    return dict['count']

def sortedList(dictionary):
    doubleDict = []
    for entry in dictionary:
        dictEntry = {}
        if (entry.isalpha()):
            dictEntry["alpha"] = entry
            dictEntry["count"] = dictionary[entry]
            doubleDict.append(dictEntry)
    doubleDict.sort(reverse=True, key=sort_on)
    return doubleDict

