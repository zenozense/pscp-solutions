'''Temperature'''

def main():
    '''Temperature'''
    r = float(input())
    temp_type = str(input())
    target = str(input())

    if temp_type == 'C':
        rt = r # rt คือค่า C
    elif temp_type == 'F':
        rt = (r - 32) * 5 / 9
    elif temp_type == 'K':
        rt = r - 273.15
    elif temp_type == 'R':
        rt = (r - 491.67)/1.8

    if target == "C":
        print(f"{rt:.2f}")
    elif target == "F":
        print(f"{(rt * 9 / 5 + 32):.2f}")
    elif target == "K":
        print(f"{(rt + 273.15):.2f}")
    elif target == "R":
        print(f"{((rt + 273.15)*1.8):.2f}")

main()
