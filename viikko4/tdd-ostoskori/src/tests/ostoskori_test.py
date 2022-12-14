import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_eri_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tuotetta(self):
        maito = Tuote("Maito", 3)
        jaffa = Tuote("Jaffa", 5)
        self.kori.lisaa_tuote(maito)        
        self.kori.lisaa_tuote(jaffa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_eri_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        jaffa = Tuote("Jaffa", 5)
        self.kori.lisaa_tuote(maito)        
        self.kori.lisaa_tuote(jaffa)
        self.assertEqual(self.kori.hinta(), 8)

    
    def test_saman_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)        
        self.kori.lisaa_tuote(maito)   
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_saman_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)        
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_eri_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        jaffa = Tuote("Jaffa", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(jaffa)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)


    def test_saman_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_kaksi_samaa_tuotetta_ostoskorissa_niin_ostos_tuotteen_niminen_ja_lkm_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)


    def test_kaksi_samaa_tuotetta_ostoskorissa_niin_ostos_tuotteen_niminen_ja_lkm_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)


    def test_kaksi_samaa_tuotetta_ostoskorissa_niin_ostos_tuotteen_niminen_ja_lkm_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)

    def test_korin_voi_tyhjentaa(self):
        maito = Tuote("Maito", 3)
        jaffa = Tuote("Jaffa", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(jaffa)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)