import sys


class Machine_nan():
    kawotchou = 4

    def __init__(self, vites, koule, model, pwopriyete, gaz, tente, ane, pri):
        self.vites = vites
        self.koule = koule
        self.model = model
        self.pwopriyete = pwopriyete
        self.gaz = gaz
        self._tente = tente
        self.ane = ane
        self._pri = pri
        self.gaz_nbf = 0

    def akselere(self):
        if self.gaz >= 14 :
            self.vites += 34
            self.gaz -= 14
            print(f"INFO\nGaz    : {self.gaz} L\nVites  : {self.vites}\n=================")
        else:
            print("Al fe gaz ou pa gen ase !!")

    def frennen(self):
        if self.vites < 58:
            self.vites = 0
            print(f"INFO\nVites  : {self.vites}\n=================")
        else:
            self.vites -= 58
            print(f"INFO\nVites  : {self.vites}\n=================")
        # ====================
        if self.gaz < 7:
            self.gaz = 0
            print(f"INFO\nGaz    : {self.gaz} L\n=================")
        else:
            self.gaz -= 7
            print(f"INFO\nGaz    : {self.gaz} L\n=================")

    def vann_machin(self):
        print(f"Ansyen Pwopriyete : {self.pwopriyete}")
        self.pwopriyete = input("Pwopriyete     :   ")
        print(f"""Prix Machin nan : {self._pri} Gdes\nNouvo Pwopriyete : {self.pwopriyete}""")

    def douko(self):
        koule = ["Ble", "Nwa", "Rouj", "Oranj", "Jòn", "Maron", "Vèt", "Blan"]
        MENU = f"""
            **** ===== Chwazi koule  ou vle an ===== ****
            1. {koule[0]}
            2. {koule[1]}
            3. {koule[2]}
            4. {koule[3]}
            5. {koule[4]}
            6. {koule[5]}
            7. {koule[6]}
            8. Bay vag sou douko a.
               Fe yon chwa    :    """

        L = ['1', '2', '3', '4', '5', '6', '7', '8']
        ch = ""
        while ch not in L:
            ch = input(MENU)
            if ch not in L:
                print("Mauvais choix!")
            match ch:
                case '1':
                    self._pri += 200
                    self.koule = {koule[0]}
                    break
                case '2':
                    self._pri += 200
                    self.koule = {koule[1]}
                    break
                case '3':
                    self._pri += 200
                    self.koule = {koule[2]}
                    break
                case '4':
                    self._pri += 200
                    self.koule = {koule[3]}
                    break
                case '5':
                    self._pri += 200
                    self.koule = {koule[4]}
                    break
                case '6':
                    self._pri += 200
                    self.koule = {koule[5]}
                    break
                case '7':
                    self._pri += 200
                    self.koule = {koule[6]}
                    break
                case '8':
                    print(f"Ou pa fe chwa de lot koule : koule w la tj rete {self.koule} ")

        print(f"\t\tKoule : {self.koule} - New Prix : {self._pri}")


    def fe_gaz(self, qte_kob):
        prix_lit = 750 / 3.785
        print(f"== Prix 1 lit : {prix_lit}")
        if self.gaz >= 3500:
            print("Machine ou an foul!")
        else :
            self.gaz = qte_kob / prix_lit
            self.gaz_nbf += 1
            if self.gaz_nbf == 3:
                print(Machine_nan.prix)
                self._pri -= 1000
                self.gaz_nbf = 0


    def message_prix(self):
        print(f"🚗 Machin nan kòmanse pèdi valè, mesye/madam {self.pwopriyete}.")


    prix = property(message_prix)


    def menu(self):
        MENU = """
            **** ===== Manipilasyon Machin nan ===== ****
            1. Akselere Machine nan
            2. Frennen Machine nan
            3. Vann Machine nan
            4. Douko Machine nan
            5. Fe Gaz met nan Machine nan
            6. Quitter
               Fe yon chwa    :    """

        L = ['1', '2', '3', '4', '5', '6']
        while True:
            ch = ""
            while ch not in L:
                ch = input(MENU)
                if ch not in L:
                    print("Mauvais choix!")
                match ch:
                    case '1':
                        self.akselere()
                    case '2':
                        self.frennen()
                    case '3':
                        self.vann_machin()
                    case '4':
                        self.douko()
                    case '5':
                        #pase pou qte kob gaz wap fe la
                        self.fe_gaz(5000)
                    case "6":
                        print("Exit!!")
                        sys.exit()


m = Machine_nan(0, "Nwa", "Toyota", "Paul Denis", 0, False, 2012, 170000)
m.menu()
