#import time
#start = time.time()

ans = 0

def solve(grid):
    solved = False
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for row in range(9):
        for col in range(9):
            check = int(grid[row][col])
            if check != 0:
                rows[row].add(check)
                cols[col].add(check)
                boxes[row//3*3 + col//3].add(check)
    def backtrack(row, col):
        if row == 9:
            solved = True
            return grid
        if int(grid[row][col]) != 0:
            backtrack(row + (row+1) // 9, (col+1) % 9)
        else:
            for entry in range(1,10):
                if str(entry) not in rows[row] and str(entry) not in cols[col] and str(entry) not in boxes[row//3*3 + col//3]:
                    rows[row].add(entry)
                    cols[col].add(entry)
                    boxes[row//3*3 + col//3].add(entry)
                    grid[row].replace("0",str(entry),1)
                    backtrack(row + (row+1) // 9, (col+1) % 9)
                    if solved == False:
                        rows[row].remove(entry)
                        cols[col].remove(entry)
                        boxes[row//3*3 + col//3].remove(entry)
                        grid[row].replace(str(entry),"0",1)
    backtrack(0,0)

with open("p096_sudoku.txt") as f:
    grid = []
    line_num = 0
    for line in f:
        if line[0:4] != "Grid":
            grid.append(line[:9])
            line_num += 1
            if line_num == 9:
                ans += int(solve(grid)[0][:2])
                grid = []
                line_num = 0

print(ans)

#end = time.time()
#print((end-start)*(10**3), "ms")

#Стилл доесн'т шорк. Лорд кношс шчй.
