from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        amount = 0
        for item in self.sisalto.values():
            amount += item.lukumaara()    
        return amount
        
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        price = 0
        for product in self.sisalto.values():
            price += product.hinta()
        return price

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi in self.sisalto:
            self.sisalto[lisattava.nimi].muuta_lukumaaraa(1)
        else:
            self.sisalto[lisattava.nimi] = Ostos(lisattava)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.sisalto.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
