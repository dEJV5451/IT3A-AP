import random
class Kocka:
    def __init__(self, jmeno:str, barva:str):
        self.barva = barva
        self.jmeno = jmeno
        pass

    def zvuk(self):
        return f"Mňau, mňau!"
    
    def barva(self):
        return f"Mám {self.barva}"
    
    def poskrabe(self):
        return f"{self.jmeno} na tebe zaútočila!"
    
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return f"Utelk jsi před {self.jmeno}!"
        else:
            return f"{self.jmeno} tě poškrábala!"
        
kocka = Kocka("Hulvát1", "Černá")
print(kocka.jmeno)
print(kocka.barva)
print(kocka.zvuk())
print(kocka.poskrabe())
print(kocka.pohladit())
