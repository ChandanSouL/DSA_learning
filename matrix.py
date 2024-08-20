arr = [[1,2,3],[4,5,6],[7,8,9]]
#accessing an element
#print(a[0][3])
n = 3
m = 3
for i in range(0,n):
    for j in range(0,m):
        print(arr[i][j],end=" ")


#searching in a Matrix
def searchInMatrix(arr,x):
    for i in range(0,n):
        for j in range(0,m):
            if (arr[i][j] == x):
                return True
    return False

##set zero in a matrix
# [1,1,1]         [1,0,1]
# [1,0,1]  --->   [0,0,0]
# [1,1,1]         [1,0,1]
def setZeroInMatrix(matrix):
    n = len(matrix)       #length of row
    m = len(matrix[0])    #length of column
    row = [0]*n 
    column = [0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                column[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or column[j]:
                matrix[i][j]=0
    
    return matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroInMatrix(matrix))

#Transpose of a matrix
def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transpose1 = []
    for i in range(m):
        newarray = []
        for j in range(n):
            newarray.append(matrix[j][i])
        transpose1.append(newarray)
    return transpose1


    
