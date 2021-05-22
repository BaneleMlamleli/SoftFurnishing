"""
Programmer:     Banele  Mlamleli
Notes:          This code was for my first year june exam. I am re-writing this code implementing different methods
                than the original way I wrote the code.
                I have added 2 image files that have detailed description of the problem
File:           SoftFurnishing.py
Description:    A business that makes soft furnishings (like cushions) on order,
                requires a program that will assist with the daily sales process.
 Date:          07 - July - 2017 22:45:36           
"""
print ('\n***** DAISY SOFT FURNISHINGS *****\n')

nrPieces = 0    #This is quantity
cost = 0.0      #cost per item purchased
totalCost = 0.0 # totalCost += cost
custTotal = 0.0 #This is custTotal += totalCost plus VAT
meter = 0.0     #amount of fabric

#this condition acts as a do-while loop so that a customer can purchase or stop the program
while True:
    customerName = str(raw_input('Please enter customer name or "X" to stop: '))
    checkName = customerName.isalpha()  # check if the entered customerName is all alphabets
    # the below code will give the user another chance to enter a his/her name again
    while checkName != True:
        customerName = str(raw_input('Error! customer name must be alphabets only. Please re-enter customer name: '))
        checkName = customerName.isalpha()
        #if checkName == True:
         #   break

    #If the user chose to stop the program will terminate
    if customerName == 'x':
        break

    #This loop is for a single customer if he/she wants to do another purchase
    while True:
        #Requesting item type code and validating code
        itemCode = int(raw_input('Please enter item type code 1 to 4, or 0 for no more items: '))
        while itemCode < 0 or itemCode > 4:
            itemCode = int(raw_input('Error! item type code must between 1 and 4, or 0 for no more items: '))

        #This condition will check to see if there is no more items for this customer then jump out of the loop
        if itemCode == 0:
            break

        #Requestion quantity and validating entered quantity
        qty = int(raw_input('Please enter quantity: '))
        while qty < 1:
            qty = int(raw_input('Error! Invalid quantity (must be 1 or more) re-enter: '))

        #Requesting fabric code and validating entered code
        fabricCode = int(raw_input('Enter fabric code 1001 - 1010: '))
        while fabricCode < 1001 or fabricCode > 1010:
            fabricCode = int(raw_input('Error! Invalid code, (must be between 1001 and 1010) re-enter code: '))

        if itemCode == 1:
            #code for Cushions
            if fabricCode >= 1001 and fabricCode <= 1003:
                nrPieces += qty
                meter = qty * 1
                cost = (meter * 95.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tCushion\t\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost)+' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1004 and fabricCode <= 1007:
                nrPieces += qty
                meter = qty * 1
                cost = (meter * 150.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tCushion\t\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost)+' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1008 and fabricCode <= 1010:
                nrPieces += qty
                meter = qty * 1
                cost = (meter * 250.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tCushion\t\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost)+' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

        elif itemCode == 2:
            #code for 6X Place Mats
            if fabricCode >= 1001 and fabricCode <= 1003:
                nrPieces += qty
                meter = qty * 2
                cost = (meter * 95.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\t6X Place Mats\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1004 and fabricCode <= 1007:
                nrPieces += qty
                meter = qty * 2
                cost = (meter * 150.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\t6X Place Mats\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1008 and fabricCode <= 1010:
                nrPieces += qty
                meter = qty * 2
                cost = (meter * 250.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\t6X Place Mats\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

        elif itemCode == 3:
            #code for Table Cloth 2.5m x 1m
            if fabricCode >= 1001 and fabricCode <= 1003:
                nrPieces += qty
                meter = qty * 2.5
                cost = (meter * 95.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tTable Cloth 2.5m x 1m\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t'+
                       str(fabricCode)+'\t\t\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1004 and fabricCode <= 1007:
                nrPieces += qty
                meter = qty * 2.5
                cost = (meter * 150.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tTable Cloth 2.5m x 1m\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t'+
                       str(fabricCode)+'\t\t\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1004 and fabricCode <= 1010:
                nrPieces += qty
                meter = qty * 2.5
                cost = (meter * 250.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tTable Cloth 2.5m x 1m\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t'+
                       str(fabricCode)+'\t\t\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

        elif itemCode == 4:
            #code for Table Cloth 2m x 2m
            if fabricCode >= 1001 and fabricCode <= 1003:
                nrPieces += qty
                meter = qty * 4
                cost = (meter * 95.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tTable Cloth 2m x 2m\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1004 and fabricCode <= 1007:
                nrPieces += qty
                meter = qty * 4
                cost = (meter * 150.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tTable Cloth 2m x 2m\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

            elif fabricCode >= 1008 and fabricCode <= 1010:
                nrPieces += qty
                meter = qty * 4
                cost = (meter * 250.0)+100.0
                totalCost = cost+(cost*(14.0/100.0))
                custTotal += totalCost
                print ('--------------------------------------------------------------------')
                print ('Item Type:\tTable Cloth 2m x 2m\t\tQuantity:\t'+str(qty)+'\nFabric:\t\t' +
                       str(fabricCode)+'\t\t\t\t\tMeter:\t\t'+str(meter)+'m')
                print ('\nR'+str(totalCost) + ' include VAT (of which R100.00 is for labour)')
                print ('====================================================================')

    print('\nCustomer:\t'+customerName+'\t\tNr of Pieces:\t'+str(nrPieces))
    print('FINAL DUE (inc VAT):\tR'+str(custTotal))
    #This is at the end of the program to allow the user to enter another customer or stop the program
    print ('####################################################################')
    newCustomer = raw_input('Is there a new customer? "Y" for yes or "X" to stop: ')
    newCustomer = str(newCustomer[0].lower())
    # the below code will give the user another chance to enter a his/her customerName again
    while newCustomer != 'y' and newCustomer != 'x':
        newCustomer = raw_input('Error! Enter "Y" or "X" to stop: ')
        newCustomer = str(newCustomer[0].lower())

    #If the user chose to stop the program will terminate
    if newCustomer == 'x':
        break

#end of the program
print ('\n***** END-OF-DAY CLOSE DOWN *****')