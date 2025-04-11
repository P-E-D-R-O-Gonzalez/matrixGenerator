#################################################################################
# Matrix Generator                                                              #
# by Pedro Gonzalez                                                             #
# this generators a matrice of random numbers to create practice problems.      #
# Not all matrices will have valid solutions, but this is just for practice.    #
#################################################################################
import random

# matrix
matrix = []

def generateMatrix(rows=3, cols=3):
    # fill in matrix
    for i in range(rows):
        # generates a row of random numbers
        randomRow = random.sample(range(1, 10), cols)  # range can be adjusted
        # and inserts it into the matrix
        matrix.insert(i,randomRow)

def printMatrix(matrix):
    # prints the matrix
    for row in matrix:
        print(row)


def main():
    # adjust the size of the matrix here 3 by 3 is default
    generateMatrix(3,4)
    printMatrix(matrix)

# start of program
main()