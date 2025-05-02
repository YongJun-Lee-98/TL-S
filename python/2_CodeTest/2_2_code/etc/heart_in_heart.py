def is_heart(row, col):
    return (
        (row == 1 and col in {1, 2, 6, 7}) or
        (row == 2 and col in {0, 1, 2, 3, 5, 6, 7, 8}) or
        (3 <= row <= 4) or
        (row ==5 and 1 <= col <= 7) or
        (row == 6 and 2 <= col <= 6) or
        (row == 7 and 3 <= col <= 5) or
        (row == 8 and col == 4)
        )

rows=9
cols=9

for row in range(rows):
    for col in range(cols):
        print('♥' if is_heart(row, col) else ' ', end='')
    print()