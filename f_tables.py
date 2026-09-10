from abc import ABC, abstractmethod
from typing import Optional, Callable

TI = 0.004
TU = 0.02
RA = 0.2
RV = 2500

class Calculate(ABC):
    @abstractmethod
    def cr(self):
        pass

    def __init__(self, input: Optional[Callable] = None):
        self.input_provider = input or self._default_input
        self.u = 0.5
        self.i = 0.0
        self.usi = 0.0
        self.r = 0.0
        self.teto = 0.0

    def run(self) -> None:
        for _ in range(10):
            print("U:", self.u)
            self.i = self.input_provider("I: ")
            self.calculate()
            self.u = round(self.u+0.05, 2)

    def _default_input(self, promt: str) -> float:
        while True:
            try:
                return float(input(promt))
            except ValueError as e:
                print(f"Wrong value: {e}, needs float")
        
                    
    def calculate(self) -> None:
        self.usi = round(self.u/self.i, 2)
        print("U/I:", self.usi)
        self.r = self.cr()
        print("R:", self.r)
        teto = self.r*(TU/self.u+TI/self.i)
        self.teto = round(teto,1)
        print("θ:", self.teto)
        print("--------------------")

class A(Calculate):
    def cr(self) -> float:
        return round(self.usi-RA, 1)

class B(Calculate):
    def cr(self) -> float:
        return round((self.usi**-1-1/RV)**-1, 1)
    
if __name__ == "__main__":
    A().run()
    B().run()
