def spiral_matrix(size):
    """
    Creates a matrix with the given size and populates it with numbers in a spiral order

    :param int size: Size of the matrix
    :return list[list[int]]: Spiral matrix
    """
    direction = "right"
    count = 1
    total_count = size ** 2
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    x = 0
    y = 0
    while count <= total_count:
        if direction == "right":
            for _ in range(size):
                spiral[x][y] = count
                count += 1
                y += 1
            y -= 1
            x += 1
            direction = "down"
            size -= 1
        elif direction == "down":
            for _ in range(size):
                spiral[x][y] = count
                count += 1
                x += 1
            x -= 1
            y -= 1
            direction = "left"
        elif direction == "left":
            for _ in range(size):
                spiral[x][y] = count
                count += 1
                y -= 1
            y += 1
            x -= 1
            direction = "up"
            size -= 1
        elif direction == "up":
            for _ in range(size):
                spiral[x][y] = count
                count += 1
                x -= 1
            x += 1
            y += 1
            direction = "right"
    return spiral