n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""

"""