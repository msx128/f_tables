from abc import ABC, abstractmethod
from typing import Optional, Callable

TI = 0.004
TU = 0.02
RA = 0.2
RV = 2500

# parent with core logic
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
        self.arr_r = []

    def run(self) -> list[float]:
        for _ in range(10):
            print("U:", self.u)
            self.i = self.input_provider("I: ")
            self.calculate()
            self.u = round(self.u+0.05, 2)
        return self.arr_r

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
        self.arr_r.append(self.r)
        teto = self.r*(TU/self.u+TI/self.i)
        self.teto = round(teto,1)
        print("θ:", self.teto)
        print("--------------------")

# r-calculation differences
class A(Calculate):
    def cr(self) -> float:
        return round(self.usi-RA, 1)

class B(Calculate):
    def cr(self) -> float:
        return round((self.usi**-1-1/RV)**-1, 1)

def ro(rsr: float, d: float, l: float):
    return (rsr * 3.14 * d*d) / (4 * l)

def h():
    # fix it?
    print("Пожалуйста диаметр без 10**-3")
    print("В ответ просто добавить значение ро и умножить на 10**-6")
    zaglushka = A()
    d = Calculate._default_input(zaglushka,"D: ")
    l = Calculate._default_input(zaglushka,"l: ")
    return (d, l)
    
# run
if __name__ == "__main__":
    n = A().run()
    n2 = B().run()
    n.extend(n2)
    rsr = round(sum(n)/20, 3)
    print(rsr)
    print(round(rsr, 1))
    d, l = h()
    print("ρ:", ro(rsr, d, l))
