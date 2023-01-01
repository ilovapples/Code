import time, os, platform

delay = 0.25


def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
boardSize = {
    "cols": 5,
    "rows": 5,
}
world = []
row = 0
for _ in range(boardSize['rows']):
    world.append([])
    for _ in range(boardSize['cols']):
        world[row].append(". ")
    row += 1

def findNeighbors(y, x):
    neighbors = ["", "", "", "", "", "", "", "", ""]
    
    # Neighbor 1
    try:
        neighbors[0] = world[y-1][x-1]
    except IndexError:
        neighbors[0] = ". "
    
    # Neighbor 2
    try:
        neighbors[1] = world[y-1][x]
    except IndexError:
        neighbors[1] = ". "
    
    # Neighbor 3
    try:
        neighbors[2] = world[y-1][x+1]
    except IndexError:
        neighbors[2] = ". "
    
    # Neighbor 4
    try:
        neighbors[3] = world[y][x-1]
    except IndexError:
        neighbors[3] = ". "
    
    # Neighbor 5
    try:
        neighbors[4] = world[y][x]
    except IndexError:
        neighbors[4] = ". "
    
    # Neighbor 6
    try:
        neighbors[5] = world[y][x+1]
    except IndexError:
        neighbors[5] = ". "
    
    # Neighbor 7
    try:
        neighbors[6] = world[y+1][x-1]
    except IndexError:
        neighbors[6] = ". "
    
    # Neighbor 8
    try:
        neighbors[7] = world[y+1][x]
    except IndexError:
        neighbors[7] = ". "
    
    # Neighbor 9
    try:
        neighbors[8] = world[y+1][x+1]
    except IndexError:
        neighbors[8] = ". "
    
    
    return neighbors.count("# ")

def killOrNot(y, x):
    global world
    if findNeighbors(y, x) == 0:
        world[y][x] = ". "
    else:
        if world[y][x] == "# ":
            if findNeighbors(y, x) < 2 or findNeighbors(y, x) > 3:
                world[y][x] = ". "
            elif findNeighbors(y, x) == 2 or findNeighbors(y, x) == 3:
                world[y][x] = "# "
            
        elif world[y][x] == ". ":
            if findNeighbors(y, x) < 2 or findNeighbors(y, x) > 3:
                world[y][x] = ". "
            elif findNeighbors(y, x) == 3:
                world[y][x] = "# "

 
def printWorld(iterate: int):
    print(f"Current Iteration: {str(iterate)}")
    world[2][2] = '# '
    row = 0
    col = 0
    toPrint = ""
    for _ in range(len(world)):
        for _ in range(len(world[row])):
            toPrint += world[row][col]
            col += 1
        col = 0
        row += 1
        toPrint += "\n"
    
    print(toPrint)

    
def startGame(times):
    iteration = 0
    if times == 0:
        while True:
            printWorld(iteration)
            x = 0
            y = 0
            for _ in range(len(world)):
                for _ in range(len(world[y])):
                    killOrNot(y, x)
                    x += 1
                x = 0
                y += 1
            iteration += 1
            time.sleep(delay)
            clear()
    else:
        for _ in range(times):
            printWorld(iteration)
            x = 0
            y = 0
            for _ in range(len(world)):
                for _ in range(len(world[y])):
                    killOrNot(y, x)
                    x += 1
                x = 0
                y += 1
            iteration += 1
            time.sleep(delay)

startGame(0)
# print(world)