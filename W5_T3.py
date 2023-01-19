exitCoin = int(input("Insert 3 - 7 coins (0 stops): "))
totalCoin = 0
while exitCoin != 0:
    if exitCoin < 3 or exitCoin >7:
        print("Failed to insert coins. Try to insert 3 - 7 coins at a time (0 ends).")
        exitCoin = int(input("Insert 3 - 7 coins (0 stops): "))
    else:
        totalCoin += exitCoin
        exitCoin = int(input("Insert 3 - 7 coins (0 stops): "))
   
print("Amount of coins inserted: "+str(totalCoin)+".")
print("Thank you for using the program.")
