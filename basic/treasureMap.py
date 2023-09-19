row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]
move = int(input("Where do you want to put the treasure? "))
column = move % 10
row = move // 10
map[row - 1][column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")