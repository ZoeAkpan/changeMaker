import math
nickels = 25
dimes = 25
quarters = 25 
ones = 0
fives = 0
print("Welcome to the vending machine change maker program\nChange maker initialized.")
print(f"Stock contains:\n   {nickels} nickels \n   {dimes} dimes \n   {quarters} quarters \n   {ones} ones \n   {fives} fives")
print()
purchasePrice = input("Enter the purchase price (xx.xx) or `q' to quit: ")
   
while purchasePrice != 'q':
   valid = True
   for char in purchasePrice:
      if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'] :
         valid = False
         break
   if valid:
      purchasePrice = float(purchasePrice)
      purchasePrice *= 100

      # finding how many dollars and cents they have
      # better way to name variables

      userDollars = int(purchasePrice) // 100
      userCents = int(purchasePrice) % 100
      originalPrice = purchasePrice

      """
      purchasePriceValid = True


      for i in len(str(purchasePrice)):
         if purchasePrice[i] is not int:
            purchasePriceValid = False
      """

      # checking to see if positive number and if multiple of 5 (5 cents goes in)
      if purchasePrice >= 0 and (purchasePrice % 5 == 0):
         print()
         print("Menu for deposits:\n  'n' - deposit a nickel\n  'd' - deposit a dime\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill\n  'c' - cancel the purchase")
         print()
         print("Payment due: ", userDollars, "dollars", "and", userCents, "cents")

         deposit = ""

         while deposit != "c" and purchasePrice > 0:

               deposit = input("Indicate your deposit: ")

               if deposit == "n":
                  if purchasePrice - 5 < 0:
                     amountOwed = math.fabs(purchasePrice - 5)
                     nickels += 1
                     break
                  else:
                     purchasePrice -= 5
                     nickels += 1
                     userDollars = int(purchasePrice // 100)
                     userCents = int(purchasePrice % 100)
                     if purchasePrice == 0:
                        break                  
                     if userDollars != 0:
                        print("Payment due: ", userDollars, "dollars", "and", userCents, "cents")
                     else:
                        print("Payment due: ", userCents, "cents")
               elif deposit == "d":
                  if purchasePrice - 10 < 0:
                     amountOwed = math.fabs(purchasePrice - 10)
                     dimes += 1
                     break
                  else:
                     purchasePrice -= 10
                     dimes += 1
                     userDollars = int(purchasePrice // 100)
                     userCents = int(purchasePrice % 100)
                     if purchasePrice == 0:
                        break                  
                     if userDollars != 0:
                        print("Payment due: ", userDollars, "dollars", "and", userCents, "cents")
                     else:
                        print("Payment due: ", userCents, "cents")
               elif deposit == "q":
                  if purchasePrice - 25 < 0:
                     amountOwed = math.fabs(purchasePrice - 25)
                     quarters += 1
                     break 
                  else:
                     purchasePrice -= 25
                     quarters += 1
                     userDollars = int(purchasePrice // 100)
                     userCents = int(purchasePrice % 100)
                     if purchasePrice == 0:
                        break                  
                     if userDollars != 0:
                        print("Payment due: ", userDollars, "dollars", "and", userCents, "cents")
                     else:
                        print("Payment due: ", userCents, "cents")
               elif deposit == "o":
                  if purchasePrice - 100 < 0:
                     amountOwed = math.fabs(purchasePrice - 100)
                     ones += 1
                     break
                  else:
                     purchasePrice -= 100
                     ones += 1
                     userDollars = int(purchasePrice // 100)
                     userCents = int(purchasePrice % 100)                 
                     if purchasePrice == 0:
                        break                  
                     if userDollars != 0:
                        print("Payment due: ", userDollars, "dollars", "and", userCents, "cents")
                     else:
                        print("Payment due: ", userCents, "cents")
               elif deposit == "f":
                  if purchasePrice - 500 < 0:
                     amountOwed = math.fabs(purchasePrice - 500)
                     fives += 1
                     break
                  else:
                     purchasePrice -= 500
                     fives += 1
                     userDollars = int(purchasePrice // 100)
                     userCents = int(purchasePrice % 100)
                     if purchasePrice == 0:
                        break
                     if userDollars != 0: 
                        print("Payment due: ", userDollars, "dollars", "and", userCents, "cents")
                     else:
                        print("Payment due: ", userCents, "cents") # FIXME you dont want to print this when theyre canceling
               elif deposit not in ["n", "d", "q", "o", "f", "c"]: 
                  print("Illegal selection:", deposit)
         else:
            amountOwed = originalPrice - purchasePrice


         print()

         counterFives = 0
         counterOnes = 0
         counterQuarters = 0
         counterDimes = 0
         counterNickels = 0 

         # calculating change
         if purchasePrice == 0:
            print("  No change due.")
         else:
            print("Please take the change below.")
            while amountOwed // 25 > 0:
               if quarters > 0:
                  amountOwed -= 25
                  quarters -= 1
                  counterQuarters += 1
               else:
                  break
            while amountOwed // 10 > 0:
               if dimes > 0:
                  amountOwed -= 10
                  dimes -= 1
                  counterDimes += 1
               else: 
                  break
            while amountOwed // 5 > 0:
               if nickels > 0:
                  amountOwed -= 5
                  nickels -= 1
                  counterNickels += 1
               else: 
                  break

            if counterFives > 0:
               print("  ", counterFives, 'fives')
            if counterOnes > 0:
               print("  ", counterOnes, 'ones')
            if counterQuarters > 0:
               print("  ", counterQuarters, 'quarters')
            if counterDimes > 0:
               print("  ", counterDimes, 'dimes')
            if counterNickels > 0:
               print("  ", counterNickels, 'nickels')

            if amountOwed != 0.00:
               amountDue = originalPrice - purchasePrice - counterFives * 500 - counterOnes * 100 - counterQuarters * 25 - counterDimes * 10 - counterNickels * 5
               print("Machine is out of change.")
               print("See store manager for remaining refund.")
               print("Amount due: ", amountDue )

         print()                                       

         print(f"Stock contains:\n   {nickels} nickels \n   {dimes} dimes \n   {quarters} quarters \n   {ones} ones \n   {fives} fives")
         print()
         purchasePrice = input("Enter the purchase price (xx.xx) or `q' to quit: ")

      else:
         print("Illegal price: Must be a non-negative multiple of 5 cents.")
         print()

         purchasePrice = input("Enter the purchase price (xx.xx) or `q' to quit: ")

         print()
   else:
      print("Invalid purchase price. Try again")
      purchasePrice = input("Enter the purchase price (xx.xx) or `q' to quit: ")

else:
   total = (fives * 500) + (ones * 100) + (quarters * 25) + (dimes * 10) + (nickels * 5)
   userDollars = int(total) // 100
   userCents = int(total) % 100
   print("Total:", userDollars, "dollars and", userCents, "cents")
   print()
