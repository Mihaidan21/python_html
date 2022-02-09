class Carte:
    VALORI = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # VALORI_INT = [15, 2, 3 , 4 , 5 , 6, 7,'8','9','10','J','Q','K']
    SIMBOLURI = ["Tr", "Ro", "In", "Pi"]

    def __init__(self, valoare, simbol):
        self.valoare = valoare
        self.simbol = simbol
    def __str__(self):
        return f"{self.valoare} {self.simbol}"
    

    # int(obiect)
    def __int__(self):
        try:
            int(self.valoare)
        except:
            valori_str =  ['J','Q','K', 'A']
            return 12 + valori_str.index(self.valoare ) 
        else:
            return int(self.valoare)

    # carte1 == carte2
    def __eq__(self, other):
        return self.valoare == other.valoare


    # carte1 < carte2
    def __lt__(self, other):
        return self.valoare < other.valoare 

    # carte1 > carte2
    def __gt__(self, other):
        return self.valoare > other.valoare


from random import shuffle 

class Pachet:
    def __init__(self):
        # self.carti = []
        # for val in Carte.VALORI:
        #     for simb in Carte.SIMBOLURI:
        #         obiect_carte = Carte(val, simb)
        #         self.carti.append(obiect_carte)
        self.carti = [ Carte(val, simb) for simb in Carte.SIMBOLURI for val in Carte.VALORI   ]

    def __str__(self):
        # return f"{list(map( str, self.carti))}"
        return f"{[ str(val) for val in self.carti]}"


    def shuffle(self):
        shuffle(self.carti)





class Jucator:
    def __init__(self):
        self.carti = []

    def joaca_carte(self):
        return self.carti.pop()

    def __str__(self):
        return f"Jucatorul are {len(self.carti)}: {[ str(val) for val in self.carti]}"


class Razboi:

    def __init__(self, pachet, jucator1, jucator2):
        self.pachet = pachet
        self.jucator1 = jucator1
        self.jucator2 = jucator2
        self.carti_castigate = []

    def imparte(self):
        self.pachet.shuffle()
        self.jucator1.carti = self.pachet.carti[:26]
        self.jucator2.carti = self.pachet.carti[26:]    

    def compara(self):
        carte1 = self.jucator1.joaca_carte()
        print("Cartea1 :", carte1, "jucata de jucatorul 1")
        carte2 = self.jucator2.joaca_carte()
        print("Cartea2 :", carte2, "jucata de jucatorul 2")
        if carte1 == carte2:
            self.razboi(int(carte1))
            print("RAZBOI!!!!!")
            self.carti_castigate.append(carte1)
            self.carti_castigate.append(carte2)
        elif carte1 < carte2:
            print("A castigat jucatorul 2")
            self.jucator2.carti.insert(0, carte1)
            self.jucator2.carti.insert(0, carte2)
            for _ in self.carti_castigate:
                self.jucator2.carti.insert(0, self.carti_castigate.pop())
        else: 
            print("A castigat jucatorul 1")
            self.jucator1.carti.insert(0, carte1)
            self.jucator1.carti.insert(0, carte2)
            for _ in self.carti_castigate:
                self.jucator1.carti.insert(0, self.carti_castigate.pop())

    def razboi(self, nr_carti):
        
        for _ in range(nr_carti-1):
            self.carti_castigate.append(self.jucator1.carti.pop()) 
            self.carti_castigate.append(self.jucator2.carti.pop()) 
        self.compara()

    def asigneaza_carte(self):
        pass
    

    def joaca_continuu(self):
        while len(self.jucator1.carti)>0 and len(self.jucator2.carti)>0:
            self.compara()
        else:
            print("Jocul s-a terminat")
            rez = "Jucatorul1 a castigat" if len(self.jucator2.carti) == 0 else "Jucatorul2 a castigat"
            print(rez)




pachet = Pachet()
# print(len(pachet.carti))
# print(pachet)

# print(" ---")
# pachet.shuffle()

# print(pachet)

# carte = Carte("10", "Ro")
# print(int(carte))



marina = Jucator()
adriana = Jucator()
joc = Razboi(pachet, marina, adriana)
joc.imparte()

joc.joaca_continuu()




