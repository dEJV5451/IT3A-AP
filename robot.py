class ROBOT:
    def __init__(self, oznaceni:int, baterie:int, ukol:str = "plavu"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass
def zvuk(self):
    return "???"

def diagnostika(self):
    return f"Jsem {self.oznaceni}, mám {self.baterie} %"

def aktuální_úkol(self):
    return f"Právě {self.ukol}"

def zadej_úkol(self, nový_úkol):
    self.ukol = nový_úkol
    return f"Nyní jdu {nový_úkol}"

robot = ROBOT(115, 100, "plavu")
print(robot.oznaceni)
print(robot.baterie)
print(robot.ukol)
