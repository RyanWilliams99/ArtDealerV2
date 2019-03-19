"""
DADSA Assignment 2018-19 - ArtDealerV2
Ryan Williams - 17009972
"""
import csv
# Defining constants
INSURED_MAX_SINGLE = 2000000000
INSURED_MAX_VAN = 2000000000 * 0.75
INSURED_MAX_MULTIPLE = 8000000000
# Used when accessing the warehouse list
WAREHOUSE_A = 0
WAREHOUSE_B = 1
WAREHOUSE_C = 2
WAREHOUSE_D = 3
WAREHOUSE_ID = 0
WAREHOUSE_DESC = 1
WAREHOUSE_VALUE = 2
WAREHOUSE_SHAPE = 3
WAREHOUSE_WEIGHT = 4
# Used when accessing the warehouse data list
WAREHOUSE_DATA_VALUE = 0
WAREHOUSE_DATA_SPACE = 1
WAREHOUSE_DATA_ITEMS = 2
WAREHOUSE_DATA_RECTANGLE = 3
WAREHOUSE_DATA_SPHERE = 5
WAREHOUSE_DATA_PYRAMID = 7
WAREHOUSE_DATA_SQUARE = 9
WAREHOUSE_DATA_LIST_ITEMS = 11

WAREHOUSE_SHAPES = ['Rectangle', 'Sphere', 'Pyramid', 'Square']
# Only used when printing warehouse names
WAREHOUSE_NAMES = ['A', 'B', 'C', 'D']
# Used when iterating over the warehouse list
NUMBER_OF_WAREHOUSES = 4
MAX_NUMBER_OF_ITEMS = 1024
# Used to create the warehouse list to store the csv files contents
COLUMNS_IN_CSV = 5

# Defines a list of length 4 with 1024 sublists then another 3 sublist for all 1024
warehouse = [[[0 for x in range(COLUMNS_IN_CSV)] for y in range(MAX_NUMBER_OF_ITEMS)] for z in range(NUMBER_OF_WAREHOUSES)]
# 2D list used to store the data about each of the warehouses
warehouseData =  [[0 for x in range(WAREHOUSE_DATA_LIST_ITEMS)] for y in range(NUMBER_OF_WAREHOUSES)]
overallCapacity = 0

# Define Valid routes for Task 3 and 4
col = 2
row = 6
validRoutes = [[6 for x in range(col)] for y in range(row)]

validRoutes[0][0] = WAREHOUSE_A
validRoutes[0][1] = WAREHOUSE_B
validRoutes[1][0] = WAREHOUSE_A
validRoutes[1][1] = WAREHOUSE_C
validRoutes[2][0] = WAREHOUSE_A
validRoutes[2][1] = WAREHOUSE_D
validRoutes[3][0] = WAREHOUSE_B
validRoutes[3][1] = WAREHOUSE_C
validRoutes[4][0] = WAREHOUSE_B
validRoutes[4][1] = WAREHOUSE_D
validRoutes[5][0] = WAREHOUSE_C
validRoutes[5][1] = WAREHOUSE_D


# Initialises a warehouse takes a int warehouse number as paramater
def initWarehouses():
    for x in range(NUMBER_OF_WAREHOUSES):
        warehouseData[x][WAREHOUSE_DATA_SPACE] = INSURED_MAX_SINGLE
        with open('DADSA Assignment 2018-19 PART B Warehouse ' + WAREHOUSE_NAMES[x] + '.csv') as csvFile:
            csv_reader = csv.reader(csvFile)  # returns a reader object which is then iterated over
            for row in csv_reader:  # For every row in csv file
                if row[0] != 'Item No.':  # This excludes the first row of the file
                    addNewItem(x, int(row[0]), str(row[1]), int(row[2]), str(row[3]), int(row[4]))
            for y in range(warehouseData[x][WAREHOUSE_DATA_ITEMS]):  # Calculating Value of warehouse
                warehouseData[x][WAREHOUSE_DATA_VALUE] = warehouseData[x][WAREHOUSE_DATA_VALUE] + int(warehouse[x][y][2])
            warehouseData[x][WAREHOUSE_DATA_SPACE] = INSURED_MAX_SINGLE - warehouseData[x][WAREHOUSE_DATA_VALUE]

