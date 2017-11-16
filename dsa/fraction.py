class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom 

    def __str__(self):
        return str(self.top) + '/' + str(self.bottom)
    
    def __add__(self, other): # Operator overriding n
        new_top = self.top * other.bottom + other.top + self.bottom
        new_bottom = self.bottom * other.bottom 
        return Fraction(new_top, new_bottom)

ob = Fraction(2, 3)
oc = Fraction(3, 4)
print(ob + oc)