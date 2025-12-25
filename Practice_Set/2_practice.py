class Employee:
    salery = 136
    increment = 20
    
    @property
    def SelaryAfterIncrement (self):
        return (self.salery + self.salery * (self.increment/100))
    
    @SelaryAfterIncrement.setter
    def SelaryAfterIncrement (self, salery):
        self.increment = ((salery/self.salery) -1)*100


e = Employee()
e.SelaryAfterIncrement = 280
print(e.increment)