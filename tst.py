import tkinter as tk
# import random
from PIL import ImageTk, Image
red = "#eb4034"
class Window(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.geometry('300x300')
    self.title('Toplevel Window')
    new = tk.Button(self, text='Close', command=self.destroy)
    new.pack()
    
    


class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.geometry('300x200')
    self.title('Main Window')
    button1 = tk.Button(self, bg = red, text= "open", image = getRandomImage((150, 150), 0), command=self.open_window)
  
    button1.pack(expand=True)
  def open_window(self):
    window = Window(self)
    window.grab_set()
    
  numButtons = 1
  allBtnImages = ["bota.png"]
  global imageChoices, buttonImages
  imageChoices = [i for i in allBtnImages]
  buttonImages = [0]*numButtons
def getRandomImage(size, buttonNumber):
    global buttonImages, imageChoices
    # indx = random.randint(0, len(imageChoices)-1)
    choice = imageChoices.pop(0) 
    img = Image.open(choice)
    img.putalpha(175)
    img = img.resize(size)
    pic = ImageTk.PhotoImage(img)
    buttonImages[buttonNumber] = pic
    return buttonImages[buttonNumber]
  
if __name__ == "__main__":
    app = App()
    app.mainloop()