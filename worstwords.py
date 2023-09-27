def main():
  word = " "
  list = []
  list2 = []
  while word != "":
    word = str(input("Enter words: "))
    list = word.split(' ')
    list2.append(list)

if __name__ == "__main__":
  main()