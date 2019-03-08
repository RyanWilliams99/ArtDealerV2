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



#Add a new item to a warehouse using the data passed to it
def addNewItem(warehouseNumber, itemNumber, description, value, shape, weight):
    #Updates overall capacity value as it is used to determine if there is enough space in any warehouse
    overallCapacity = warehouseData[WAREHOUSE_A][WAREHOUSE_SPACE] + warehouseData[WAREHOUSE_B][WAREHOUSE_SPACE] + \
                      warehouseData[WAREHOUSE_C][WAREHOUSE_SPACE] + warehouseData[WAREHOUSE_D][WAREHOUSE_SPACE]
    print("Adding " + str(description) + " to Warehouse " + WAREHOUSE_NAMES[warehouseNumber] + "...")
    if value > INSURED_MAX_SINGLE: #Print error and return 0 if value over 2000000000
        print("ERROR - Value is higher than the total insured value of a single warehouse")
        return 0
    if value > overallCapacity: #Print error and return 0 if impossible to store this item without removing others
        print("ERROR - Remaining storage capacity across all 4 warehouse is less than the current item value\n"
              "Some items will have to be removed to store this item")
        return 0
    if value == INSURED_MAX_SINGLE: #Prompts user that a whole warehouse is needed
        print("An entire warehouse will be needed to store this item")
        #identify_items_to_be_moved(warehouseNumber, itemNumber, description, value)
        return 0
    if (value > warehouseData[WAREHOUSE_A][WAREHOUSE_SPACE]) & (value > warehouseData[WAREHOUSE_B][WAREHOUSE_SPACE]) & \
       (value > warehouseData[WAREHOUSE_C][WAREHOUSE_SPACE]) & (value > warehouseData[WAREHOUSE_D][WAREHOUSE_SPACE]):
        print("No warehouse currently has space")#Tells user no space is available then calls identify_items_to_be_moved
        #identify_items_to_be_moved(warehouseNumber,itemNumber,description,value)
        return  0

    if warehouseData[warehouseNumber][WAREHOUSE_SPACE] >= value:
        warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][0] = itemNumber
        warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][1] = description
        warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][2] = value
        warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][3] = shape
        warehouse[warehouseNumber][warehouseData[warehouseNumber][WAREHOUSE_ITEMS]][4] = weight
        warehouseData[warehouseNumber][WAREHOUSE_SPACE] = warehouseData[warehouseNumber][WAREHOUSE_SPACE] - value
        warehouseData[warehouseNumber][WAREHOUSE_ITEMS] = warehouseData[warehouseNumber][WAREHOUSE_ITEMS] + 1
        print("Successfully added " + description + " to warehouse {}, Warehouse {} at {}% capacity"
              .format(WAREHOUSE_NAMES[warehouseNumber],WAREHOUSE_NAMES[warehouseNumber],
                      round((100 - warehouseData[warehouseNumber][WAREHOUSE_SPACE] / INSURED_MAX_SINGLE * 100), 2)))
    # else: #Identifys items to move if enough space overall but not in this warehouse
    #     #identify_items_to_be_moved(warehouseNumber, itemNumber, description, value)





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
                print("Adding item " + row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[4])
                addNewItem(WAREHOUSE_A, row[0], row[1], int(row[2]), row[3], row[4])





initialiseWarehouses(WAREHOUSE_A)
# initialiseWarehouses(WAREHOUSE_B)
# initialiseWarehouses(WAREHOUSE_C)
# initialiseWarehouses(WAREHOUSE_D)
printAllWarehouses()
# task1()
# # printAllWarehouses()