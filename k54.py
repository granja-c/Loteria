from stanfordkarel import *


class ktools:

    def m(self):
        """Move"""
        move()

    def tl(self):
        """Turn left"""
        turn_left()

    def tr(self):
        """Turn right"""
        self.tl()
        self.tl()
        self.tl()

    def ta(self):
        """Turn around"""
        self.tl()
        self.tl()

    def put(self):
        """Put beeper"""
        put_beeper()

    def pick(self):
        """Pick beeper"""
        pick_beeper()

    def put2(self):
        """Put down 2 beepers"""
        self.put()
        self.m()
        self.put()

    def put5(self):
        """Put down 5 beepers"""
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.put()

    def h(self):
        """Print H with beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def e(self):
        """Print E with beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.put2()
        self.tr()
        self.m()
        self.m()
        self.tr()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.put2()
        self.m()
        self.m()

    def l(self):
        """Print L with beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.put2()
        self.m()
        self.m()

    def o(self):
        """Print O with beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.put2()
        self.m()
        self.tr()
        self.put5()
        self.tr()
        self.m()
        self.put2()
        self.ta()
        self.m()
        self.m()
        self.m()
        self.m()

    def doubleL(self):
        """Print 2 L's with beepers"""
        self.l()
        self.l()

    def m3(self):
        self.m()
        self.m()
        self.m()

    def m4(self):
        self.m()
        self.m()
        self.m()
        self.m()

    def m5(self):
        self.m()
        self.m()
        self.m()
        self.m()
        self.m()

    def pick3(self):
        self.pick()
        self.m()
        self.pick()
        self.m()
        self.pick()

    def c(self):
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.put2()
        self.ta()
        self.m()
        self.tl()
        self.m4()
        self.tl()
        self.put2()
        self.m()
        self.m()

    def a(self):
        self.tl()
        self.put2()
        self.m()
        self.put2()
        self.tr()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.ta()
        self.m()
        self.m()
        self.put()
        self.tl()
        self.m()
        self.tl()
        self.put2()
        self.ta()
        self.m()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()

    def M(self):
        """Print M /w beepers"""
        self.tl()
        self.put2()
        self.m()
        self.put2()
        self.tr()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.ta()
        self.m()
        self.tl()
        self.m()
        self.tr()
        self.put2()
        self.ta()
        self.m()
        self.m()
        self.tr()
        self.m()
        self.put()
        self.m()
        self.tr()
        self.m()
        self.put2()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()

    def i(self):
        self.tl()
        self.put5()
        self.ta()
        self.m4()
        self.tl()
        self.m()
        self.m()

    
    def fic(self) -> bool:
        return front_is_clear()

    def fib(self) -> bool:
        return not self.fic()

    def ric(self) -> bool:
        self.tr()
        if self.fic():
            self.tl()
            return True
        self.tl()
        return False
   
    def rib(self) -> bool:
        return not self.ric()

    def lic(self) -> bool:
        self.tl()
        if self.fic():
            self.tr()
            return True
        self.tr()
        return False

    def lib(self) -> bool:
        return not self.lic()

    def mazemove(self):
        if self.fib():
            self.tl()
        else:
            self.m()
            if self.ric():
                self.tr()
                self.m()
                if self.ric():
                    self.tr()
                    self.m()
        pass

    def mazemove2(self):
      if not onbeeper():
        while self.rib() and self.fic():
          self.m()
          while self.fib():
            self.tl()
            if self.ric():
              self.tr()
              self.m()
              if self.ric():
                self.tr()
                self.m()
      else:
        self.pick()

    def treasurehunt(self):
      i = 0
      while i != 5:
        while not self.onbeep():
          self.m()
        while self.onbeep():
          self.pick()
          i += 1
        if i == 1:
          while not facing_north():
            self.tl()
          i == 0
        elif i == 2:
          while not facing_west():
            self.tl()
          i == 0
        elif i == 3:
          while not facing_south():
            self.tl()
          i == 0
        elif i == 4:
          while not facing_east():
            self.tl()
          i == 0


  
    def carpet1(self):
        if (self.rib() and self.fib() and self.lib()):
          self.put()
          self.ta()
          self.m()
          self.tl()
        self.ta()
        self.m()
        self.tl()
      
    def carpet2(self):
        if (self.fic() and self.lib() and self.rib()):
          while (self.fic() and self.lib() and self.rib()):
            self.m()
            if self.fib():
              self.ta()
              while (self.lib() and self.rib()):
                self.put()
                self.m()

              
    def zero(self):
      self.tl()
      self.put5()
      self.tr()
      self.m()
      self.put()
      self.m()
      self.tr()
      self.put5()
      self.tr()
      self.m()
      self.put()
      self.ta()
      self.m()
      self.m()
      self.m()

    def mm(self, num):
      """multi-move"""
      for number in range(0, num):
        self.m()

    def putm(self, num):
      """multi-put"""
      for i in range(num - 1):
        self.put()
        self.m()
      self.put()

    def pickm(self, num):
      """multi-pick"""
      for _ in range(num - 1):
        self.pick()
        self.m()
      self.pick()
    
    def zero(self):
      self.tl()
      self.put5()
      self.tr()
      self.m()
      self.put()
      self.m()
      self.tr()
      self.put5()
      self.tr()
      self.m()
      self.put()
      self.ta()
      self.m()
      self.m()
      self.m()

    def onbeep(self):
      return beepers_present()

    def jump(self):
      """Jump for 510"""
      while self.fic():
        self.m()
      self.tl()
      while self.rib():
        self.m()
      self.tr()
      self.m()
      self.tr()
      while self.fic():
        self.m()
      self.tl()

    def jump2(self):
      """For 511"""
      while self.fic():
        self.m()
      self.tl()
      while self.rib():
        self.m()
      self.tr()
      self.m()
      if self.ric():
        self.tr()
        self.m()
      else:
        while self.rib():
          self.m()
        self.tr()
        self.m()
      while self.rib() and self.fic():
        self.m()
      self.tl()

      
    def find(self):
      """for 515"""
      while not facing_north():
        self.tl()
      self.m()
      if not self.onbeep():
        self.tl()
        self.m()
        self.tl()
        self.m()
      for _ in range(2):
        if not self.onbeep():
          self.m()
          self.tl()
          self.m()
      pass  
      
def main():
    """ Karel code goes here! """
    kt = ktools()
    b = 0
  
    kt.mm(4)
    kt.tl()
    kt.mm(4)
    while kt.onbeep():
      kt.pick()
      b += 1
    if (b % 2) == 0:
      kt.tr()
      kt.m()
    else:
      kt.tl()
      kt.m()
    while kt.onbeep():
      kt.pick()
      
    pass


if __name__ == "__main__":
    run_karel_program()
