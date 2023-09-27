pnd = int(input("pounds: "))
shill = int(input("shillings: "))
pnc = int(input("pence: "))

dec = round((((shill * 12 + pnc) * (100 / 240)) * 0.01), 2)

print(pnd + dec)