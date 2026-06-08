# LIST COMPREHENSION

# squares = []
# for i in range(10):
#     squares.append(i * i)

# x1, y1     x2, y2
# (1, 2)     (3, 4)

# 1, 3 ---- 1, 4 ---- 2, 3 ---- 2, 4

# lst = []
# for a in (1, 2):
#     for b in (3 , 4):
#         lst.append( (a,b) )

# Manipulation takes 1 line
# copy_of_a_list = [ (a, b) for a in (1, 2) for b in (3, 4) ]

# print(copy_of_a_list)


# all ( LIST ) -----> True -- ONLY IF ALL ELEMENTS INSIDE ARE TRUE
#              -----> False


username = "Abhishek Karmakar Prasad Nath"

parts = username.split()

c = True
for p in parts:
    if not p.isalpha():
        c = False

print(all ([p.isalpha() for p in parts]) )

from pathlib import Path
print(Path.cwd())