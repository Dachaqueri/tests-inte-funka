from msilib.schema import Class


class Bil():
    hjul = 4

    def __init__(self, modell, pris) -> None:
        self.modell = modell
        self.pris = pris

    def presentera_bil(self):
        return "Den här bilen är av modellen {m} och kostar {p} kr".format(m=self.modell, p=self.pris)
#min_bil = Bil("Volkswagen Golf", 300000)
#print(min_bil.hjul)