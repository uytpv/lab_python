def displayItems(itemList):
    print('Current items: ', end='\n')
    for item in itemList:
        print(' - ' + str(item))
    print()
    return None


def insertItem(number, itemList):
    itemList.append(number)
    return None


itemList = [1000, 500, 100]
print('Handling "Items" list:')
displayItems(itemList)
number = float(input('Give a number: '))
insertItem(number, itemList)
displayItems(itemList)
itemList.sort()
displayItems(itemList)
print('Thank you for using the program.')
