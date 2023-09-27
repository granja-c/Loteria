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
      
  
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.pick()
    kt.m()
    kt.tl()
    kt.pick()
    kt.m()
    kt.pick()
    kt.ta()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.tl()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.ta()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()  
    kt.tl()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.ta()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.pick()
    kt.m()
    
    pass  
  


if __name__ == "__main__":
    run_karel_program()
