print("Program asks for strings and finds the longest string.")
numberOfString = int(input("How many strings are prompted: "))
shortestStringLen = int(input("Shortest string (in characters) allowed: "))

len = 0
longestString = ""
for i in range(numberOfString):
    string = input("Give a word: ")
    currentStringLen = 0
    for c in string: 
        currentStringLen += 1 
        
    if currentStringLen < shortestStringLen:
        print("Program ends, because the inserted string was too short.")
        print("You gave "+ str(i+1) +" strings.")
        break
    else:
        if currentStringLen > len:
            len = currentStringLen
            longestString = string
        if i == numberOfString - 1:
            print("Program ends because all the strings were prompted.") 
            print("You gave "+ str(i+1) +" strings.")
            break

print("Longest string was \'"+ longestString +"\', which had "+ str(len) +" characters.")    
print("Thank you for using the program.")
