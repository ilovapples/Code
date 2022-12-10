def generate(cols, rows):
    customBoard = []
    for _ in range(rows):
        customBoard.append([])
        for _ in range(cols):
            customBoard[-1].append("_")
    return customBoard