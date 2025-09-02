'''Bill.py'''

def main():
    '''DocString'''
    net = int(input(""))
    service_charge = net*10/100
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    else:
        pass
    summary = float((net + service_charge)*107/100)
    print(f"{summary:.2f}")

main()
