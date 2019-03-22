def checkio(matrix):
    def getMatrixMinor(matrix,i,j):
        return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

    def getMatrixDeternminant(matrix):
        #base case for 2x2 matrix
        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        determinant = 0
        for c in range(len(matrix)):
            determinant += ((-1)**c)*matrix[0][c]*getMatrixDeternminant(getMatrixMinor(matrix,0,c))
        return determinant
    
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        return getMatrixDeternminant(matrix)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4, 3], [6, 3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'
    print('passed all tests')
