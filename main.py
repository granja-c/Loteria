import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import *
import random

blue = "#83c5fc"
blue2 = "#78c2ff"
mark = "#f3f768"

clickedbs = []
global buttonImages
numButtons = 100
buttonImages = [0]*100
class Game(tk.Toplevel):
  def __init__(self, parent):
    global buttonImages
    super().__init__(parent)
    self.geometry("300x300")
    self.title("¡Lotería!") 
    self.configure(background = blue)
    
    space1 = tk.Label(self, bg = blue, text="", height = 1, width = 2)
    space1.grid(row = 0, column = 0)
    space2 = tk.Label(self, bg = blue, text=" ", height = 2, width = 4)
    space2.grid(row = 1, column = 1)

    yourslbl = tk.Label(self, bg = blue, text="Your Board", height = 3, width = 10)
    yourslbl.place(x = 90, y = 20)
    theirslbl = tk.Label(self, bg = blue, text="Opponent's Board", height = 3, width = 15)
    theirslbl.place(x = 430, y = 20)
    numButtons = 32
    photos = ["alacran.png", "arana.png", "arbol.png", "arpa.png", "bandera.png", "bando.png", "barril.png", "bota.png", "cala.png", "camaron.png", "catrin.png", "chalupa.png", "corazon.png", "corona.png", "cotorro.png", "dama.png", "diablo.png", "esca.png", "estrella.png", "luna.png",  "melon.png", "muerte.png", "mundo.png", "musico.png", "nopal.png", "pajaro.png", "pesc.png",  "rana.png", "rosa.png", "sanda.png", "sol.png", "tambor.png"]
    photos = list(set(photos))
    buttonImages = [0]*numButtons
    random.shuffle(photos)
    def randpic(buttonNumber):
      choice = photos[buttonNumber]
      img = Image.open(choice)
      img.putalpha(190)
      img = img.resize((46, 69))
      pic = ImageTk.PhotoImage(img)
      buttonImages[buttonNumber] = pic
      return buttonImages[buttonNumber] 
    
    button1 = tk.Button(self, height= 67, width = 54, image= randpic(0), command = lambda: clicked(self, button1))
    button1.grid(row = 2, column = 1)
    button2 = tk.Button(self, image= randpic(1), height= 67, width = 54, command = lambda:clicked(self, button2))
    button2.grid(row = 2, column = 2)
    button3 = tk.Button(self, image= randpic(2), height= 67, width = 54, command = lambda:clicked(self, button3))
    button3.grid(row = 2, column = 3)
    button4 = tk.Button(self, image= randpic(3), height= 67, width = 54, command = lambda:clicked(self, button4))
    button4.grid(row = 2, column = 4)
    
    button5 = tk.Button(self, image= randpic(4), height= 67, width = 54, command = lambda:clicked(self, button5))
    button5.grid(row = 3, column = 1)
    button6 = tk.Button(self, image= randpic(5), height= 67, width = 54, command = lambda:clicked(self, button6))
    button6.grid(row = 3, column = 2)
    button7 = tk.Button(self, image= randpic(6), height= 67, width = 54, command = lambda:clicked(self, button7))
    button7.grid(row = 3, column = 3)
    button8 = tk.Button(self, image= randpic(7), height= 67, width = 54, command = lambda:clicked(self, button8))
    button8.grid(row = 3, column = 4)
    
    button9 = tk.Button(self, image= randpic(8), height= 67, width = 54, command = lambda:clicked(self, button9))
    button9.grid(row = 4, column = 1)
    button10 = tk.Button(self, image= randpic(9), height= 67, width = 54, command = lambda:clicked(self, button10))
    button10.grid(row = 4, column = 2)
    button11 = tk.Button(self, image= randpic(10), height= 67, width = 54, command = lambda:clicked(self, button11))
    button11.grid(row = 4, column = 3)
    button12 = tk.Button(self, image= randpic(11), height= 67, width = 54, command = lambda:clicked(self, button12))
    button12.grid(row = 4, column = 4)
    
    button13 = tk.Button(self, image= randpic(12), height= 67, width = 54, command = lambda: clicked(self, button13))
    button13.grid(row = 5, column = 1)
    button14 = tk.Button(self, image= randpic(13), height= 67, width = 54, command = lambda:clicked(self, button14))
    button14.grid(row = 5, column = 2)
    button15 = tk.Button(self, image= randpic(14), height= 67, width = 54, command = lambda: clicked(self, button15))
    button15.grid(row = 5, column = 3)
    button16 = tk.Button(self, image= randpic(15), height= 67, width = 54, command = lambda:clicked(self, button16))
    button16.grid(row = 5, column = 4)
    
    random.shuffle(photos)
    
    button17 = tk.Button(self, height= 67, width = 54, image= randpic(16), command = lambda:clicked(self, button17))
    button17.grid(row = 2, column = 7)
    button18 = tk.Button(self, image= randpic(17), height= 67, width = 54, command = lambda: clicked(self, button18))
    button18.grid(row = 2, column = 8)
    button19 = tk.Button(self, image= randpic(18), height= 67, width = 54, command = lambda:clicked(self, button19))
    button19.grid(row = 2, column = 9)
    button20 = tk.Button(self, image= randpic(19), height= 67, width = 54, command = lambda: clicked(self, button20))
    button20.grid(row = 2, column = 10)

    button21 = tk.Button(self, image= randpic(20), height= 67, width = 54, command = lambda: clicked(self, button21))
    button21.grid(row = 3, column = 7)
    button22 = tk.Button(self, image= randpic(21), height= 67, width = 54, command = lambda: clicked(self, button22))
    button22.grid(row = 3, column = 8)
    button23 = tk.Button(self, image= randpic(22), height= 67, width = 54, command = lambda: clicked(self, button23))
    button23.grid(row = 3, column = 9)
    button24 = tk.Button(self, image= randpic(23), height= 67, width = 54, command = lambda: clicked(self, button24))
    button24.grid(row = 3, column = 10)
    
    button25 = tk.Button(self, image= randpic(24), height= 67, width = 54, command = lambda: clicked(self, button25))
    button25.grid(row = 4, column = 7)
    button26 = tk.Button(self, image= randpic(25), height= 67, width = 54)
    button26.grid(row = 4, column = 8)
    button27 = tk.Button(self, image= randpic(26), height= 67, width = 54)
    button27.grid(row = 4, column = 9)
    button28 = tk.Button(self, image= randpic(27), height= 67, width = 54)
    button28.grid(row = 4, column = 10)
    
    button29 = tk.Button(self, image= randpic(28), height= 67, width = 54)
    button29.grid(row = 5, column = 7)
    button30 = tk.Button(self, image= randpic(29), height= 67, width = 54)
    button30.grid(row = 5, column = 8)
    button31 = tk.Button(self, image= randpic(30), height= 67, width = 54)
    button31.grid(row = 5, column = 9)
    button32 = tk.Button(self, image= randpic(31), height= 67, width = 54)
    button32.grid(row = 5, column = 10)

    space3 = tk.Label(self, bg = blue, text="", height = 1, width = 5)
    space3.grid(row = 0, column = 4)
    space4 = tk.Label(self, bg = blue, text="", height = 1, width = 4)
    space4.grid(row = 0, column = 5)
    space5 = tk.Label(self, bg = blue, text="", height = 1, width = 9)
    space5.grid(row = 0, column = 6)
    space6 = tk.Label(self, bg = blue, text="", height = 1, width = 4)
    space6.grid(row = 0, column = 7)
    space7 = tk.Label(self, bg = blue, text="", height = 1, width = 4)
    space7.grid(row = 0, column = 8)
    
    def clicked(self, button):
      if button == button1:
        if button1['image'] == testlbl['image']:
          button1.configure(bg = mark)
          clickedbs.append("b1")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b13") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button2:
        if button2['image'] == testlbl['image']:
          button2.configure(bg = mark)
          clickedbs.append("b2")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b14") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button3:
        if button3['image'] == testlbl['image']:
          button3.configure(bg = mark)
          clickedbs.append("b3")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b15") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button4:
        if button4['image'] == testlbl['image']:
          button4.configure(bg = mark)
          clickedbs.append("b4")
        if clickedbs.count("b1") > 0 and clickedbs.count("b2") > 0 and clickedbs.count("b3") > 0 and clickedbs.count("b4") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b16") > 0 or clickedbs.count("b4") and clickedbs.count("b7") and clickedbs.count("b10") and clickedbs.count("b13"):
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
          
      if button == button5:
        if button5['image'] == testlbl['image']:
          button5.configure(bg = mark)
          clickedbs.append("b5")
        if clickedbs.count("b5") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b13") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")    
      if button == button6:
        if button6['image'] == testlbl['image']:
          button6.configure(bg = mark)
          clickedbs.append("b6")
        if clickedbs.count("b5") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b14") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button7:
        if button7['image'] == testlbl['image']:
          button7.configure(bg = mark)
          clickedbs.append("b7")
        if clickedbs.count("b5") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b15") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b13") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button8:
        if button8['image'] == testlbl['image']:
          button8.configure(bg = mark)
          clickedbs.append("b8")
        if clickedbs.count("b5") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b8") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b16") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
          
      if button == button9:
        if button9['image'] == testlbl['image']:
          button9.configure(bg = mark)
          clickedbs.append("b9")
        if clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b13") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button10:
        if button10['image'] == testlbl['image']:
          button10.configure(bg = mark)
          clickedbs.append("b10")
        if clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b14") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b13") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button11:
        if button11['image'] == testlbl['image']:
          button11.configure(bg = mark)
          clickedbs.append("b11")
        if clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b15") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button12:
        if button12['image'] == testlbl['image']:
          button12.configure(bg = mark)
          clickedbs.append("b12")
        if clickedbs.count("b9") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b12") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b16") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
          
      if button == button13:
        if button13['image'] == testlbl['image']:
          button13.configure(bg = mark)
          clickedbs.append("b13")
        if clickedbs.count("b13") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b16") > 0 or clickedbs.count("b1") > 0 and clickedbs.count("b5") > 0 and clickedbs.count("b9") > 0 and clickedbs.count("b13") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b13") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button14:
        if button14['image'] == testlbl['image']:
          button14.configure(bg = mark)
          clickedbs.append("b14")
        if clickedbs.count("b13") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b16") > 0 or clickedbs.count("b2") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b10") > 0 and clickedbs.count("b14") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button15:
        if button15['image'] == testlbl['image']:
          button15.configure(bg = mark)
          clickedbs.append("b15")
        if clickedbs.count("b13") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b16") > 0 or clickedbs.count("b3") > 0 and clickedbs.count("b7") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b15") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")
      if button == button16:
        if button16['image'] == testlbl['image']:
          button16.configure(bg = mark)
          clickedbs.append("b16")
        if clickedbs.count("b13") > 0 and clickedbs.count("b14") > 0 and clickedbs.count("b15") > 0 and clickedbs.count("b16") > 0 or clickedbs.count("b4") > 0 and clickedbs.count("b8") > 0 and clickedbs.count("b12") > 0 and clickedbs.count("b16") > 0 or  clickedbs.count("b1") > 0 and clickedbs.count("b6") > 0 and clickedbs.count("b11") > 0 and clickedbs.count("b16") > 0:
          tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You win!")     
    
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    a = list(range(0, len(photos)))
    x = random.choice(a)
    a.remove(x)
    pic = buttonImages[x]
    
    testlbl = tk.Label(self, bg = mark, image = pic, height = 95, width = 72)
    testlbl.place(x = 280, y = 57)
    nextbutton = tk.Button(self, bg = blue2, text="next" , height= 2, width = 6, command = lambda: next())
    nextbutton.place(x = 280, y = 160)
    
    def next():
      x = random.choice(a)
      a.remove(x)
      pic = buttonImages[x]
      testlbl['image'] = pic

      if button17['image'] == testlbl['image']:
        button17.configure(bg = mark)
        clickedbs.append("b17")
      if button18['image'] == testlbl['image']:
        button18.configure(bg = mark)
        clickedbs.append("b18")
      if button19['image'] == testlbl['image']:
        button19.configure(bg = mark)
        clickedbs.append("b19")
      if button20['image'] == testlbl['image']:
        button20.configure(bg = mark)
        clickedbs.append("b20")
      if button21['image'] == testlbl['image']:
        button21.configure(bg = mark)
        clickedbs.append("b21")
      if button22['image'] == testlbl['image']:
        button22.configure(bg = mark)
        clickedbs.append("b22")
      if button23['image'] == testlbl['image']:
        button23.configure(bg = mark)
        clickedbs.append("b23")
      if button24['image'] == testlbl['image']:
        button24.configure(bg = mark)
        clickedbs.append("b24")
      if button25['image'] == testlbl['image']:
        button25.configure(bg = mark)
        clickedbs.append("b25")
      if button26['image'] == testlbl['image']:
        button26.configure(bg = mark)
        clickedbs.append("b26")
      if button27['image'] == testlbl['image']:
        button27.configure(bg = mark)
        clickedbs.append("b27")
      if button28['image'] == testlbl['image']:
        button28.configure(bg = mark)
        clickedbs.append("b28")
      if button29['image'] == testlbl['image']:
        button29.configure(bg = mark)
        clickedbs.append("b29")
      if button30['image'] == testlbl['image']:
        button30.configure(bg = mark)
        clickedbs.append("b30")
      if button31['image'] == testlbl['image']:
        button31.configure(bg = mark)
        clickedbs.append("b31")
      if button32['image'] == testlbl['image']:
        button32.configure(bg = mark)
        clickedbs.append("b32")
        
      if clickedbs.count("b17") and clickedbs.count("b18") and clickedbs.count("b19") and clickedbs.count("b20") or clickedbs.count("b21") and clickedbs.count("b22") and clickedbs.count("b23") and clickedbs.count("b24") or clickedbs.count("b25") and clickedbs.count("b26") and clickedbs.count("b27") and clickedbs.count("b28") or clickedbs.count("b29") and clickedbs.count("b30") and clickedbs.count("b31") and clickedbs.count("b32") or clickedbs.count("b17") and clickedbs.count("b21") and clickedbs.count("b25") and clickedbs.count("b29") or clickedbs.count("b18") and clickedbs.count("b22") and clickedbs.count("b26") and clickedbs.count("b30") or clickedbs.count("b19") and clickedbs.count("b23") and clickedbs.count("b27") and clickedbs.count("b31") or clickedbs.count("b20") and clickedbs.count("b24") and clickedbs.count("b28") and clickedbs.count("b32") or clickedbs.count("b17") and clickedbs.count("b22") and clickedbs.count("b27") and clickedbs.count("b32") or clickedbs.count("b20") and clickedbs.count("b23") and clickedbs.count("b26") and clickedbs.count("b29"):
        tk.messagebox.showinfo(parent = self, title = "¡Lotería!", message = "You lose!")

class Window(tk.Tk):
  def __init__(self):
    super().__init__()
    self.geometry("300x300")
    self.title("¡Lotería!")
    self.configure(bg = blue)

    title = tk.Label(self, bg = blue, text="Lotería!", height = 3, width = 15)
    title.place(x = 240, y = 45)
    
    open = tk.Button(self, bg = blue2, text="Start", height = 1, width = 8, command=self.open_game)
    open.place(x = 255, y = 110)

  def open_game(self):
    game = Game(self)
    game.grab_set()

if __name__ == "__main__":
  start = Window()
  start.mainloop()