def printAllWarehouses():
    print("Printing contents of all warehouses...")
    for x in range(NUMBER_OF_WAREHOUSES): # For every warehouse
        print(" _____________________________________________________________________________________________"
              "\n|_________________________________________Warehouse_{}_________________________________________|".format(WAREHOUSE_NAMES[x]),
              "\n|Item No. | Description                                 | Value      | Shape     | Weight (Kg)|")
        for t in range(warehouseData[x][WAREHOUSE_DATA_ITEMS]): #For the number of items in the current warehouse x
            print("|{:<9}|".format(warehouse[x][t][0]), "{:<44}|".format(warehouse[x][t][1]), #print the values in a row
                  "£{:<10}|".format(warehouse[x][t][2]), "{:<10}|".format(warehouse[x][t][3]), "{:<8}   |".format(warehouse[x][t][4]))
        print("|_________|_____________________________________________|____________|___________|____________|")
    # Prints the number of items in each warehouse
    print("No. of items in all warehouses\nA -", warehouseData[WAREHOUSE_A][WAREHOUSE_DATA_ITEMS], "B -", warehouseData[WAREHOUSE_B][WAREHOUSE_DATA_ITEMS]
          ,"C -", warehouseData[WAREHOUSE_C][WAREHOUSE_DATA_ITEMS], "D -", warehouseData[WAREHOUSE_D][WAREHOUSE_DATA_ITEMS], "\n")
    for y in range(NUMBER_OF_WAREHOUSES): # Prints percentage space used in each warehouse
        print('Warehouse {} at {}% Insurance capacity'.format(WAREHOUSE_NAMES[y], round((100 - warehouseData[y][WAREHOUSE_DATA_SPACE] / INSURED_MAX_SINGLE * 100), 4)))
        print("Remaining Storage Types for Warehouse " + WAREHOUSE_NAMES[y])
        print(" Rectangle: " + str(warehouseData[y][WAREHOUSE_DATA_RECTANGLE]) + " x " + str(warehouseData[y][WAREHOUSE_DATA_RECTANGLE + 1]) + "kg")
        print(" Sphere: " + str(warehouseData[y][WAREHOUSE_DATA_SPHERE]) + " x " + str(warehouseData[y][WAREHOUSE_DATA_SPHERE + 1]) + "kg")
        print(" Pyramid: " + str(warehouseData[y][WAREHOUSE_DATA_PYRAMID]) + " x " + str(warehouseData[y][WAREHOUSE_DATA_PYRAMID + 1]) + "kg")
        print(" Square: " + str(warehouseData[y][WAREHOUSE_DATA_SQUARE]) + " x " + str(warehouseData[y][WAREHOUSE_DATA_SQUARE + 1]) + "kg\n")
    # Calculate and prints the capacty of all warehouses combined
    overallCapacity = warehouseData[WAREHOUSE_A][WAREHOUSE_DATA_SPACE] + warehouseData[WAREHOUSE_B][WAREHOUSE_DATA_SPACE] + \
                      warehouseData[WAREHOUSE_C][WAREHOUSE_DATA_SPACE] + warehouseData[WAREHOUSE_D][WAREHOUSE_DATA_SPACE]
    print('Insurance Value across all 4 Warehouses is at {}%\n'.format(round((100 - overallCapacity/INSURED_MAX_MULTIPLE * 100),4)))


