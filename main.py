board=[[8,0,0,4,0,6,0,0,7],
    [0,0,0,0,0,0,4,0,0],
    [0,1,0,0,0,0,6,5,0],
    [5,0,9,0,3,0,7,8,0],
    [0,0,0,0,7,0,0,0,0],
    [0,4,8,0,2,0,1,0,3],
    [0,5,2,0,0,0,0,9,0],
    [0,0,1,0,0,0,0,0,0],
    [3,0,0,9,0,2,0,0,5]]

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



# def checkValidGrid(bo, row, col):
#     count=0
#     if row // 3 == 0 and col // 3 == 0:
#         for r in range(0, 3):
#             for c in range(0, 3):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 1 and col // 3 == 0:
#         for r in range(3, 6):
#             for c in range(0, 3):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 2 and col // 3 == 0:
#         for r in range(6, 9):
#             for c in range(0, 3):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 0 and col // 3 == 1:
#         for r in range(0, 3):
#             for c in range(3, 6):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 1 and col // 3 == 1:
#         for r in range(3, 6):
#             for c in range(3, 6):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 2 and col // 3 == 1:
#         for r in range(6, 9):
#             for c in range(3, 6):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 0 and col // 3 == 2:
#         for r in range(0, 3):
#             for c in range(6, 9):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 1 and col // 3 == 2:
#         for r in range(3, 6):
#             for c in range(6, 9):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1
#     elif row // 3 == 2 and col // 3 == 2:
#         for r in range(6, 9):
#             for c in range(6, 9):
#                 if bo[row][col] == bo[r][c]:
#                     count += 1

#     if count <= 1:
#         return True
#     return False

# def checkValid(bo, r, c):
#     count=0
#     for i in range(9):
#         if (bo[r][i]==bo[r][c]) or (bo[i][c]==bo[r][c]):
#             count+=1
#         if checkValidGrid(bo, r, c)==False:
#             count+=1
#     if count<=1:
#         return True
#     return False

# def solve(bo):
    # row=(findEmpty(bo))[0]
    # col=(findEmpty(bo))[1]
    # while findEmpty(bo)!=False:
    #     for i in range(1, 10):
    #         bo[row][col]=i
    #         valid=checkValid(bo, row, col)
    #         if valid==True:
    #             solve(bo)
    #         else:
    #             bo[row][col]=0
    # return bo



def checkValid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1]!=i:
            return False

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[0]!=i:
            return False

    # Check 3x3 grid
    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if bo[i][j]==num and (i, j)!=pos:
                return False
                
    return True

def solve(bo):
    find=findEmpty(bo)
    if not find:
        return True  # No empty cells left, puzzle solved
    else:
        row, col=find

    for i in range(1, 10):
        if checkValid(bo, i, (row, col)):
            bo[row][col]=i

            if solve(bo):
                return bo

            bo[row][col]=0  # Reset the cell and backtrack

    return False  # Trigger backtracking

# # Print the solved board
# if solve(board):
#     display(board)
# else:
#     print("No solution exists")


def insertNum(number, row, col):
    board[row][col]=number

def displayErrors(bo, solvedBo):
    for r in range(9):
        for c in range(9):
            if bo[r][c]!=solvedBo[r][c] and bo[r][c]!=0:
                print("Error at row "+str(r)+" and column "+str(c)+".")

def play(board):
    display(board)
    empty=[row[:] for row in board]
    solved=solve(empty)
    done=False
    while done==False:
        choice = input("Do you want to A: enter a number, B: check your inputs, or C: view the solution?")
        if choice=="A" or choice=="a":
            num=int(input("Enter number (1 to 9): "))
            x=int(input("Enter x coordinate (0 to 8): "))
            y=int(input("Enter y coordinate (0 to 8): "))
            insertNum(num, x , y)
            display(board)
        elif choice=="B" or choice=="b":
            displayErrors(board, solved)
        elif choice=="C" or choice=="c":
            display(solved)
            done=True
        else:
            print("Invalid input")

play(board)