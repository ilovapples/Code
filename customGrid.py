def generate(cols: int, rows: int, fill=""):
    grid = []
    for _ in range(rows):
        grid.append([])
        for i in range(cols):
            grid[-1].append(fill)
    return grid
