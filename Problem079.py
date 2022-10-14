
with open("p079_keylog.txt") as f:
    first = []
    middle = []
    last = []
    list1 = set()
    list2 = set()

    for line in f:
        first.append(line[0])
        middle.append(line[1])
        last.append(line[2])
        if line[1] == "1":
            list1.add(line[2])
        if line[1] == "2":
            list2.add(line[2])

print(first, "\n", middle, "\n", last, "\n", list1, list2)

#{'6', '1', '2', '7', '3', '8'} 1 2 3 6 7 8
#{'6', '1', '9', '2', '8', '3'} 1 2 3 6 8 9
#{'0', '6', '2', '9', '1', '8'} 0 1 2 6 8 9

#{'3', '9', '6', '2', '1'} after 7
#{'8', '9', '6', '2', '1'} before 0
# 1 6 8 after first 3   ->   2 6 8 after first 1, 2 8 9 after first 6
#                       ->   8 9 after first 2, 9 after first 8 -> 16289
# 2 6 7 8 before first 9  ^done
# 7 before first 3
# 1 6 after last 3
# 0 after last 9, 0 9 after last 8, 0 2 8 9 after last 6
# 0 8 9 after last 2, 0 6 8 9 after last 1    ->   162890 note overlap above


# 73162890

#Coding is cringe, just do a little guess work.
