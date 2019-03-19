def checkio(matrix):
    n = len(matrix)
    
    def rot_90_counterclockwise(matrix):
        return  list(reversed([list(row) for row in zip(*matrix)]))
    
    def horizontal(matrix):
        for row in matrix:
            for i in range(n-3):
                if row[i:i+4] == [row[i]]*4:
                    return True
        return False
    
    def vertical(matrix):
        temp = rot_90_counterclockwise(matrix)
        return horizontal(temp)
    
    def diagonal(matrix):
        for i in range(n-3):
            for j in range(n-3):
                if matrix[i][j]==matrix[i+1][j+1]==matrix[i+2][j+2]==matrix[i+3][j+3]:
                    return True
        return False
    
    def slash_diagonal(matrix):
        temp = rot_90_counterclockwise(matrix)
        return diagonal(temp)
    
    
    return horizontal(matrix) or vertical(matrix) or diagonal(matrix) or slash_diagonal(matrix)
    
        
        
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
