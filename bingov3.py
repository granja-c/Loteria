import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Bingo")
window.geometry("300x300")

numberlist = []
for i in range(1, 25):
  num = str(i)
  numberlist.append(num)

random.shuffle(numberlist)
options = []
for i in range(1, 25):
  options.append("B" + str(i))
  options.append("I" + str(i))
  options.append("N" + str(i))
  options.append("G" + str(i))
  options.append("O" + str(i))

print(options)


pink = "#ff86c4"
clickedbs = []

def clicked(button):
  # r1
  if button == button1:
    if button1['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b1")
    if clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button2:
    if button2['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b2")
    if clickedbs.count("b1") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button3:
    if button3['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b3")
    if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    
  if button == button4:
    if button4['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b4")
    if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button5:
    if button5['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b5")
    if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  # r2
  if button == button6:
    if button6['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b6")
    if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button7:
    if button7['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b7")
    if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button8:
    if button8['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b8")
    if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button9:
    if button9['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b9")
    if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button10:
    if button10['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b10")
    if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
  # r3
  if button == button11:
    if button11['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b11")
    if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button12:
    if button12['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b12")
    if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == freespace:
    button.configure(bg = pink)
    clickedbs.append("free")
    if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button14:
    if button14['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b14")
    if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button15:
    if button15['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b15")
    if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0:
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  # r4
  if button == button16:
    if button16['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b16")
    if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button17:
    if button17['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b17")
    if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button18:
    if button18['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b18")
    if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button19:
    if button19['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b19")
    if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button20:
    if button20['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b20")
    if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  # r5
  if button == button21:
    if button21['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b21")
    if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button22:
    if button22['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b22")
    if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button23:
    if button23['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b23")
    if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button24:
    if button24['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b24")
    if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
      
  if button == button25:
    if button25['text'] == testlbl['text']:
      button.configure(bg = pink)
      clickedbs.append("b25")
    if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")
    if clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0: 
      tk.messagebox.showinfo(title = "Bingo!", message = "You win!")


def next():
  a = random.choice(options)
  testlbl.configure(text = a)
  options.remove(a)
  


space1 = tk.Label(text="", height = 1, width = 2)
space1.grid(row = 0, column = 0)

Blabel = tk.Label(text="B", height = 2, width = 4)
Blabel.grid(row = 1, column = 1)
Ilabel = tk.Label(text="I", height = 2, width = 4)
Ilabel.grid(row = 1, column = 2)
Nlabel = tk.Label(text="N", height = 2, width = 4)
Nlabel.grid(row = 1, column = 3)
Glabel = tk.Label(text="G", height = 2, width = 4)
Glabel.grid(row = 1, column = 4)
Olabel = tk.Label(text="O", height = 2, width = 4)
Olabel.grid(row = 1, column = 5)

# r1
button1 = tk.Button(text="B" + numberlist[0], height= 4, width = 4, command = lambda: clicked(button1))
button1.grid(row = 2, column = 1)
button2 = tk.Button(text="I" + numberlist[1], height= 4, width = 4, command = lambda:clicked(button2))
button2.grid(row = 2, column = 2)
button3 = tk.Button(text="N" + numberlist[2], height= 4, width = 4, command = lambda:clicked(button3))
button3.grid(row = 2, column = 3)
button4 = tk.Button(text="G" + numberlist[3], height= 4, width = 4, command = lambda:clicked(button4))
button4.grid(row = 2, column = 4)
button5 = tk.Button(text="O" + numberlist[4], height= 4, width = 4, command = lambda:clicked(button5))
button5.grid(row = 2, column = 5)
# r2
button6 = tk.Button(text="B" + numberlist[5], height= 4, width = 4, command = lambda:clicked(button6))
button6.grid(row = 3, column = 1)
button7 = tk.Button(text="I" + numberlist[6], height= 4, width = 4, command = lambda:clicked(button7))
button7.grid(row = 3, column = 2)
button8 = tk.Button(text="N" + numberlist[7], height= 4, width = 4, command = lambda: clicked(button8))
button8.grid(row = 3, column = 3)
button9 = tk.Button(text="G" + numberlist[8], height= 4, width = 4, command = lambda:clicked(button9))
button9.grid(row = 3, column = 4)
button10 = tk.Button(text="O" + numberlist[9], height= 4, width = 4, command = lambda: clicked(button10))
button10.grid(row = 3, column = 5)
# r3
button11 = tk.Button(text="B" + numberlist[10], height= 4, width = 4, command = lambda:clicked(button11))
button11.grid(row = 4, column = 1)
button12 = tk.Button(text="I" + numberlist[11], height= 4, width = 4, command = lambda:clicked(button12))
button12.grid(row = 4, column = 2)
freespace = tk.Button(text="Free\nSpace", height= 4, width = 4, command = lambda: clicked(freespace))
freespace.grid(row = 4, column = 3)
button14 = tk.Button(text="G" + numberlist[12], height= 4, width = 4, command = lambda:clicked(button14))
button14.grid(row = 4, column = 4)
button15 = tk.Button(text="O" + numberlist[13], height= 4, width = 4, command = lambda: clicked(button15))
button15.grid(row = 4, column = 5)
# r4
button16 = tk.Button(text="B" + numberlist[14], height= 4, width = 4, command = lambda:clicked(button16))
button16.grid(row = 5, column = 1)
button17 = tk.Button(text="I" + numberlist[15], height= 4, width = 4, command = lambda:clicked(button17))
button17.grid(row = 5, column = 2)
button18 = tk.Button(text="N" + numberlist[16], height= 4, width = 4, command = lambda: clicked(button18))
button18.grid(row = 5, column = 3)
button19 = tk.Button(text="G" + numberlist[17], height= 4, width = 4, command = lambda:clicked(button19))
button19.grid(row = 5, column = 4)
button20 = tk.Button(text="O" + numberlist[18], height= 4, width = 4, command = lambda: clicked(button20))
button20.grid(row = 5, column = 5)
# r5
button21 = tk.Button(text="B" + numberlist[19], height= 4, width = 4, command = lambda:clicked(button21))
button21.grid(row = 6, column = 1)
button22 = tk.Button(text="I" + numberlist[20], height= 4, width = 4, command = lambda:clicked(button22))
button22.grid(row = 6, column = 2)
button23 = tk.Button(text="N" + numberlist[21], height= 4, width = 4, command = lambda: clicked(button23))
button23.grid(row = 6, column = 3)
button24 = tk.Button(text="G" + numberlist[22], height= 4, width = 4, command = lambda:clicked(button24))
button24.grid(row = 6, column = 4)
button25 = tk.Button(text="O" + numberlist[23], height= 4, width = 4, command = lambda: clicked(button25))
button25.grid(row = 6, column = 5)


random.shuffle(numberlist)
testlbl = tk.Label(text= random.choice(options), bg = pink, height = 6, width = 9)
testlbl.place(x = 360, y = 57)
nextbutton = tk.Button(text="next" , height= 2, width = 6, command = lambda: next())
nextbutton.place(x = 360, y = 160)


# bingobutton = tk.Button(text="bingo", height= 4, width = 4, command = lambda:ifclicked())
# bingobutton.place(x = 350, y = 250)


tk.mainloop()