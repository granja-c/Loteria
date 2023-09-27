def main():
  shells = " "
  bweight = 0
  gList = []
  while shells != "":
    shells = str(input("Enter grams of seashells: "))
    gList.append(shells)
  gList2 = gList[:-1]
  gList3 = [int(i) for i in gList2]
  bucket = 1
  for i in gList3:
    if bweight + i > 100:
      bucket += 1
      bweight = 0 + i
    else:
      bweight += i
      

  
  print(bucket)
  pass

if __name__ == "__main__":
  main()