def addNewItem(warehouseNumber, itemNumber, description, value, shape, weight):
    if warehouseData[warehouseNumber][getShapeNumber(shape)] > 0: # Good if true
        if value < warehouseData[warehouseNumber][WAREHOUSE_DATA_SPACE] and value < INSURED_MAX_SINGLE: # value is less than space, and space is less than 2bn
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_DATA_ITEMS]][0] = itemNumber # Add the new item
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_DATA_ITEMS]][1] = description
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_DATA_ITEMS]][2] = value
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_DATA_ITEMS]][3] = shape
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_DATA_ITEMS]][4] = weight
            warehouseData[warehouseNumber][WAREHOUSE_DATA_SPACE] = warehouseData[warehouseNumber][WAREHOUSE_DATA_SPACE] - value
            warehouseData[warehouseNumber][WAREHOUSE_DATA_ITEMS] += 1 # Increment items remove space and remove 1 shape
            warehouseData[warehouseNumber][getShapeNumber(shape)] -= 1
        else: #Should try to add somewhere else
            print("Item value is too much for this warehouse")
            if warehouseNumber + 1 < 4: #As long as in bounds try next warehouse
                addNewItem(warehouseNumber + 1, itemNumber, description, value, shape, weight)
    else:
        print("Cannot store " + shape + " in Warehouse " + WAREHOUSE_NAMES[warehouseNumber])
        if warehouseNumber + 1 < 4:
            addNewItem(warehouseNumber + 1, itemNumber, description, value, shape, weight)


def getShapeNumber(passedString): # Returns the shape number used in warehouse data
    if passedString == 'Rectangle':
        return WAREHOUSE_DATA_RECTANGLE
    if passedString == 'Sphere':
        return WAREHOUSE_DATA_SPHERE
    if passedString == 'Pyramid':
        return WAREHOUSE_DATA_PYRAMID
    if passedString == 'Square':
        return WAREHOUSE_DATA_SQUARE
    return 0

def getShapeName(shapeNumber): # Reverse of the above
    if shapeNumber == WAREHOUSE_DATA_RECTANGLE:
        return 'Rectangle'
    if shapeNumber == WAREHOUSE_DATA_SPHERE:
        return 'Sphere'
    if shapeNumber == WAREHOUSE_DATA_PYRAMID:
        return 'Pyramid'
    if shapeNumber == WAREHOUSE_DATA_SQUARE:
        return 'Square'
    return 'Not Found'

def getWarehouseNumber(passedString): # Returns warehouse number. eg convert 'A' to WAREHOUSE_A or 0
    for x in range(NUMBER_OF_WAREHOUSES):
        if passedString == WAREHOUSE_NAMES[x]:
            return x

        
def getItemData(itemNumber, dataRequested): # Takes item number and 0-4 for which column eg 15108 3 returns the shape
    for x in range(NUMBER_OF_WAREHOUSES): # For every warehouse
        for y in range(warehouseData[x][WAREHOUSE_DATA_ITEMS]): # For number of items in current warehouse
            if int(itemNumber) == int(warehouse[x][y][0]):
                if dataRequested == WAREHOUSE_VALUE or dataRequested == WAREHOUSE_WEIGHT:
                    return int(warehouse[x][y][dataRequested])
                else:
                    return str(warehouse[x][y][dataRequested])

def initWarehouseData(): #Reads Shape and weight data from a CSV
    with open('DADSA Assignment 2018-19 PART B Warehouse Capacity.csv') as csvFile:
        csv_reader = csv.reader(csvFile)  # returns a reader object which is then iterated over
        for row in csv_reader:  # For every row in csv file
            if row[0] != 'Warehouse':  # This excludes the first row of the file
                warehouseData[int(row[0])][int(row[1])] = int(row[2])
                warehouseData[int(row[0])][int(row[1]) + 1] = int(row[3])

def clearWarehouseData():
    for x in range(NUMBER_OF_WAREHOUSES):
        for y in range(COLUMNS_IN_CSV):
            warehouse[x][y] = 0
        # for y in range(WAREHOUSE_DATA_LIST_ITEMS):
        #     warehouseData[x][y] = 0

def task1(): # Add new items based on data in TASK 1 CSV
    print("__________________________________________________Task 1__________________________________________________")
    addedItems = 0
    with open('DADSA Assignment 2018-19 PART B DATA TO INSERT INTO WAREHOUSE A TASK 1.csv') as csvFile:
        csv_reader = csv.reader(csvFile)  # returns a reader object which is then iterated over
        for row in csv_reader:  # For every row in csv file
            if addedItems == 0:
                print("Excluding First Row")
                addedItems = addedItems + 1
            else:
                addNewItem(WAREHOUSE_A, row[0], row[1], int(row[2]), row[3], row[4])


