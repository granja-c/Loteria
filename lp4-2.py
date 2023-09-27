def main():
  kg = int(input("Enter package weight in kg: "))
  leng = int(input("Enter package length in cm: "))
  wid = int(input("Enter package width in cm: "))
  height = int(input("Enter package height in cm: "))
  vol = leng * wid * height
  if kg > 27 and vol > 100000:
    print("Too heavy and too large.")
  elif kg > 27:
    print("Too heavy.")
  elif vol > 100000:
    print("Too large.")
  pass

if __name__ == "__main__":
  main()
