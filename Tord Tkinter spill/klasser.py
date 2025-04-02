from random import randint 
#forskjellige klasser til forskjellige personer/udyr!
class Vesner:
    #klasse som fungerer som en base til andre vesner!
    def __init__(self, navn, health, damage):
        self.navn = navn            # Navnet på fienden
        self.health = health        # Hvor mye helse fienden har
        self.damage = damage        # Hvor mye skade fienden gjør per angrep
    
    def attack(self):
        """Angrip et mål og gjør skade basert på fiendens skade."""
        # Returner skaden som kan brukes til å redusere helsen til målet
        return randint(0,self.damage)
    
    def motangrep(self):
        return randint(0,self.damage/2)
    
    def take_damage(self, amount):
        """Reduser fiendens helse basert på mottatt skade."""
        self.health -= amount
        print(f"{self.name} tar {amount} skade. Gjenstående helse: {self.health}")
        
        # Sjekker om fienden er død
        if self.health <= 0:
            print(f"{self.name} har blitt beseiret!")
            return True  # Returner True hvis fienden er død
        return False  # Returner False hvis fienden fortsatt lever

class Helt(Vesner):
    #klassen til den snille helten
    def __init__(self, navn, health, damage, wepons = 0, armor = 0):
        super().__init__(navn, health, damage)
        self.wepons = wepons
        self.armor = armor
    
    def dodge(self):
        test = randint(1,2)
        if test == 2:
            return ("du klarte og hoppe unna")
        else:
            return ("monsteret tar tak i deg, og klarer å slå deg")
    def attack_helt(self, damage , wepons):
        self.damage += wepons
        print(f"{self.navn} tar {damage} på han")
        return damage
    def blokker(self):
        print ("hei")

class Gjenstander:
    def __init__(self, navn="noName"):
        self.navn = navn
        

    

