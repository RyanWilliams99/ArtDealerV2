'''
DADSA Assignment 2018-19 - ArtDealerV2
Ryan Williams - 17009972
'''
import csv

#Defining constants
INSURED_MAX_SINGLE = 2000000000
INSURED_MAX_MULTIPLE = 8000000000
#Used when accessing the warehouse list
WAREHOUSE_A = 0
WAREHOUSE_B = 1
WAREHOUSE_C = 2
WAREHOUSE_D = 3
#Used when accessing the warehouse data list
WAREHOUSE_VALUE = 0
WAREHOUSE_SPACE = 1
WAREHOUSE_ITEMS = 2
WAREHOUSE_RECTANGLE = 3
WAREHOUSE_RECTANGLE_WEIGHT = 4
WAREHOUSE_SPHERE = 5
WAREHOUSE_SPHERE_WEIGHT = 6
WAREHOUSE_PYRAMID = 7
WAREHOUSE_PYRAMID_WEIGHT = 8
WAREHOUSE_SQUARE = 9
WAREHOUSE_SQUARE_WEIGHT = 10

WAREHOUSE_SHAPES = ['Rectangle', 'Sphere', 'Pyramid', 'Square']
#Only used when printing warehouse names
WAREHOUSE_NAMES = ['A', 'B', 'C', 'D']
#Used when iterationg over the warehouse list
NUMBER_OF_WAREHOUSES = 4
MAX_NUMBER_OF_ITEMS = 1024
#Used to create the warehouse list to store the csv files contents
COLUMNS_IN_CSV = 5

#Defines a list of length 4 with 1024 sublists then another 3 sublist for all 1024
warehouse = [[[0 for j in range(COLUMNS_IN_CSV)] for i in range(MAX_NUMBER_OF_ITEMS)] for k in range(NUMBER_OF_WAREHOUSES)]
#2D list used to store the data about each of the warehouses
warehouseData = warehouseA = [[0 for x in range(11)] for y in range(NUMBER_OF_WAREHOUSES)]
overallCapacity = 0

#Initialises a warehouse takes a int warehouse number as paramater
def initialiseWarehouses(warehouseNumber):
    #for x in range(NUMBER_OF_WAREHOUSES):
        with open('DADSA Assignment 2018-19 PART B Warehouse ' + WAREHOUSE_NAMES[warehouseNumber] + '.csv') as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=',')  # returns a reader object which is then iterated over
            for row in csv_reader:  # For every row in csv file
                if warehouseData[warehouseNumber][WAREHOUSE_ITEMS] == 0:  # This excludes the first row of the file
                    warehouseData[warehouseNumber][WAREHOUSE_ITEMS] += 1
                else:
                    for x in range(COLUMNS_IN_CSV):  # For every column in csv file store value in warehouse list
                        warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS] - 1][x] = row[x]
                    warehouseData[warehouseNumber][WAREHOUSE_ITEMS] += 1
                    print(row[3])

            warehouseData[warehouseNumber][WAREHOUSE_ITEMS] -= 1  # Used so the value displayed is correct for the user
            for x in range(warehouseData[warehouseNumber][WAREHOUSE_ITEMS]):  # Calculating Value of warehouse
                warehouseData[warehouseNumber][WAREHOUSE_VALUE] = warehouseData[warehouseNumber][WAREHOUSE_VALUE] + int(warehouse[warehouseNumber][x][2])
            # Calculating space left in warehouse
            warehouseData[warehouseNumber][WAREHOUSE_SPACE] = INSURED_MAX_SINGLE - warehouseData[warehouseNumber][
                WAREHOUSE_VALUE]
        #Shapes Allowed
        warehouseData[WAREHOUSE_A][WAREHOUSE_RECTANGLE] = 5
        warehouseData[WAREHOUSE_A][WAREHOUSE_RECTANGLE_WEIGHT] = 1000
        warehouseData[WAREHOUSE_A][WAREHOUSE_PYRAMID] = 10
        warehouseData[WAREHOUSE_A][WAREHOUSE_PYRAMID_WEIGHT] = 2000
        warehouseData[WAREHOUSE_A][WAREHOUSE_SQUARE] = 5
        warehouseData[WAREHOUSE_A][WAREHOUSE_SQUARE_WEIGHT] = 2000

        warehouseData[WAREHOUSE_B][WAREHOUSE_RECTANGLE] = 10
        warehouseData[WAREHOUSE_B][WAREHOUSE_RECTANGLE_WEIGHT] = 500
        warehouseData[WAREHOUSE_B][WAREHOUSE_SPHERE] = 5
        warehouseData[WAREHOUSE_B][WAREHOUSE_SPHERE_WEIGHT] = 2000
        warehouseData[WAREHOUSE_B][WAREHOUSE_PYRAMID] = 10
        warehouseData[WAREHOUSE_B][WAREHOUSE_PYRAMID_WEIGHT] = 250

        warehouseData[WAREHOUSE_C][WAREHOUSE_SPHERE] = 15
        warehouseData[WAREHOUSE_C][WAREHOUSE_SPHERE_WEIGHT] = 250
        warehouseData[WAREHOUSE_C][WAREHOUSE_PYRAMID] = 5
        warehouseData[WAREHOUSE_C][WAREHOUSE_PYRAMID_WEIGHT] = 500

        warehouseData[WAREHOUSE_D][WAREHOUSE_RECTANGLE] = 10
        warehouseData[WAREHOUSE_D][WAREHOUSE_RECTANGLE_WEIGHT] = 500
        warehouseData[WAREHOUSE_D][WAREHOUSE_SPHERE] = 2
        warehouseData[WAREHOUSE_D][WAREHOUSE_SPHERE_WEIGHT] = 750
        warehouseData[WAREHOUSE_D][WAREHOUSE_PYRAMID] = 2
        warehouseData[WAREHOUSE_D][WAREHOUSE_PYRAMID_WEIGHT] = 3000
        warehouseData[WAREHOUSE_D][WAREHOUSE_SQUARE] = 10
        warehouseData[WAREHOUSE_D][WAREHOUSE_SQUARE_WEIGHT] = 750


