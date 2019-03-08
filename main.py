'''
DADSA Assignment 2018-19 - ArtDealerV2
Ryan Williams - 17009972
'''
import csv
import random

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
WAREHOUSE_SPHERE = 4
WAREHOUSE_PYRAMID = 5
WAREHOUSE_SQUARE = 6

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
warehouseData = warehouseA = [[0 for x in range(7)] for y in range(NUMBER_OF_WAREHOUSES)]
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
            warehouseData[warehouseNumber][WAREHOUSE_ITEMS] -= 1  # Used so the value displayed is correct for the user
            # for x in range(warehouseData[warehouseNumber][WAREHOUSE_ITEMS]):  # Calculating Value of warehouse
            #     warehouseData[warehouseNumber][WAREHOUSE_VALUE] = warehouseData[warehouseNumber][WAREHOUSE_VALUE] + \ int(warehouse[warehouseNumber][x][2])
            # # Calculating space left in warehouse
            # warehouseData[warehouseNumber][WAREHOUSE_SPACE] = INSURED_MAX_SINGLE - warehouseData[warehouseNumber][
            #     WAREHOUSE_VALUE]


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
    #Calculate and prints the capacty of all warehouses combined
    overallCapacity = warehouseData[WAREHOUSE_A][WAREHOUSE_SPACE] + warehouseData[WAREHOUSE_B][WAREHOUSE_SPACE] + \
                      warehouseData[WAREHOUSE_C][WAREHOUSE_SPACE] + warehouseData[WAREHOUSE_D][WAREHOUSE_SPACE]
    print('Storage capacity across all 4 Warehouses is at {}%\n'.format(round((100 - overallCapacity/INSURED_MAX_MULTIPLE * 100),4)))

def task1():
    print("Task 1")


initialiseWarehouses(WAREHOUSE_A)
initialiseWarehouses(WAREHOUSE_B)
initialiseWarehouses(WAREHOUSE_C)
initialiseWarehouses(WAREHOUSE_D)
printAllWarehouses()