print("Program starting.")
fileName = str(input("Give filename: "))
f = open(fileName, mode='r', encoding='utf-8')
# row = f.readlines
row = 0
len = 0
for line in f:
    if line != "\n":
        row += 1
        for c in line:
            if c != "\n":
                len += 1
print('There was ' + str(row) + ' names in the file.')
print('There was ' + str(len) + ' characters in the names.')
print('Average name length was ' + str(round(len/row,1)) + '.')
print('Thank you for using the program.')