def printAllWarehouses():
    print("Printing contents of all warehouses...")
    for x in range(NUMBER_OF_WAREHOUSES): #For every warehouse
        print(" _____________________________________________________________________________________________"
              "\n|_________________________________________Warehouse_{}_________________________________________|".format(WAREHOUSE_NAMES[x]),
              "\n|Item No. | Description                                 | Value      | Shape     | Weight (Kg)|")
        for t in range(warehouseData[x][WAREHOUSE_ITEMS]): #For the number of items in the current warehouse x
            print("|{:<9}|".format(warehouse[x][t][0]), "{:<44}|".format(warehouse[x][t][1]), #print the values in a row
                  "£{:<10}|".format(warehouse[x][t][2]), "{:<10}|".format(warehouse[x][t][3]), "{:<8}   |".format(warehouse[x][t][4]))
        print("|_________|_____________________________________________|____________|___________|____________|")
    #Prints the number of items in each warehouse
    print("No. of items in all warehouses\nA -" ,warehouseData[WAREHOUSE_A][WAREHOUSE_ITEMS], "B -" ,warehouseData[WAREHOUSE_B][WAREHOUSE_ITEMS]
                                         ,"C -" ,warehouseData[WAREHOUSE_C][WAREHOUSE_ITEMS], "D -" ,warehouseData[WAREHOUSE_D][WAREHOUSE_ITEMS],"\n")
    for y in range(NUMBER_OF_WAREHOUSES): #Prints percentage space used in each warehouse
        print('Warehouse {} at {}% capacity'.format(WAREHOUSE_NAMES[y],round((100 - warehouseData[y][WAREHOUSE_SPACE] / INSURED_MAX_SINGLE * 100),4)))
        print("Storage for Warehouse " + WAREHOUSE_NAMES[y])
        print(" Rectangle: " + str(warehouseData[y][WAREHOUSE_RECTANGLE]) + " x " + str(warehouseData[y][WAREHOUSE_RECTANGLE_WEIGHT]) + "kg")
        print(" Sphere: " + str(warehouseData[y][WAREHOUSE_SPHERE]) + " x " + str(warehouseData[y][WAREHOUSE_SPHERE_WEIGHT]) + "kg")
        print(" Pyramid: " + str(warehouseData[y][WAREHOUSE_PYRAMID]) + " x " + str(warehouseData[y][WAREHOUSE_PYRAMID_WEIGHT]) + "kg")
        print(" Square: " + str(warehouseData[y][WAREHOUSE_SQUARE]) + " x " + str(warehouseData[y][WAREHOUSE_SQUARE_WEIGHT]) + "kg")
    #Calculate and prints the capacty of all warehouses combined
    overallCapacity = warehouseData[WAREHOUSE_A][WAREHOUSE_SPACE] + warehouseData[WAREHOUSE_B][WAREHOUSE_SPACE] + \
                      warehouseData[WAREHOUSE_C][WAREHOUSE_SPACE] + warehouseData[WAREHOUSE_D][WAREHOUSE_SPACE]
    print('Storage capacity across all 4 Warehouses is at {}%\n'.format(round((100 - overallCapacity/INSURED_MAX_MULTIPLE * 100),4)))