def task2a(): # Calculate days to move items based on csv
    print("__________________________________________________Task 2a__________________________________________________")
    addedItems = 0
    daysToRelocate = 0

    with open('DADSA Assignment 2018-19 PART B DATA FOR TASK 2.csv') as csvFile:
        csv_reader = csv.reader(csvFile)  # returns a reader object which is then iterated over
        for row in csv_reader:  # For every row in csv file
            if addedItems == 0:
                addedItems = addedItems + 1
            else:
                daysToRelocate += 1
        print("Ignoring Insurance value and shape of items it will take " + str(daysToRelocate) + " days to move items")
        return daysToRelocate


def task2b(): # Calculate number of days whilst taking into account van weight and value
    print("__________________________________________________Task 2b__________________________________________________")
    CSV_LENGTH = 10 #Declare constants and 2D list
    vanSchedule = [['N/A' for x in range(CSV_LENGTH)] for x in range(15)]
    vanScheduleItems = 0
    FROM = 0
    TO = 1
    NUMBEROFITEMS = 2
    VANVALUE = 3
    VANWEIGHT = 4
    ITEM = 5
    with open('DADSA Assignment 2018-19 PART B DATA FOR TASK 2.csv') as csvFile:
        csv_reader = csv.reader(csvFile)
        for row in csv_reader: # For every row
            if row[0] != 'ITEM': # Excluding First row
                vanSchedule[vanScheduleItems][FROM] = row[1]
                vanSchedule[vanScheduleItems][TO] = row[2]
                vanSchedule[vanScheduleItems][NUMBEROFITEMS] = 1
                vanSchedule[vanScheduleItems][ITEM] = row[0]
                vanSchedule[vanScheduleItems][VANVALUE] = getItemData(row[0], WAREHOUSE_VALUE)
                vanSchedule[vanScheduleItems][VANWEIGHT] = getItemData(row[0], WAREHOUSE_WEIGHT)
                vanScheduleItems += 1
    for x in range(CSV_LENGTH): # For every row
        for y in range(CSV_LENGTH):# Check every row
            # Check is Going from and to same warehouse
            if vanSchedule[x][FROM] == vanSchedule[y][FROM] and vanSchedule[x][TO] == vanSchedule[y][TO] and vanSchedule[x][ITEM] != vanSchedule[y][ITEM]:
                # Check value is not too much
                if vanSchedule[x][VANVALUE] + getItemData(row[0], WAREHOUSE_VALUE) < INSURED_MAX_VAN:
                    # Check weight is not too much
                    if vanSchedule[x][VANWEIGHT] + getItemData(row[0], WAREHOUSE_WEIGHT) < 2000:
                        vanSchedule[x][NUMBEROFITEMS] += 1 # Increment values
                        vanSchedule[x][FROM] = vanSchedule[y][FROM]
                        vanSchedule[x][TO] = vanSchedule[y][TO]
                        vanSchedule[x][vanSchedule[x][NUMBEROFITEMS] + 4] = vanSchedule[y][ITEM]
                        vanSchedule[x][VANVALUE] += getItemData(row[0], WAREHOUSE_VALUE)
                        vanSchedule[x][VANWEIGHT] += getItemData(row[0], WAREHOUSE_WEIGHT)
                        vanSchedule[y][FROM] = 0 # Reset to 0
                        vanSchedule[y][TO] = 0
                        vanSchedule[y][ITEM] = 0
    # Print Table form
    printVanSchedule(CSV_LENGTH - 1, vanSchedule)

