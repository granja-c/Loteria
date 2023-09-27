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
        

    def doubleL(self):
        """Print 2 L's with beepers"""
        self.l()
        self.l()


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.tr()
    kt.h()
    kt.e()
    kt.doubleL()
    kt.o()

    pass


if __name__ == "__main__":
    run_karel_program()
