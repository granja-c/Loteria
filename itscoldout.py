def main():
  temps = input("Enter number of days and the high temperatures:")
  templist = temps.split(' ')
  tlist2 = [int(i) for i in templist]
  tlist3 = tlist2[1:]
  prev = tlist3[0]
  day = 1
  cdays = 0
  for i in tlist3[1:]:
    diff = prev - i
    day += 1
    if diff >= 15:
      print("Temperature drop (" + str(diff) + " degrees)  on day " + str(day))
      cdays += 1
    prev = i
  if cdays == 0:
    print("No cold days")
  pass

if __name__ == "__main__":
  main()