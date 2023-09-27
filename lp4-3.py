def main():
  egg = int(input("Enter the number of eggs purchased: "))
  doz = egg // 12
  ext = egg % 12
  price = 0.0
  
  if doz > 0 and doz < 4:
    price = 0.5 
  if doz >= 4 and doz < 6:
    price = 0.45
  if doz >= 6 and doz < 11:
    price = 0.4
  if doz >= 11:
    price = 0.35
    
  bill = doz * price + ext * (price * (1.0 / 12))
  print("The bill is equal to: $" + str(round(bill, 2)))
  pass

if __name__ == "__main__":
  main()