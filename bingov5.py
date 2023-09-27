# make 2nd board, shuffle nl again before making other board 
import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image

numberlist = []
for i in range(1, 25):
  num = str(i)
  numberlist.append(num)
random.shuffle(numberlist)
letterlist = ["B", "I", "N", "G", "O"]
pink = "#ff86c4"
red = "#eb4034"
clickedbs = []
options = []


for i in range(1, 25):
  options.append("B" + str(i))
  options.append("I" + str(i))
  options.append("N" + str(i))
  options.append("G" + str(i))
  options.append("O" + str(i))

class Game(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.geometry("300x300")
    self.title("Bingo")
    

    space1 = tk.Label(self, text="", height = 1, width = 2)
    space1.grid(row = 0, column = 0)

    Blabel = tk.Label(self, text="B", height = 2, width = 4)
    Blabel.grid(row = 1, column = 1)
    Ilabel = tk.Label(self,text="I", height = 2, width = 4)
    Ilabel.grid(row = 1, column = 2)
    Nlabel = tk.Label(self,text="N", height = 2, width = 4)
    Nlabel.grid(row = 1, column = 3)
    Glabel = tk.Label(self,text="G", height = 2, width = 4)
    Glabel.grid(row = 1, column = 4)
    Olabel = tk.Label(self, text="O", height = 2, width = 4)
    Olabel.grid(row = 1, column = 5)

    button1 = tk.Button(self, text="B" + numberlist[0], height= 4, width = 4, command = lambda: clicked(self, button1))
    button1.grid(row = 2, column = 1)
    button2 = tk.Button(self, text="I" + numberlist[1], height= 4, width = 4, command = lambda:clicked(self, button2))
    button2.grid(row = 2, column = 2)
    button3 = tk.Button(self, text="N" + numberlist[2], height= 4, width = 4, command = lambda:clicked(self, button3))
    button3.grid(row = 2, column = 3)
    button4 = tk.Button(self, text="G" + numberlist[3], height= 4, width = 4, command = lambda:clicked(self, button4))
    button4.grid(row = 2, column = 4)
    button5 = tk.Button(self, text="O" + numberlist[4], height= 4, width = 4, command = lambda:clicked(self, button5))
    button5.grid(row = 2, column = 5)

    button6 = tk.Button(self, text="B" + numberlist[5], height= 4, width = 4, command = lambda:clicked(self, button6))
    button6.grid(row = 3, column = 1)
    button7 = tk.Button(self, text="I" + numberlist[6], height= 4, width = 4, command = lambda:clicked(self, button7))
    button7.grid(row = 3, column = 2)
    button8 = tk.Button(self, text="N" + numberlist[7], height= 4, width = 4, command = lambda: clicked(self, button8))
    button8.grid(row = 3, column = 3)
    button9 = tk.Button(self, text="G" + numberlist[8], height= 4, width = 4, command = lambda:clicked(self, button9))
    button9.grid(row = 3, column = 4)
    button10 = tk.Button(self, text="O" + numberlist[9], height= 4, width = 4, command = lambda: clicked(self, button10))
    button10.grid(row = 3, column = 5)
    
    button11 = tk.Button(self, text="B" + numberlist[10], height= 4, width = 4, command = lambda:clicked(self, button11))
    button11.grid(row = 4, column = 1)
    button12 = tk.Button(self, text="I" + numberlist[11], height= 4, width = 4, command = lambda:clicked(self, button12))
    button12.grid(row = 4, column = 2)
    freespace = tk.Button(self, text="Free\nSpace", height= 4, width = 4, command = lambda: clicked(self, freespace))
    freespace.grid(row = 4, column = 3)
    button14 = tk.Button(self, text="G" + numberlist[12], height= 4, width = 4, command = lambda:clicked(self, button14))
    button14.grid(row = 4, column = 4)
    button15 = tk.Button(self, text="O" + numberlist[13], height= 4, width = 4, command = lambda: clicked(self, button15))
    button15.grid(row = 4, column = 5)

    button16 = tk.Button(self, text="B" + numberlist[14], height= 4, width = 4, command = lambda:clicked(self, button16))
    button16.grid(row = 5, column = 1)
    button17 = tk.Button(self, text="I" + numberlist[15], height= 4, width = 4, command = lambda:clicked(self, button17))
    button17.grid(row = 5, column = 2)
    button18 = tk.Button(self, text="N" + numberlist[16], height= 4, width = 4, command = lambda: clicked(self, button18))
    button18.grid(row = 5, column = 3)
    button19 = tk.Button(self, text="G" + numberlist[17], height= 4, width = 4, command = lambda:clicked(self, button19))
    button19.grid(row = 5, column = 4)
    button20 = tk.Button(self, text="O" + numberlist[18], height= 4, width = 4, command = lambda: clicked(self, button20))
    button20.grid(row = 5, column = 5)

    button21 = tk.Button(self, text="B" + numberlist[19], height= 4, width = 4, command = lambda: clicked(self, button21))
    button21.grid(row = 6, column = 1)
    button22 = tk.Button(self, text="I" + numberlist[20], height= 4, width = 4, command = lambda: clicked(self, button22))
    button22.grid(row = 6, column = 2)
    button23 = tk.Button(self, text="N" + numberlist[21], height= 4, width = 4, command = lambda: clicked(self, button23))
    button23.grid(row = 6, column = 3)
    button24 = tk.Button(self, text="G" + numberlist[22], height= 4, width = 4, command = lambda: clicked(self, button24))
    button24.grid(row = 6, column = 4)
    button25 = tk.Button(self, text="O" + numberlist[23], height= 4, width = 4, command = lambda: clicked(self, button25))
    button25.grid(row = 6, column = 5)

    #

    space2 = tk.Label(self, text="", height = 1, width = 9)
    space2.grid(row = 0, column = 6)
    space3 = tk.Label(self, text="", height = 1, width = 9)
    space3.grid(row = 0, column = 7)
    space4 = tk.Label(self, text="", height = 1, width = 7)
    space4.grid(row = 0, column = 8)

    Blabel2 = tk.Label(self, text="B", height = 2, width = 4)
    Blabel2.grid(row = 1, column = 8)
    Ilabel2 = tk.Label(self,text="I", height = 2, width = 4)
    Ilabel2.grid(row = 1, column = 9)
    Nlabel2 = tk.Label(self,text="N", height = 2, width = 4)
    Nlabel2.grid(row = 1, column = 10)
    Glabel2 = tk.Label(self,text="G", height = 2, width = 4)
    Glabel2.grid(row = 1, column = 11)
    Olabel2 = tk.Label(self, text="O", height = 2, width = 4)
    Olabel2.grid(row = 1, column = 12)
    
    random.shuffle(numberlist)
    
    button26 = tk.Button(self, text="B" + numberlist[0], height= 4, width = 4)
    button26.grid(row = 2, column = 8)
    button27 = tk.Button(self, text="I" + numberlist[1], height= 4, width = 4)
    button27.grid(row = 2, column = 9)
    button28 = tk.Button(self, text="N" + numberlist[2], height= 4, width = 4)
    button28.grid(row = 2, column = 10)
    button29 = tk.Button(self, text="G" + numberlist[3], height= 4, width = 4)
    button29.grid(row = 2, column = 11)
    button30 = tk.Button(self, text="O" + numberlist[4], height= 4, width = 4)
    button30.grid(row = 2, column = 12)

    button31 = tk.Button(self, text="B" + numberlist[5], height= 4, width = 4)
    button31.grid(row = 3, column = 8)
    button32 = tk.Button(self, text="I" + numberlist[6], height= 4, width = 4)
    button32.grid(row = 3, column = 9)
    button33 = tk.Button(self, text="N" + numberlist[7], height= 4, width = 4)
    button33.grid(row = 3, column = 10)
    button34 = tk.Button(self, text="G" + numberlist[8], height= 4, width = 4)
    button34.grid(row = 3, column = 11)
    button35 = tk.Button(self, text="O" + numberlist[9], height= 4, width = 4)
    button35.grid(row = 3, column = 12)

    button36 = tk.Button(self, text="B" + numberlist[10], height= 4, width = 4)
    button36.grid(row = 4, column = 8)
    button37 = tk.Button(self, text="I" + numberlist[11], height= 4, width = 4)
    button37.grid(row = 4, column = 9)
    freespace2 = tk.Button(self, bg = pink, text="Free\nSpace", height= 4, width = 4)
    freespace2.grid(row = 4, column = 10)
    button39 = tk.Button(self, text="G" + numberlist[12], height= 4, width = 4)
    button39.grid(row = 4, column = 11)
    button40 = tk.Button(self, text="O" + numberlist[13], height= 4, width = 4)
    button40.grid(row = 4, column = 12)
    
    button41 = tk.Button(self, text="B" + numberlist[14], height= 4, width = 4)
    button41.grid(row = 5, column = 8)
    button42 = tk.Button(self, text="I" + numberlist[15], height= 4, width = 4)
    button42.grid(row = 5, column = 9)
    button43 = tk.Button(self, text="N" + numberlist[16], height= 4, width = 4)
    button43.grid(row = 5, column = 10)
    button44 = tk.Button(self, text="G" + numberlist[17], height= 4, width = 4)
    button44.grid(row = 5, column = 11)
    button45 = tk.Button(self, text="O" + numberlist[18], height= 4, width = 4)
    button45.grid(row = 5, column = 12)

    button46 = tk.Button(self, text="B" + numberlist[19], height= 4, width = 4)
    button46.grid(row = 6, column = 8)
    button47 = tk.Button(self, text="I" + numberlist[20], height= 4, width = 4)
    button47.grid(row = 6, column = 9)
    button48 = tk.Button(self, text="N" + numberlist[21], height= 4, width = 4)
    button48.grid(row = 6, column = 10)
    button49 = tk.Button(self, text="G" + numberlist[22], height= 4, width = 4)
    button49.grid(row = 6, column = 11)
    button50 = tk.Button(self, text="O" + numberlist[23], height= 4, width = 4)
    button50.grid(row = 6, column = 12)
    
    n = random.choice(options)
    options.remove(n)
    testlbl = tk.Label(self, text= n, bg = pink, height = 6, width = 9)
    testlbl.place(x = 360, y = 57)
    nextbutton = tk.Button(self, text="next" , height= 2, width = 6, command = lambda: next())
    nextbutton.place(x = 360, y = 160)

    numButtons = 3
    allBtnImages = ["index.jpg", "orange.png", "Banana-Single.jpg"]
    global imageChoices, buttonImages
    imageChoices = [i for i in allBtnImages]
    buttonImages = [0]*numButtons
    def getRandomImage(size, buttonNumber):
      global buttonImages, imageChoices
      indx = random.randint(0, len(imageChoices)-1)
      choice = imageChoices.pop(indx)  # Only select image once and remove
      img = Image.open(choice)
      img.putalpha(127)
      img = img.resize(size)
      pic = ImageTk.PhotoImage(img)
      buttonImages[buttonNumber] = pic
      return buttonImages[buttonNumber]

    
    def clicked(self, button):
      if button == button1:
        if button1['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b1")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button2:
        if button2['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b2")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button3:
        if button3['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b3")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button4:
        if button4['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b4")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button5:
        if button5['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b5")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 and clickedbs.count("b5") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
          
      if button == button6:
        if button6['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b6")
        if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button7:
        if button7['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b7")
        if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button8:
        if button8['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b8")
        if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button9:
        if button9['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b9")
        if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button10:
        if button10['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b10")
        if clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")

      if button == button11:
        if button11['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b11")
        if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button12:
        if button12['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b12")
        if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == freespace:
        button.configure(bg = pink)
        clickedbs.append("free")
        if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button14:
        if button14['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b14")
        if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button15:
        if button15['text'] == testlbl['text']:
          button15.configure(bg = pink)
          clickedbs.append("b15")
        if clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")

      if button == button16:
        if button16['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b16")
        if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button17:
        if button17['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b17")
        if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button18:
        if button18['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b18")
        if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button19:
        if button19['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b19")
        if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button20:
        if button20['text'] == testlbl['text']:
          button.configure(bg = pink)
          clickedbs.append("b20")
        if clickedbs.count("b16") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b20") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")

      if button == button21:
        if button21['text'] == testlbl['text']:
          button21.configure(bg = pink)
          clickedbs.append("b21")
        if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0 and clickedbs.count("b21") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b21") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button22:
        if button22['text'] == testlbl['text']:
          button22.configure(bg = pink)
          clickedbs.append("b22")
        if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b17") > 0 and clickedbs.count("b22") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button23:
        if button23['text'] == testlbl['text']:
          button23.configure(bg = pink)
          clickedbs.append("b23")
        if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b18") > 0 and clickedbs.count("b23") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button24:
        if button24['text'] == testlbl['text']:
          button24.configure(bg = pink)
          clickedbs.append("b24")
        if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b24") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
      if button == button25:
        if button25['text'] == testlbl['text']:
          button25.configure(bg = pink)
          clickedbs.append("b25")
        if clickedbs.count("b21") > 0 and clickedbs.count("b22") > 0 and clickedbs.count("b23") > 0 and clickedbs.count("b24") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b5") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b20") > 0 and clickedbs.count("b25") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("free") > 0 and clickedbs.count("b19") > 0 and clickedbs.count("b25") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You win!")
        
    clickedbs.append("free2")  
    def next():
      a = random.choice(options)
      testlbl.configure(text = a)
      options.remove(a)
      
      if button26['text'] == testlbl['text']:
        button26.configure(bg = pink)
        clickedbs.append("b26")
      if button27['text'] == testlbl['text']:
        button27.configure(bg = pink)
        clickedbs.append("b27")
      if button28['text'] == testlbl['text']:
        button28.configure(bg = pink)
        clickedbs.append("b28")
      if button29['text'] == testlbl['text']:
        button29.configure(bg = pink)
        clickedbs.append("b29")
      if button30['text'] == testlbl['text']:
        button30.configure(bg = pink)
        clickedbs.append("b30")
      if clickedbs.count("b26") > 0 and clickedbs.count("b27") > 0 and clickedbs.count("b28") > 0 and clickedbs.count("b29") > 0 and clickedbs.count("b30") > 0:
          tk.messagebox.showinfo(parent = self, title = "Bingo!", message = "You lose!")
      
class Window(tk.Tk):
  def __init__(self):
    super().__init__()
    self.geometry("300x300")
    self.title("Bingo")

    title = tk.Label(self, text="Bingo!", height = 4, width = 9)
    title.pack()
    
    open = tk.Button(self, text="Start", command=self.open_game)
    open.pack()  
  def open_game(self):
    game = Game(self)
    game.grab_set()
height = Window.winfo_height
width = Window.winfo_width

if __name__ == "__main__":
  start = Window()
  start.mainloop()