from abc import ABC, abstractmethod
TI = 0.004
TU = 0.02
RA = 0.2
RV = 2500

class Calculate(ABC):
    @abstractmethod
    def cr(self):
        pass

    def __init__(self): #run()
        self.u = 0.5
        for j in range(10):
            print("U:", self.u)
            while True:
                try:
                    print("I: ", end="")
                    self.i = float(input())
                    break
                except Exception as e:
                    print(f"Wrong value: {e}, needs float")
            self.calculate()
            self.u = round(self.u+0.05, 2)
                    
    def calculate(self):
        self.usi = round(self.u/self.i, 2)
        print("U/I:", self.usi)
        self.r = self.cr()
        print("R:", self.r)
        teto = self.r*(TU/self.u+TI/self.i)
        self.teto = round(teto,1)
        print("θ:", self.teto)
        print("--------------------")

class A(Calculate):
    def cr(self):
        return round(self.usi-RA, 1)

class B(Calculate):
    def cr(self):
        return round((self.usi-1/RV)**-1, 1)

A()
B()
    
