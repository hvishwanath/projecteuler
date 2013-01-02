def transpose(matrix):
    """ Returns transpose of a valid matrix"""
    row = len(matrix)
    col = len(matrix[0])
    rmatrix = []
    for i in range(0,col):
        rmatrix.append([])

    for i in range(0,row):
        for j in range(0,col):
            #Get the row element from matrix
            #and populate in the column of rmatrix
            rmatrix[j].append(matrix[i][j])

    return rmatrix

def swapRows(matrix,max_count, swapFromTop = False):
    """ Swap the rows the supplied matrix upto max_count number of swaps
    Algorithm :
    Swaps are performed in the following fashion.
    If swapFromTop : Swapping begins from 0th row
    Else: Swapping begins from last row
    While rows are not out of boundary :
        swap 0 with 1, 2 with 3 and so on.
        if number of swaps is greater than max_count - break
    """
    
    numberOfSwaps = 0
    swapIndex = 0
    maxRows = len(matrix) - 1

    if(swapFromTop):
        swapIndex = 0
    else:
        swapIndex = maxRows
        

        
    for i in range(0,max_count):

        if swapFromTop:

            if (swapIndex > maxRows - 1):
                break
            
            temp = matrix[swapIndex]
            matrix[swapIndex] = matrix[swapIndex + 1]
            matrix[swapIndex + 1] = temp
            swapIndex = swapIndex + 2

        else:
            if (swapIndex < 1):
                break
            temp = matrix[swapIndex]
            matrix[swapIndex] = matrix[swapIndex - 1]
            matrix[swapIndex - 1] = temp
            swapIndex = swapIndex - 2

    return matrix                

def swapColumns(matrix,max_count, swapFromLeft = False):
    """ Swap the Columns the supplied matrix upto max_count number of swaps
    Algorithm :
    Get a transpose of the matrix
    Swap the rows
    Get a transpose of the matrix again and return it
    """

    matrix = transpose(matrix)
    matrix = swapRows(matrix, max_count, swapFromLeft)
    matrix = transpose(matrix)
    return matrix


def getUpperTriangleElements(matrix):
    """Returns the upper triangle elements of a square matrix.
    Diagonal elements are ignored"""
    li = []
    row = col = len(matrix)
    for i in range(0,row):
        for j in range(i+1,col):
            li.append(matrix[i][j])
    return li

def getLowerTriangleElements(matrix):
    """Returns the lower triangle elements of a square matrix.
    Diagonal elements are ignored"""
    li = []
    row = col = len(matrix)
    for i in range(0,row):
        for j in range(0,i):
            li.append(matrix[i][j])
    return li

def strMatrix(matrix):
    """ Return string representation of the passed matrix """
    row = col = len(matrix)
    rval = ''
    for i in range(0,row):
        for j in range(0,col):
            rval = rval + str(matrix[i][j]) + ' '
        rval = rval + '\n'
    return rval
    
def printMatrix(matrix):
    """Prints a valid Matrix"""
    print strMatrix(matrix)