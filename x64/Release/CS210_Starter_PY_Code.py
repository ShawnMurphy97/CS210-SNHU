import re
import string


def itemCount():
    itemFreq = {
        }
    itemFile = open(r"C:\Users\Harophin\source\repos\CornerGrocerApplication\x64\Release\shopping_list.txt")
    grocerList = itemFile.read() ##reads input file into string
    itemList = grocerList.split("\n") ##splits each item and enters it into list of itemList
    for i in range(len(itemList)): ##Iterates through list and adds unique entries into dictionary
        if itemList[i] not in itemFreq:
            itemFreq[itemList[i]] = 1
        elif itemList[i] in itemFreq: ##If item is already in list it increments the value of that entry to show duplicates
            itemFreq[itemList[i]] += 1
    for key, value in itemFreq.items():
        print (key, ' ', value)
    itemFile.close()

def PurchaseAmount(item):
    itemFreq = {
        } ##declares dictionary
    itemFile = open(r"C:\Users\Harophin\source\repos\CornerGrocerApplication\x64\Release\shopping_list.txt")
    grocerList = itemFile.read() ##reads input file into string
    itemList = grocerList.split("\n") ##splits each item and enters it into list of itemList
    for i in range(len(itemList)): ##Iterates through list and adds unique entries into dictionary
        if itemList[i] not in itemFreq:
            itemFreq[itemList[i]] = 1
        elif itemList[i] in itemFreq: ##If item is already in list it increments the value of that entry to show duplicates
            itemFreq[itemList[i]] += 1
    itemFile.close()
    freq = itemFreq[item]
    return freq

def SalesTable():
    histoBar = ""
    itemFreq = {
        } ##declares dictionary
    itemFile = open(r"C:\Users\Harophin\source\repos\CornerGrocerApplication\x64\Release\shopping_list.txt")
    grocerList = itemFile.read() ##reads input file into string
    itemList = grocerList.split("\n") ##splits each item and enters it into list of itemList
    for i in range(len(itemList)): ##Iterates through list and adds unique entries into dictionary
        if itemList[i] not in itemFreq:
            itemFreq[itemList[i]] = 1
        elif itemList[i] in itemFreq: ##If item is already in list it increments the value of that entry to show duplicates
            itemFreq[itemList[i]] += 1
    itemFile.close()
    f = open("GrocerHistorgram.txt", "w")
    for key, value in itemFreq.items():
        f.write('%s %s\n' % (key, value)) ##writes line between two histograms
    f.write("\n")
    for key, value in itemFreq.items():
        i = 0
        while i < itemFreq[key]:
            histoBar += "*" ##creates the * for histogram
            i += 1
        output = "%s %s\n" % (key, histoBar)
        f.write(output) ##writes out histogram to file
        histoBar = "" ##resets value of the histogram bar variable