def addNewItem(warehouseNumber, itemNumber, description, value, shape, weight):
    if warehouseData[warehouseNumber][getShapeNumber(shape)] > 0: #good if true
        #print("Shape allowed in this warehouse")
        if value < warehouseData[warehouseNumber][WAREHOUSE_SPACE] or value > INSURED_MAX_SINGLE: #good if true
            #print("Item value is low enough")
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][0] = itemNumber
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][1] = description
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][2] = value
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][3] = shape
            warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][4] = weight
            warehouseData[warehouseNumber][WAREHOUSE_SPACE] = warehouseData[warehouseNumber][WAREHOUSE_SPACE] - value
            warehouseData[warehouseNumber][WAREHOUSE_ITEMS] = warehouseData[warehouseNumber][WAREHOUSE_ITEMS] + 1
        else:
            print("Item value is too much")
            addNewItem(warehouseNumber + 1, itemNumber, description, value, shape, weight)
    else:
        print("Cannot store " + shape + " in Warehouse " + WAREHOUSE_NAMES[warehouseNumber])
        addNewItem(warehouseNumber + 1, itemNumber, description, value, shape, weight)


def getShapeNumber(passedString):
    for x in range(NUMBER_OF_WAREHOUSES):
        if passedString == WAREHOUSE_SHAPES[x]:
            return x + 5


def getWarehouseNumber(passedString):
    for x in range(NUMBER_OF_WAREHOUSES):
        if passedString == WAREHOUSE_NAMES[x]:
            return x

def getItemValue(warehouseNumber, itemNumber):
    for x in range(warehouseData[warehouseNumber][WAREHOUSE_ITEMS]):
        if str(itemNumber) == str(warehouse[warehouseNumber][x][0]):
            return warehouse[warehouseNumber][x][2]
    print("Cant Find")



def getItemWeight(warehouseNumber, itemNumber):
    for x in range(warehouseData[warehouseNumber][WAREHOUSE_ITEMS]):
        if str(itemNumber) == str(warehouse[warehouseNumber][x][0]):
            return warehouse[warehouseNumber][x][4]
    print("Cant Find")




def task1():
    print("Task 1")
    addedItems = 0
    with open('DADSA Assignment 2018-19 PART B DATA TO INSERT INTO WAREHOUSE A TASK 1.csv') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',')  # returns a reader object which is then iterated over
        for row in csv_reader:  #For every row in csv file
            if addedItems == 0:
                print("Excluding First Row")
                addedItems = addedItems + 1
            else:
                #print("Adding item " + row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[4])
                addNewItem(WAREHOUSE_A, row[0], row[1], int(row[2]), row[3], row[4])


def task2a():
    print("Task 2a")
    addedItems = 0
    currentVanValue = 0
    daysToRelocate = 0

    with open('DADSA Assignment 2018-19 PART B DATA FOR TASK 2.csv') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',')  # returns a reader object which is then iterated over
        for row in csv_reader:  #For every row in csv file
            if addedItems == 0:
                addedItems = addedItems + 1
            else:
                daysToRelocate += 1
        print("Ignoring Insurance value and shape of items it will take " + str(daysToRelocate) + " days to move items")
        return daysToRelocate


def task2b(): # Calculate number of days whilst taking into account van can only move 1.5 bn and destination warehouse must have shape avalable
    print("Task 2")
    addedItems = 0
    currentVanValue = 0
    currentVanWeight = 0
    currentDaysToRelocate = task2a()
    moveList = [[0 for x in range(3)] for x in range(10)]
    with open('DADSA Assignment 2018-19 PART B DATA FOR TASK 2.csv') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',')  # returns a reader object which is then iterated over
        for row in csv_reader:  #For every row in csv file
            if addedItems == 0:
                addedItems += 1
            else:
                moveList[addedItems - 1][0] = row[0]
                moveList[addedItems - 1][1] = row[1]
                moveList[addedItems - 1][2] = row[2]
                addedItems += 1
                print(row[0] + " " + row[1] + " " + row[2])
        print(moveList)
        for x in range(9):
            if moveList[x][1] == moveList[x + 1][1] and moveList[x][2] == moveList[x + 1][2]:
                # Now should see if can do 2 items in one move because value is less than 1.5bn and less than 2000kg
                print("Possible double move item " + str(moveList[x][0]) + " and item " + str(moveList[x + 1][0]) + " Going to from warehouse " + str(moveList[x][1]) + " To warehouse " + str(moveList[x][2]))
                value1 = int(getItemValue(getWarehouseNumber(moveList[x][1]),int(moveList[x][0])))
                value2 = int(getItemValue(getWarehouseNumber(moveList[x + 1][1]),int(moveList[x + 1][0])))
                currentVanValue = value1 + value2
                weight = getItemWeight(getWarehouseNumber(moveList[x][1]),int(moveList[x][0]))
                #print("Value of item " + str(cvalue) + " Weight of Item " + str(weight))
                if int(currentVanValue) < 1500000000 and currentVanWeight < 2000:
                    currentDaysToRelocate -= 1
        print("To move items considering weight capacity and value capacity of van it will take " + str(currentDaysToRelocate) + " Days")



initialiseWarehouses(WAREHOUSE_A)
initialiseWarehouses(WAREHOUSE_B)
initialiseWarehouses(WAREHOUSE_C)
initialiseWarehouses(WAREHOUSE_D)
printAllWarehouses()
task1()
printAllWarehouses()
task2a()
task2b()