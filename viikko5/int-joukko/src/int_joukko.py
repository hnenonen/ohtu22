KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError('Virheellinen kapasiteetti')
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError('Virheellinen kasvatuskoko')
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, kuuluuko_joukkoon: int) -> bool:
        for luku in self.lukujono:
            if luku == kuuluuko_joukkoon:
                return True
        return False

    def lisaa(self, lisattava_luku: int) -> bool:
        if not self.kuuluu(lisattava_luku):
            self.lukujono[self.alkioiden_lkm] = lisattava_luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            if self.alkioiden_lkm == len(self.lukujono):
                vanha_joukko = self.lukujono
                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(vanha_joukko, self.lukujono)
            return True
        return False

    def poista(self, poistettava: int) -> bool:
        poistettu = False
        for kohta, luku in enumerate(self.lukujono):
            if luku == poistettava:
                self.lukujono[kohta] = 0
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                poistettu = True
            if poistettu:  
                self.lukujono[kohta] = self.lukujono[kohta + 1]
                self.lukujono[kohta + 1] = 0
                if kohta >= len(self.lukujono) - 2:
                    return True
        return False

    @staticmethod
    def kopioi_taulukko(kopioitava: list, kohde: list):
        for kohta, alkio in enumerate(kopioitava):
            kohde[kohta] = alkio

    def mahtavuus(self) -> int:
        return self.alkioiden_lkm

    def to_int_list(self):
        return [self.lukujono[kohta] for kohta in range(self.alkioiden_lkm)]

    
    @staticmethod
    def yhdiste(lukujono1, lukujono2):
        tulos = IntJoukko()
        for alkio in lukujono1.to_int_list():
            tulos.lisaa(alkio)
        for alkio in lukujono2.to_int_list():
            tulos.lisaa(alkio)
        return tulos

    @staticmethod
    def leikkaus(lukujono1, lukujono2):
        tulos = IntJoukko()
        for alkio in lukujono1.to_int_list():
            if lukujono2.kuuluu(alkio):
                tulos.lisaa(alkio)
        return tulos

    @staticmethod
    def erotus(lukujono1, lukujono2):
        tulos = IntJoukko()
        for alkio in lukujono1.to_int_list():
            if not lukujono2.kuuluu(alkio):
                tulos.lisaa(alkio)
        return tulos

    def __str__(self):
        cleaned_str = str(self.to_int_list()).strip("],[")
        return ("{"+cleaned_str+"}")