import tkinter as tk
import random

window = tk.Tk()
window.title("Bingo")
window.geometry("300x300")

numberlist = []
for i in range(1, 100):
  num = str(i)
  numberlist.append(num)
random.shuffle(numberlist)


button1 = tk.Button(text="Button1", height= 4, width = 5)
button1.grid(row = 0, column = 0)
button2 = tk.Button(text="Button2", height= 4, width = 5)
button2.grid(row = 0, column = 1)


tk.mainloop()