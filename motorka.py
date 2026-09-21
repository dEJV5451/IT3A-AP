class MOTORKA:
    def __init__(self, značka:str, kategorie:int, stav_nádrže:int, stav_stojánku:str = "vyklopen", palivo:int = "500"):
        self.značka = značka
        self.kategorie = kategorie
        self.stav_nádrže = stav_nádrže
        self.stav_stojánku = stav_stojánku
        self.palivo = palivo
        pass

    def zatoč_plyn(self):
        return "???"

    def popiš_motorku(self):
        return f"Má {self.značka}, nádrž {self.stav_nádrže}, stojánek {self.stav_stojánku}"

    def vypiš_stav_stojánku(self):
        return f"Aktuální stav: {self.stav_stojánku}"

    def změna_stojánku(self, nový_stav_stojánku):
        self.stav_stojánku = nový_stav_stojánku
        return f"Stojánek: {nový_stav_stojánku}"

    def popojeď(self, spotřeba: int = 10):
        if self.palivo >= spotřeba:
            self.palivo -= spotřeba
            return f"Motorka popojela, zbývá: {self.palivo}"
        else:
            return "Motorka nemá dostatek paliva"

    def vypiš_palivo(self):
        return f"Aktuálně mám v nádrži {self.palivo}"

    def zadej_tankovani(self):
        tankovani = input("Zadej množství, které chceš natankovat: ")

        try:
            mnozstvi = int(tankovani)

            if mnozstvi > 0:
                self.palivo += mnozstvi
                return f"Natankoval jsi {mnozstvi}, nyní máš {self.palivo}"
            else:
                return "Nemůžeš natankovat 0!"

        except ValueError:
            return "Musíš zadat číslo!"


motorka = MOTORKA("Honda", 3, 100, "vyklopen", 500)

print(motorka.značka)
print(motorka.kategorie)
print(motorka.stav_nádrže)
print(motorka.stav_stojánku)
print(motorka.palivo)

print(motorka.popiš_motorku())
print(motorka.vypiš_stav_stojánku())
print(motorka.popojeď())
print(motorka.vypiš_palivo())