def task3(): # Calculate number of days whilst taking into account van can only move 1.5 bn and destination warehouse must have shape avalable
    print("\n_________________________________________________Task 3_________________________________________________")
    CSV_LENGTH = 17 #Declare constants and 2D list
    vanSchedule = [['N/A' for x in range(10)] for x in range(CSV_LENGTH)]
    vanScheduleItems = 0
    FROM = 0
    TO = 1
    NUMBEROFITEMS = 2
    VANVALUE = 3
    VANWEIGHT = 4
    ITEM = 5
    with open('DADSA Assignment 2018-19 PART B DATA FOR TASK 3 AND 4.csv') as csvFile:
        csv_reader = csv.reader(csvFile)
        for row in csv_reader:
            if row[0] != 'ITEM':
                vanSchedule[vanScheduleItems][FROM] = row[1]
                vanSchedule[vanScheduleItems][TO] = row[2]
                vanSchedule[vanScheduleItems][NUMBEROFITEMS] = 1
                vanSchedule[vanScheduleItems][ITEM] = row[0]
                vanSchedule[vanScheduleItems][VANVALUE] = getItemData(row[0], WAREHOUSE_VALUE)
                vanSchedule[vanScheduleItems][VANWEIGHT] = getItemData(row[0], WAREHOUSE_WEIGHT)
                vanScheduleItems += 1
    for x in range(CSV_LENGTH):
        for y in range(CSV_LENGTH):
            if vanSchedule[x][FROM] == vanSchedule[y][FROM] and vanSchedule[x][TO] == vanSchedule[y][TO] and vanSchedule[x][ITEM] != vanSchedule[y][ITEM]:
                if vanSchedule[x][VANVALUE] + getItemData(row[0], WAREHOUSE_VALUE) < INSURED_MAX_VAN:
                    if vanSchedule[x][VANWEIGHT] + getItemData(row[0], WAREHOUSE_WEIGHT) < 2000:
                        vanSchedule[x][NUMBEROFITEMS] += 1
                        vanSchedule[x][FROM] = vanSchedule[y][FROM]
                        vanSchedule[x][TO] = vanSchedule[y][TO]
                        vanSchedule[x][vanSchedule[x][NUMBEROFITEMS] + 4] = vanSchedule[y][ITEM]
                        vanSchedule[x][VANVALUE] += getItemData(row[0], WAREHOUSE_VALUE)
                        vanSchedule[x][VANWEIGHT] += getItemData(row[0], WAREHOUSE_WEIGHT)
                        vanSchedule[y][FROM] = 0
                        vanSchedule[y][TO] = 0
                        vanSchedule[y][ITEM] = 0
                    else:
                        print("Cant have will be too high WEIGHT")
                else:
                    print("Cant have will be too high value")

    printVanSchedule(CSV_LENGTH - 1, vanSchedule)


    for x in range (vanScheduleItems):
        for y in range(6):
            if getWarehouseNumber(vanSchedule[x][FROM]) == validRoutes[y][0] and getWarehouseNumber(vanSchedule[x][TO]) == validRoutes[y][1]:
                print("Route From: " + str(vanSchedule[x][FROM]) + " To: " + str(vanSchedule[x][TO]) + " is valid")


