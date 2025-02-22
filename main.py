board=[[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

def display(bo):
    for i in range(9):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - ")
        for j in range(9):
            if j%3==0 and j!=0:
                print(" | ", end="")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ", end="")
#^displays the board; uses integer division to determine when to print the horizontal and vertical lines

def findEmpty(bo):
    for r in range(9):
        for c in range(9):
            if bo[r][c]==0:
                return r,c
    return False
#^returns the row and column of the first empty cell

def checkValidGrid(bo, row, col):
    count=0
    if row // 3 == 0 and col // 3 == 0:
        for r in range(0, 3):
            for c in range(0, 3):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 1 and col // 3 == 0:
        for r in range(3, 6):
            for c in range(0, 3):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 2 and col // 3 == 0:
        for r in range(6, 9):
            for c in range(0, 3):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 0 and col // 3 == 1:
        for r in range(0, 3):
            for c in range(3, 6):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 1 and col // 3 == 1:
        for r in range(3, 6):
            for c in range(3, 6):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 2 and col // 3 == 1:
        for r in range(6, 9):
            for c in range(3, 6):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 0 and col // 3 == 2:
        for r in range(0, 3):
            for c in range(6, 9):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 1 and col // 3 == 2:
        for r in range(3, 6):
            for c in range(6, 9):
                if bo[row][col] == bo[r][c]:
                    count += 1
    elif row // 3 == 2 and col // 3 == 2:
        for r in range(6, 9):
            for c in range(6, 9):
                if bo[row][col] == bo[r][c]:
                    count += 1

    if count <= 1:
        return True
    return False

def checkValid(bo, r, c):
    count=0
    for i in range(9):
        if (bo[r][i]==bo[r][c]) or (bo[i][c]==bo[r][c]):
            count+=1
        if checkValidGrid(bo, r, c)==False:
            count+=1
    if count<=1:
        return True
    return False

def solve(bo):
    row=(findEmpty(bo))[0]
    col=(findEmpty(bo))[1]
    while findEmpty(bo)!=False:
        for i in range(1, 10):
            bo[row][col]=i
            valid=checkValid(bo, row, col)
            if valid==True:
                solve(bo)
            else:
                bo[row][col]=0
    return bo

print(solve(board))