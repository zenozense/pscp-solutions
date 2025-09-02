"""dogstring"""

def main():
    """eiei"""
    color = str(input())
    maxgi = int(input())
    start = 0

    if color == "R":
        start = 0
    elif color == "G":
        start = 1
    elif color == "B":
        start = 2

    L = ["Red", "Green", "Blue"]
    for i in range(start, maxgi+start, 1):
        print(L[i%3], end=" ")

main()