def task4():
    print("|________________________________________________Task 4________________________________________________|\n")
    CSV_LENGTH = 17 #Declare constants and 2D list
    vanSchedule = [['N/A' for x in range(10)] for x in range(CSV_LENGTH)]
    vanScheduleItems = 0
    FROM = 0
    TO = 1
    NUMBEROFITEMS = 2
    VANVALUE = 3
    VANWEIGHT = 4
    SHAPE = 5
    ITEM = 6
    with open('DADSA Assignment 2018-19 PART B DATA FOR TASK 3 AND 4.csv') as csvFile:
        csv_reader = csv.reader(csvFile)
        for row in csv_reader:
            if row[0] != 'ITEM':
                vanSchedule[vanScheduleItems][FROM] = row[1]
                vanSchedule[vanScheduleItems][TO] = row[2]
                vanSchedule[vanScheduleItems][NUMBEROFITEMS] = 1
                vanSchedule[vanScheduleItems][ITEM] = row[0]
                vanSchedule[vanScheduleItems][VANVALUE] = getItemData(row[0], WAREHOUSE_VALUE)
                vanSchedule[vanScheduleItems][VANWEIGHT] = getItemData(row[0], WAREHOUSE_WEIGHT)
                vanSchedule[vanScheduleItems][SHAPE] = getItemData(row[0], WAREHOUSE_SHAPE)
                vanScheduleItems += 1
    for x in range(CSV_LENGTH):
        for y in range(CSV_LENGTH):
            if vanSchedule[x][FROM] == vanSchedule[y][FROM] and vanSchedule[x][TO] == vanSchedule[y][TO] and vanSchedule[x][ITEM] != vanSchedule[y][ITEM]:
                if vanSchedule[x][VANVALUE] + getItemData(row[0], WAREHOUSE_VALUE) < INSURED_MAX_VAN:
                    if vanSchedule[x][VANWEIGHT] + getItemData(row[0], WAREHOUSE_WEIGHT) < 2000:
                        if vanSchedule[x][SHAPE] == getItemData(row[0], WAREHOUSE_SHAPE):
                            vanSchedule[x][NUMBEROFITEMS] += 1
                            vanSchedule[x][FROM] = vanSchedule[y][FROM]
                            vanSchedule[x][TO] = vanSchedule[y][TO]
                            vanSchedule[x][vanSchedule[x][NUMBEROFITEMS] + 5] = vanSchedule[y][ITEM]
                            vanSchedule[x][VANVALUE] += getItemData(row[0], WAREHOUSE_VALUE)
                            vanSchedule[x][VANWEIGHT] += getItemData(row[0], WAREHOUSE_WEIGHT)
                            vanSchedule[y][FROM] = 0
                            vanSchedule[y][TO] = 0
                            vanSchedule[y][ITEM] = 0
                    else:
                        print("Cant have will be too high WEIGHT")
                else:
                    print("Cant have will be too high value")

    printVanSchedule(CSV_LENGTH - 1, vanSchedule)

    for x in range (vanScheduleItems):
        for y in range(6):
            if getWarehouseNumber(vanSchedule[x][FROM]) == validRoutes[y][0] and getWarehouseNumber(vanSchedule[x][TO]) == validRoutes[y][1]:
                print("Route From: " + str(vanSchedule[x][FROM]) + " To: " + str(vanSchedule[x][TO]) + " is valid")


def printVanSchedule(length, vanSchedule): #Prints a 2d list in table form. Used to display van schedule
    linesPrinted = 0
    print(" ____________________________________________________________________________________________________________________"
        "\n|_____________________________________________________Van Schedule___________________________________________________|"
        "\n| Day No. | From | To   | No. Items | Total Value | Total Weight | Shape     | Item(s)                               |")
    for x in range(length): #For the number of items in list
        if vanSchedule[x][0] != 0:
            linesPrinted += 1
            print(
                "| {:<7} |".format(linesPrinted), "{:<5}|".format(vanSchedule[x][0]), "{:<5}|".format(vanSchedule[x][1]),
                "{:<9} |".format(vanSchedule[x][2]), "{:<10}  |".format(vanSchedule[x][3]),
                "{:<12} |".format(vanSchedule[x][4]), "{:<9} |".format(getShapeName(vanSchedule[x][5])),
                "{:<7} |".format(vanSchedule[x][6]), "{:<7} |".format(vanSchedule[x][7]),"{:<7} |".format(vanSchedule[x][8]),
                "{:<7} |".format(vanSchedule[x][9]), )
    print("|_________|______|______|___________|_____________|______________|___________________________________________________|")


def mainProgramLoop():

    while(1): #Infinite loop that waits until user gives input

        print("_________________________________________________________________________________________________________\n"
              "Art Dealer warehouse manager Enter a number between 1 - 6\n1 - Task 1\n2 - Task 2\n3 - Task 3\n4 - Task 2"
              "\n5 - Print All Warehouses\n6 - Exit")
        command = input("Enter a command number between 0 and 5\n") #Prompts for user input
        if (command.isdigit() == False) or (int(command) < 0) or (int(command)) > 6: #Checks user input is valid
            print("Invalid Command number")
            mainProgramLoop() #Calls the main loop again to "reset" if the input is invalid

        if int(command) == 1:
            task1()
            printAllWarehouses()

        if int(command) == 2:
            task2a()
            task2b()

        if int(command) == 3:
            task3()

        if int(command) == 4:
            task4()

        if int(command) == 5:
            printAllWarehouses()

        if int(command) == 6:
            exit(0)


initWarehouseData()
initWarehouses()
mainProgramLoop()